SET SERVEROUTPUT ON SIZE 1000000;
-- FAIL: Tell sqlplus not to trim output lines.
SET TRIMOUT OFF;
SET TRIMSPOOL OFF;

SET PAGESIZE 0;
SET NEWPAGE 0;
SET SPACE 0;
SET LINESIZE 1000;
SET ECHO OFF;
SET FEEDBACK OFF;
SET VERIFY OFF;
SET HEADING OFF;
SET MARKUP HTML OFF SPOOL OFF;
SET COLSEP ' ';

DROP TYPE FuploadFileWriter;
DROP TYPE FuploadDocumentRecords;
DROP TYPE FuploadDocumentRecord;
DROP TYPE FuploadDetailRecords;
DROP TYPE FuploadHeaderRecord;
DROP TYPE FuploadTrailerRecord;
DROP TYPE FuploadTextRecords;
DROP TYPE FuploadTextRecord;
DROP TYPE FuploadDetailRecord;
DROP TYPE FuploadBaseRecord;


-- PRE: If on personal Oracle instance:
-- CREATE OR REPLACE DIRECTORY NEW_EXTRACTS AS 'C:\temp';
-- GRANT READ ON DIRECTORY NEW_EXTRACTS TO PUBLIC;

-- Abstract base class for the 4 types of atomic FUPLOAD records.
-- Since we're making fixed-width records, we'll use char, not varchar2.
CREATE OR REPLACE TYPE FuploadBaseRecord AS OBJECT (
	-- This is the id of the non-Banner system loading finance document data into Banner via FUPLOAD.
	-- This id is defined via FTMSDAT and GJAPVAL.
	-- We probably should be using JEBTRS here instead of a generic id DATALOAD we use.
	system_id varchar2(8),

	-- The desired Banner finance document id code.
	-- This should be left blank to let Banner generate an id.
	-- Banner uses FOMFSEQ to generate the id.
	doc_code varchar2(8),

	-- The FUPLOAD record type.
	-- 1 => header record
	-- 2 => detail record
	-- 3 => trailer record
	-- 4 => text record
	rec_type varchar2(1),
	NOT FINAL MEMBER FUNCTION toString RETURN varchar2

) NOT FINAL NOT INSTANTIABLE;
/


-- FUPLOAD header record interface spec.  Inherits from the base record type.
CREATE OR REPLACE TYPE FuploadHeaderRecord UNDER FuploadBaseRecord (
	-- The transaction date in YYYYMMDD format.
	trans_date varchar2(8),

	-- An atomic FUPLOAD record has a fixed length of 148 bytes.
	-- This filler field aligns with that record boundary.
	-- It should contain all space characters (ASCII 32).
	filler char(123),
	CONSTRUCTOR FUNCTION FuploadHeaderRecord(trans_date varchar2) RETURN SELF AS RESULT,
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD header record implementation body.
CREATE OR REPLACE TYPE BODY FuploadHeaderRecord AS
	CONSTRUCTOR FUNCTION FuploadHeaderRecord(trans_date varchar2)
    RETURN SELF AS RESULT IS
    BEGIN
		self.system_id := 'DATALOAD';
		self.doc_code := '';
		self.rec_type := '1';
		self.trans_date := trans_date;
		self.filler := ' '; -- Yes, if you leave this null, it concats as nothing.
        RETURN;
    END;

	OVERRIDING MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(148) := '';
	BEGIN
		r := LPAD(NVL(self.system_id, ' '), 8);
		r := r || LPAD(NVL(self.doc_code, ' '), 8);
		r := r || NVL(self.rec_type, ' '); -- Length 1.
		r := r || LPAD(NVL(self.trans_date, ' '), 8);
		r := r || self.filler; -- char, not varchar2
		return r;
	END toString;
END;
/
show errors;


-- FUPLOAD trailer record interface spec.  Inherits from the base record type.
CREATE OR REPLACE TYPE FuploadTrailerRecord UNDER FuploadBaseRecord (
	-- Number of atomic records in the FUPLOAD finance document record.
	rec_count varchar2(8),

	-- The total of the absolute value of each atomic detail record amount.
	-- This is a value in cents (no decimal point).
	-- On output, it gets left-padded with 0s.
	trans_tot varchar2(12),

	-- An atomic FUPLOAD record has a fixed length of 148 bytes.
	-- This filler field aligns with that record boundary.
	-- It should contain all space characters (ASCII 32).
	filler char(111),
	CONSTRUCTOR FUNCTION FuploadTrailerRecord(rec_count varchar2, trans_tot varchar2) RETURN SELF AS RESULT,
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD trailer record implementation body.
CREATE OR REPLACE TYPE BODY FuploadTrailerRecord AS
	CONSTRUCTOR FUNCTION FuploadTrailerRecord(rec_count varchar2, trans_tot varchar2)
    RETURN SELF AS RESULT IS
    BEGIN
		self.system_id := 'DATALOAD';
		self.doc_code := '';
		self.rec_type := '3';
		self.rec_count := rec_count;
		self.trans_tot := trans_tot;
		self.filler := ' '; -- Yes, if you leave this null, it concats as nothing.
        RETURN;
    END;

	OVERRIDING MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(148) := '';
	BEGIN
		r := LPAD(NVL(self.system_id, ' '), 8);
		r := r || LPAD(NVL(self.doc_code, ' '), 8);
		r := r || NVL(self.rec_type, ' ');
		r := r || LPAD(NVL(self.rec_count, ' '), 8);
		r := r || LPAD(NVL(self.trans_tot, '0'), 12, '0');
		r := r || self.filler;
		return r;
	END toString;
END;
/
show errors;


-- FUPLOAD text record interface spec.  Inherits from the base record type.
CREATE OR REPLACE TYPE FuploadTextRecord UNDER FuploadBaseRecord (
	text varchar2(50), -- Arbitrary text describing the transaction.

	-- An atomic FUPLOAD record has a fixed length of 148 bytes.
	-- This filler field aligns with that record boundary.
	-- It should contain all space characters (ASCII 32).
	filler char(81),
	CONSTRUCTOR FUNCTION FuploadTextRecord(text varchar2) RETURN SELF AS RESULT,
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD text record implementation body.
CREATE OR REPLACE TYPE BODY FuploadTextRecord AS
	CONSTRUCTOR FUNCTION FuploadTextRecord(text varchar2)
	RETURN SELF AS RESULT IS
	BEGIN
		self.system_id := 'DATALOAD';
		self.doc_code := '';
		self.rec_type := '4';
		self.text := text;
		self.filler := ' ';
		return;
	END;

	OVERRIDING MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(148) := '';
	BEGIN
		r := LPAD(NVL(self.system_id, ' '), 8);
		r := r || LPAD(NVL(self.doc_code, ' '), 8);
		r := r || self.rec_type;
		r := r || LPAD(NVL(self.text, ' '), 50);
		r := r || self.filler;
		return r;
	END toString;
END;
/
show errors;


-- FUPLOAD detail record interface spec.  Inherits from the base record type.
CREATE OR REPLACE TYPE FuploadDetailRecord UNDER FuploadBaseRecord (
	-- Banner Finance rule class.
	-- This represents the type of financial operation/transaction being done.
	rucl_code varchar2(4),

	-- A finance document reference number.
	-- This is something you can use to link back to the transaction in the external system.
	-- We'll probably use a hash that maps to a <request id>.<line number> in JEBTRS.
	doc_ref_num varchar2(8),

	-- The absolute value of the transaction amount.
	-- This is a value in cents (no decimal point).
	-- On output, it gets left-padded with 0s.
	trans_amt varchar2(12),

	--  A description of the transaction.
	trans_desc varchar2(35),

	-- Debit/credit indicator.  Must be 'D', 'C', '+', or '-'.
	dr_cr_ind varchar2(1),

	-- WF => Wells Fargo.
	bank_code varchar2(2),

	-- C-FOAPAL
	-- Banner Finance chart of accounts code.
	coas_code varchar2(1),

	-- Banner Finance "account" index code.
	acci_code varchar2(6),

	-- Banner Finance fund code.
	fund_code varchar2(6),

	-- Banner Finance organization code.
	orgn_code varchar2(6),

	-- Bannr Finance account code.
	acct_code varchar2(6),

	-- Banner Finance program code.
	prog_code varchar2(6),

	-- Banner Finance activity code.
	actv_code varchar2(6),

	-- Banner Finance location code.
	locn_code varchar2(6),

	-- Encumbrances
	-- Encumbrance number.
	encd_num varchar2(8),

	-- Encumbrance commodity item number.
	encd_item_num varchar2(4),

	-- Encumbrance detail sequence number.
	encd_seq_num varchar2(4),

	-- Encumbrance action indication.
	-- T => total liquidation; P => partial liquidation; A => adjustment.
	encd_action_ind varchar2(1),

	-- Project code.
	prjd_code varchar2(8),

	-- Encumbrance type.
	-- R => requisition; P => purchase order; E => general encubrance; L => labor; M => memo.
	encb_type varchar2(1),

	CONSTRUCTOR FUNCTION FuploadDetailRecord(json varchar2, opi number, role number) RETURN SELF AS RESULT,
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD detail record implementation body.
-- TO DO: Handle other types of request operations.
CREATE OR REPLACE TYPE BODY FuploadDetailRecord AS
	-- Each request operation can yield more than one detail record.
	-- Thus, we pass in the desired role of the detail record we're generating relative to its
	-- source operation.
	--
	-- json: The JSON of the entire request.
	-- opi: The 1-based index of the request operation for which we are generating one (of perhaps many) detail records.
	-- role: The role of the detail record we're generating (relative to its source operation).
	CONSTRUCTOR FUNCTION FuploadDetailRecord(json varchar2, opi number, role number)
    RETURN SELF AS RESULT IS
		v_sequence number;
		v_type varchar2(128);
		v_opid varchar2(8); -- This identifies a particular line item of a JE request.
		v_index varchar2(6);
		v_fromAccount varchar2(6);
		v_toAccount varchar2(6);
		v_transactionId number; -- The surrogate id from FGBTRND.
		v_reason varchar2(128);
    BEGIN
		apex_json.parse(json);
		v_sequence := apex_json.get_number('operations[%d].sequence', opi);
		v_type := apex_json.get_varchar2('operations[%d].type', opi);
		v_opid := apex_json.get_varchar2('operations[%d].id', opi);
		v_index := apex_json.get_varchar2('operations[%d].index', opi);
		v_fromAccount := apex_json.get_varchar2('operations[%d].fromAccount', opi);
		v_toAccount := apex_json.get_varchar2('operations[%d].toAccount', opi);
		v_transactionId := apex_json.get_number('operations[%d].transactionId', opi);

		-- This would need to go into a text record.
		-- v_reason := apex_json.get_varchar2('operations[%d].reason', opi);

		self.system_id := 'DATALOAD';
		self.doc_code := ''; -- TO DO: Look this up based on surrogate id.
		self.rec_type := '2';
		self.rucl_code := 'JESY';
		self.doc_ref_num := v_opid;
		self.trans_amt := ''; -- TO DO: Convert to cents.
		self.trans_desc := ''; -- TO DO: Compose from other info.
		self.dr_cr_ind := ''; -- Depends on transaction role.
		self.bank_code := 'WF';
		self.coas_code := 'U';
		self.acci_code := v_index; -- For recategorization op, this stays the same.
		self.fund_code := '';
		self.orgn_code := '';
		self.acct_code := ''; -- Depends on transaction role.
		self.prog_code := '';
		self.actv_code := '';
		self.locn_code := '';
		self.encd_num := '';
		self.encd_item_num := '';
		self.encd_seq_num := '';
		self.encd_action_ind := '';
		self.prjd_code := '';
		self.encb_type := '';

		-- I can't tell how to do class constants in PL/SQL, so its magic numbers for now.
		if role = 0 then
			self.dr_cr_ind := '';
			self.acct_code := '';
		elsif role = 1 then
			self.dr_cr_ind := '';
			self.acct_code := '';
		else
			dbms_output.put_line('ERROR: Unknown detail record transaction role.');
		end if;

        RETURN;
    END;

	OVERRIDING MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(148) := '';
	BEGIN
		r := LPAD(NVL(self.system_id, ' '), 8);
		r := r || LPAD(NVL(self.doc_code, ' '), 8);
		r := r || NVL(self.rec_type, ' ');
		r := r || LPAD(NVL(self.rucl_code, ' '), 4);
		r := r || LPAD(NVL(self.doc_ref_num, ' '), 8);
		r := r || LPAD(NVL(self.trans_amt, '0'), 12, '0');
		r := r || LPAD(NVL(self.trans_desc, ' '), 35);
		r := r || NVL(self.dr_cr_ind, ' '); -- Length 1.
		r := r || LPAD(NVL(self.bank_code, ' '), 2);
		r := r || LPAD(NVL(self.coas_code, ' '), 1);
		r := r || LPAD(NVL(self.acci_code, ' '), 6);
		-- Oracle does empty strings WRONG!
		-- And Ellucian doesn't know how to write accurate data specs.
		r := r || LPAD(NVL(self.fund_code, ' '), 6);
		r := r || LPAD(NVL(self.orgn_code, ' '), 6);
		r := r || LPAD(NVL(self.acct_code, ' '), 6);
		r := r || LPAD(NVL(self.prog_code, ' '), 6);
		r := r || LPAD(NVL(self.actv_code, ' '), 6);
		r := r || LPAD(NVL(self.locn_code, ' '), 6);
		r := r || LPAD(NVL(self.encd_num, ' '), 8);
		r := r || LPAD(NVL(self.encd_item_num, ' '), 4);
		r := r || LPAD(NVL(self.encd_seq_num, ' '), 4);
		r := r || NVL(self.encd_action_ind, ' '); -- Length 1.
		r := r || LPAD(NVL(self.prjd_code, ' '), 8);
		r := r || NVL(self.encb_type, ' '); -- Length 1.

		return r;
	END toString;
END;
/
show errors;


-- This just acts as a list collection type.
CREATE OR REPLACE TYPE FuploadDetailRecords AS TABLE OF FuploadDetailRecord;
/

CREATE OR REPLACE TYPE FuploadTextRecords AS TABLE OF FuploadTextRecord;
/

-- FUPLOAD document record interface spec.
CREATE OR REPLACE TYPE FuploadDocumentRecord AS OBJECT (
	header FuploadHeaderRecord,
	details FuploadDetailRecords,
	trailer FuploadTrailerRecord,
	texts FuploadTextRecords,

	CONSTRUCTOR FUNCTION FuploadDocumentRecord(json varchar2) RETURN SELF AS RESULT,
	MEMBER FUNCTION toString RETURN varchar2

);
/
show errors;


CREATE OR REPLACE TYPE BODY FuploadDocumentRecord AS
	CONSTRUCTOR FUNCTION FuploadDocumentRecord(json varchar2)
    RETURN SELF AS RESULT IS
		v_count number;
		v_detail_record FuploadDetailRecord;
		v_value varchar2(256);
    BEGIN
		apex_json.parse(json);

		-- All the transactions implied by this request happen today even though they alter
		-- transactions that happened in the past.
		self.header := FuploadHeaderRecord(to_char(sysdate, 'YYYYMMDD'));

		-- Get number of elements in a array.  Loop over each op in the request.
		v_count := apex_json.get_count('operations');
		dbms_output.put_line('The request contains ' || v_count || ' operations.');
		for i in 1 .. v_count loop
			v_detail_record := FuploadDetailRecord(json, i, 0); -- invert existing transaction
			-- TO DO: Add to self.details.
			v_detail_record := FuploadDetailRecord(json, i, 1); -- new fixed transaciton
			-- TO DO: Add to self.details.
			v_value := apex_json.get_varchar2('operations[%d].type', i);
			dbms_output.put_line(v_value);
		end loop;

		-- self.trailer := FuploadTrailerRecord(json);
		-- self.texts = FuploadTextRecords(json);
        RETURN;
    END;


	MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(32767) := ''; -- This might need to be a CLOB.
	BEGIN
		-- The records are 148 byte fixed length.
		-- Thus, there are no newlines between them.
		if self.header is not null then
			r := self.header.toString();
		end if;

		if self.details is not null then
			FOR i IN 1 .. self.details.count() LOOP
				r := r || self.details(i).toString();
			END LOOP;
		end if;

		if self.trailer is not null then
			r := r || self.trailer.toString();
		end if;

		if self.texts is not null then
			FOR i IN 1 .. self.texts.count() LOOP
				r := r || self.texts(i).toString();
			END LOOP;
		end if;

		return r;
	END toString;
END;
/
show errors;


CREATE OR REPLACE TYPE FuploadDocumentRecords AS TABLE OF FuploadDocumentRecord;
/

-- FUPLOAD file writer class.
CREATE OR REPLACE TYPE FuploadFileWriter AS OBJECT (
	documents FuploadDocumentRecords,

	MEMBER FUNCTION getFileContents RETURN varchar2,
	MEMBER PROCEDURE write

);
/
show errors;

CREATE OR REPLACE TYPE BODY FuploadFileWriter AS
	MEMBER FUNCTION getFileContents RETURN varchar2 IS
		contents varchar2(32767) := ''; -- This might need to be a CLOB.
	BEGIN
		FOR i IN 1 .. self.documents.count() LOOP
			contents := contents || self.documents(i).toString();
		END LOOP;

		return contents;
	END getFileContents;

	MEMBER PROCEDURE write IS
		ofile UTL_FILE.FILE_TYPE;
		contents varchar2(32767) := ''; -- This might need to be a CLOB.
	BEGIN
		dbms_output.put_line('Writing file.');

		ofile := UTL_FILE.FOPEN('MY_DIR', 'fupload.dat.unprocessed', 'W');
		contents := self.getFileContents();
		UTL_FILE.PUT(ofile, contents);
		UTL_FILE.FCLOSE(ofile);
	END write;
END;
/
show errors;


-- Test using the FUPLOAD object types.
DECLARE
	hr1 FuploadHeaderRecord;
	tr1 FuploadTrailerRecord;
	txr1 FuploadTextRecord;
	dr1 FuploadDetailRecord;
	dr2 FuploadDetailRecord;

	docr0 FuploadDocumentRecord;
	docr1 FuploadDocumentRecord;
	fdoc varchar2(32767);

	writer FuploadFileWriter;
	file_contents varchar2(32767);
 	line varchar2(1024);
	value varchar2(128);
	ifile UTL_FILE.FILE_TYPE;
	ofile UTL_FILE.FILE_TYPE;

	r varchar2(148);
	er varchar2(148); -- Expected record.

	rd varchar2(1024);
	erd varchar2(1024);


BEGIN
	dbms_output.put_line('--------------------------------------------------------------------------------');
	dbms_output.put_line('Reading file.');

	-- ifile := UTL_FILE.FOPEN('MY_DIR', 'request.json', 'R');
	ifile := UTL_FILE.FOPEN('NEW_EXTRACTS', 'request.json', 'R');
	IF UTL_FILE.IS_OPEN(ifile) THEN
		LOOP
			BEGIN
				UTL_FILE.GET_LINE(ifile, line);
				-- Oracle strips off the EOL when reading in a line.
				-- Also, make sure you're using Unix line endings because it only strips off the \n,
				-- not the \r.
				file_contents := file_contents || line || CHR(10);
			EXCEPTION
				WHEN NO_DATA_FOUND THEN
					EXIT;
			END;
		END LOOP;
		UTL_FILE.FCLOSE(ifile);
	END IF;
	dbms_output.put_line(file_contents);
	dbms_output.put_line(length(file_contents));

	apex_json.parse(file_contents);

	value := apex_json.get_varchar2('requester');
    dbms_output.put_line(value);

	-- Reading the file seems to munge the whitespace a bit, but the JSON meaning is the same.
	dbms_output.put_line('Writing file.');
	-- WARNING: Oracle's default max_line_size is 1024.  Unless we increase it, an error is thrown.
	ofile := UTL_FILE.FOPEN('NEW_EXTRACTS', 'request.out.json', 'W', 32767);
	-- UTL_FILE.PUT(ofile, 'hello file');
	UTL_FILE.PUT(ofile, file_contents);
	UTL_FILE.FCLOSE(ofile);

	dbms_output.put_line('--------------------------------------------------------------------------------');
	docr0 := FuploadDocumentRecord(file_contents);
	fdoc := docr0.toString();
	dbms_output.put_line(fdoc);

	dbms_output.put_line('--------------------------------------------------------------------------------');

	return;


	dbms_output.put_line('Testing FUPLOAD object types.');

	dbms_output.put_line('--------------------------------------------------------------------------------');
	er := RPAD('DATALOAD        120190206', 148);
	hr1 := FuploadHeaderRecord('20190206');
	r := hr1.toString();

	-- dbms_output.put_line(REPLACE(r, ' ', '_'));
	-- dbms_output.put_line(LENGTH(r));

	if r = er then
		dbms_output.put_line('Test 1 passed.');
	else
		dbms_output.put_line('Test 1 failed.');
	end if;


	dbms_output.put_line(' ');
	dbms_output.put_line(' ');

	dbms_output.put_line('--------------------------------------------------------------------------------');
	er := RPAD('DATALOAD        3      10000000430286', 148);
	tr1 := FuploadTrailerRecord('10', '430286');
	r := tr1.toString();
	-- dbms_output.put_line(REPLACE(r, ' ', '_'));
	-- dbms_output.put_line(LENGTH(r));
	dbms_output.put_line(er);
	select dump(er) into erd from dual;
	dbms_output.put_line(erd);

	dbms_output.put_line(r);
	select dump(r) into rd from dual;
	dbms_output.put_line(rd);

	if r = er then
		dbms_output.put_line('Test 2 passed.');
	else
		dbms_output.put_line('Test 2 failed.');
	end if;

	dbms_output.put_line(' ');
	dbms_output.put_line(' ');

	dbms_output.put_line('--------------------------------------------------------------------------------');
	txr1 := FuploadTextRecord('This is a sample text record.');
	r := txr1.toString();
	dbms_output.put_line(REPLACE(r, ' ', '_'));
	dbms_output.put_line(LENGTH(r));

	dbms_output.put_line('--------------------------------------------------------------------------------');
	dr1 := FuploadDetailRecord(
		'DATALOAD', -- system_id
		'', -- doc_code
		'2', -- rec_type
		'JESY',-- rucl_code
		'JE12.10', -- doc_ref_num
		'12345', -- trans_amt
		'Sample transaction', -- trans_desc
		'C', -- dr_cr_ind
		'WF', -- bank_code
		'U', -- coas_code
		'660001', -- acci_code
		'FUND12', -- fund_code
		'ORGN34', -- orgn_code
		'ACCT56', -- acct_code
		'', -- prog_code
		'', -- actv_code
		'', -- locn_code
		'', -- encd_num
		'', -- encd_item_num
		'', -- encd_seq_num
		'', -- encd_action_ind
		'', -- prjd_code
		'' -- encb_type
	);
	r := dr1.toString();
	dbms_output.put_line(REPLACE(r, ' ', '_'));
	dbms_output.put_line(LENGTH(r));

	dbms_output.put_line(' ');
	dbms_output.put_line(' ');

	dbms_output.put_line('--------------------------------------------------------------------------------');
	er := 'DATALOAD        2JESY10002074000000001290            Move FZ031253 to 720556CWFU660001            720559                                            ';
	dr2 := FuploadDetailRecord(
		'DATALOAD', -- system_id
		'', -- doc_code
		'2', -- rec_type
		'JESY',-- rucl_code
		'10002074', -- doc_ref_num
		'1290', -- trans_amt
		'Move FZ031253 to 720556', -- trans_desc
		'C', -- dr_cr_ind
		'WF', -- bank_code
		'U', -- coas_code
		'660001', -- acci_code
		'', -- fund_code
		'', -- orgn_code
		'720559', -- acct_code
		'', -- prog_code
		'', -- actv_code
		'', -- locn_code
		'', -- encd_num
		'', -- encd_item_num
		'', -- encd_seq_num
		'', -- encd_action_ind
		'', -- prjd_code
		'' -- encb_type
	);
	r := dr2.toString();
	dbms_output.put_line(r);

	dbms_output.put_line(er);
	select dump(er) into erd from dual;
	dbms_output.put_line(erd);

	dbms_output.put_line(r);
	select dump(r) into rd from dual;
	dbms_output.put_line(rd);

	-- This fails even though the strings appear to be exactly the same.
	if r = er then
		dbms_output.put_line('Test 3 passed.');
	else
		dbms_output.put_line('Test 3 failed.');
	end if;

	dbms_output.put_line(' ');
	dbms_output.put_line(' ');

	dbms_output.put_line('--------------------------------------------------------------------------------');
	er := 'DATALOAD        2JESY10002074000000001290          Move FZ031253 from 720559DWFU660001            720556                                            ';
	dr2 := FuploadDetailRecord(
		'DATALOAD', -- system_id
		'', -- doc_code
		'2', -- rec_type
		'JESY',-- rucl_code
		'10002074', -- doc_ref_num
		'1290', -- trans_amt
		'Move FZ031253 from 720559', -- trans_desc
		'D', -- dr_cr_ind
		'WF', -- bank_code
		'U', -- coas_code
		'660001', -- acci_code
		'', -- fund_code
		'', -- orgn_code
		'720556', -- acct_code
		'', -- prog_code
		'', -- actv_code
		'', -- locn_code
		'', -- encd_num
		'', -- encd_item_num
		'', -- encd_seq_num
		'', -- encd_action_ind
		'', -- prjd_code
		'' -- encb_type
	);
	r := dr2.toString();
	dbms_output.put_line(r);

	dbms_output.put_line(er);
	select dump(er) into erd from dual;
	dbms_output.put_line(erd);

	dbms_output.put_line(r);
	select dump(r) into rd from dual;
	dbms_output.put_line(rd);

	-- This fails even though the strings appear to be exactly the same.
	if r = er then
		dbms_output.put_line('Test 4 passed.');
	else
		dbms_output.put_line('Test 4 failed.');
	end if;
	dbms_output.put_line(' ');
	dbms_output.put_line(' ');

	dbms_output.put_line('--------------------------------------------------------------------------------');
	docr1 := FuploadDocumentRecord(
		hr1,
		FuploadDetailRecords(dr1, dr2),
		tr1,
		FuploadTextRecords(txr1)
	);
	fdoc := docr1.toString();
	dbms_output.put_line(fdoc);

	-- Oh God, just to add another layer of horrors, sqlplus tries to be "helpful" by trimming
	-- whitespace from your output.
	dbms_output.put_line(REPLACE(fdoc, ' ', '_'));
	dbms_output.put_line(LENGTH(fdoc));

	-- TO DO: Construct a document record without any optional text records.

	dbms_output.put_line('--------------------------------------------------------------------------------');
	writer := FuploadFileWriter(FuploadDocumentRecords(docr1));
	file_contents := writer.getFileContents();
	dbms_output.put_line(file_contents);
	writer.write();
	dbms_output.put_line(' ');
	dbms_output.put_line(' ');

END;
/



