SET SERVEROUTPUT ON SIZE 1000000

/*
CREATE OR REPLACE TYPE FuploadDocumentRecord AS OBJECT (

);
/
*/

DROP TYPE FuploadHeaderRecord;
DROP TYPE FuploadTrailerRecord;
DROP TYPE FuploadTextRecord;
DROP TYPE FuploadDetailRecord;
DROP TYPE FuploadBaseRecord;


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

	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD detail record implementation body.
CREATE OR REPLACE TYPE BODY FuploadDetailRecord AS
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


-- Test using the FUPLOAD object types.
DECLARE
	hr1 FuploadHeaderRecord;
	tr1 FuploadTrailerRecord;
	txr1 FuploadTextRecord;
	dr1 FuploadDetailRecord;
	dr2 FuploadDetailRecord;

	r varchar2(148);
	er varchar2(148); -- Expected record.

	rd varchar(1024);
	erd varchar2(1024);


BEGIN
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


	dbms_output.put_line(chr(10));
	dbms_output.put_line(chr(10));

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

	dbms_output.put_line(chr(10));
	dbms_output.put_line(chr(10));

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

	dbms_output.put_line(chr(10));
	dbms_output.put_line(chr(10));

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

	dbms_output.put_line(chr(10));
	dbms_output.put_line(chr(10));

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

END;
/



