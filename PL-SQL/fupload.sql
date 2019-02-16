SET SERVEROUTPUT ON SIZE 1000000

/*
CREATE OR REPLACE TYPE FuploadDocumentRecord AS OBJECT (

);
/
*/

DROP TYPE FuploadHeaderRecord;
DROP TYPE FuploadTrailerRecord;
DROP TYPE FuploadText Record;
DROP TYPE FuploadDetailRecord;


-- Abstract base class for the 4 types of atomic FUPLOAD records.
-- Since we're making fixed-width records, we'll use char, not varchar2.
CREATE OR REPLACE TYPE FuploadBaseRecord AS OBJECT (
	-- This is the id of the non-Banner system loading finance document data into Banner via FUPLOAD.
	-- This id is defined via FTMSDAT and GJAPVAL.
	-- We probably should be using JEBTRS here instead of a generic id DATALOAD we use.
	system_id char(8),

	-- The desired Banner finance document id code.
	-- This should be left blank to let Banner generate an id.
	-- Banner uses FOMFSEQ to generate the id.
	doc_code char(8),

	-- The FUPLOAD record type.
	-- 1 => header record
	-- 2 => detail record
	-- 3 => trailer record
	-- 4 => text record
	rec_type char(1),

	NOT FINAL MEMBER FUNCTION toString RETURN varchar2
) NOT FINAL NOT INSTANTIABLE;
/


-- FUPLOAD header record interface spec.  Inherits from the base record type.
CREATE OR REPLACE TYPE FuploadHeaderRecord UNDER FuploadBaseRecord (
	-- The transaction date in YYYYMMDD format.
	trans_date char(8),

	-- An atomic FUPLOAD record has a fixed length of 148 bytes.
	-- This filler field aligns with that record boundary.
	-- It should contain all space characters (ASCII 32).
	filler char(123),
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD header record implementation body.
CREATE OR REPLACE TYPE BODY FuploadHeaderRecord AS
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(148) := '';
	BEGIN
		r := self.system_id;
		r := r || self.doc_code;
		r := r || self.rec_type;
		r := r || self.trans_date;
		r := r || self.filler;
		return r;
	END toString;
END;
/


-- FUPLOAD trailer record interface spec.  Inherits from the base record type.
CREATE OR REPLACE TYPE FuploadTrailerRecord UNDER FuploadBaseRecord (
	rec_count char(8), -- Number of atomic records in the FUPLOAD finance document record.
	trans_tot char(12), -- The total of the absolute value of each atomic detail record amount.

	-- An atomic FUPLOAD record has a fixed length of 148 bytes.
	-- This filler field aligns with that record boundary.
	-- It should contain all space characters (ASCII 32).
	filler char(111),
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD trailer record implementation body.
CREATE OR REPLACE TYPE BODY FuploadTrailerRecord AS
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(148) := '';
	BEGIN
		r := self.system_id;
		r := r || self.doc_code;
		r := r || self.rec_type;
		r := r || self.rec_count;
		r := r || self.trans_tot;
		r := r || self.filler;
		return r;
	END toString;
END;
/


-- FUPLOAD text record interface spec.  Inherits from the base record type.
CREATE OR REPLACE TYPE FuploadTextRecord UNDER FuploadBaseRecord (
	text char(50), -- Arbitrary text describing the transaction.

	-- An atomic FUPLOAD record has a fixed length of 148 bytes.
	-- This filler field aligns with that record boundary.
	-- It should contain all space characters (ASCII 32).
	filler char(81),
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD text record implementation body.
CREATE OR REPLACE TYPE BODY FuploadTextRecord AS
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(148) := '';
	BEGIN
		r := self.system_id;
		r := r || self.doc_code;
		r := r || self.rec_type;
		r := r || self.text;
		r := r || self.filler;
		return r;
	END toString;
END;
/



-- FUPLOAD detail record interface spec.  Inherits from the base record type.
CREATE OR REPLACE TYPE FuploadDetailRecord UNDER FuploadBaseRecord (
	-- Banner Finance rule class.
	-- This represents the type of financial operation/transaction being done.
	rucl_code char(4),

	-- A finance document reference number.
	-- This is something you can use to link back to the transaction in the external system.
	-- We'll probably use a hash that maps to a <request id>.<line number> in JEBTRS.
	doc_ref_num char(8),

	-- The absolute value of the transaction amount.
	trans_amt char(12),

	--  A description of the transaction.
	trans_desc char(35),

	-- Debit/credit indicator.  Must be 'D', 'C', '+', or '-'.
	dr_cr_ind char(1),

	-- WF => Wells Fargo.
	bank_code char(2),

	-- C-FOAPAL
	-- Banner Finance chart of accounts code.
	coas_code char(1),

	-- Banner Finance "account" index code.
	acci_code char(6),

	-- Banner Finance fund code.
	fund_code char(6),

	-- Banner Finance organization code.
	orgn_code char(6),

	-- Bannr Finance account code.
	acct_code char(6),

	-- Banner Finance program code.
	prog_code char(6),

	-- Banner Finance activity code.
	actv_code char(6),

	-- Banner Finance location code.
	locn_code char(6),

	-- Encumbrances
	-- Encumbrance number.
	encd_num char(8),

	-- Encumbrance commodity item number.
	encd_item_num char(4),

	-- Encumbrance detail sequence number.
	encd_seq_num char(4),

	-- Encumbrance action indication.
	-- T => total liquidation; P => partial liquidation; A => adjustment.
	encd_action_ind char(1),

	-- Project code.
	prjd_code char(8),

	-- Encumbrance type.
	-- R => requisition; P => purchase order; E => general encubrance; L => labor; M => memo.
	encb_type char(1),

	OVERRIDING MEMBER FUNCTION toString RETURN varchar2
);
/


-- FUPLOAD detail record implementation body.
CREATE OR REPLACE TYPE BODY FuploadDetailRecord AS
	OVERRIDING MEMBER FUNCTION toString RETURN varchar2 IS
		r varchar2(148) := '';
	BEGIN
		r := self.system_id;
		r := r || self.doc_code;
		r := r || self.rec_type;
		r := r || self.rucl_code;
		r := r || self.doc_ref_num;
		r := r || self.trans_amt;
		r := r || self.trans_desc;
		r := r || self.dr_cr_ind;
		r := r || bank_code;
		r := r || coas_code;
		r := r || acci_code;
		r := r || fund_code;
		r := r || orgn_code;
		r := r || acct_code;
		r := r || prog_code;
		r := r || actv_code;
		r := r || locn_code;
		r := r || encd_num;
		r := r || encd_item_num;
		r := r || encd_seq_num;
		r := r || encd_action_ind;
		r := r || prjd_code;
		r := r || encb_type;

		return r;
	END toString;
END;
/


-- Show specific compilation errors, if any.
show errors;


-- Test using the FUPLOAD object types.
DECLARE
	hr1 FuploadHeaderRecord;
	tr1 FuploadTrailerRecord;
	txr1 FuploadTextRecord;
	dr1 FuploadDetailRecord;
	r varchar2(148);

BEGIN
	dbms_output.put_line('Testing FUPLOAD object types.');

	hr1 := FuploadHeaderRecord('DATALOAD', '', '1', '20190216', '');
	r := hr1.toString();
	dbms_output.put_line(REPLACE(r, ' ', '_'));
	dbms_output.put_line(LENGTH(r));

	tr1 := FuploadTrailerRecord('DATALOAD', '', '3', '20190216', '20', '123.45');
	r := tr1.toString();
	dbms_output.put_line(REPLACE(r, ' ', '_'));
	dbms_output.put_line(LENGTH(r));

	txr1 := FuploadTextRecord('DATALOAD', '', '4', '20190216', 'This is a sample transaction.');
	r := txr1.toString();
	dbms_output.put_line(REPLACE(r, ' ', '_'));
	dbms_output.put_line(LENGTH(r));

	dr1 := FuploadDetailRecord(
		'DATALOAD', -- self.system_id
		'', -- self.doc_code
		'2', -- self.rec_type
		'JE16',-- self.rucl_code
		'JE12.10', -- self.doc_ref_num
		'123.45', -- self.trans_amt
		'Sample transaction', -- self.trans_desc
		'+', -- self.dr_cr_ind
		'WF', -- bank_code
		'U', -- coas_code
		'660001', -- acci_code
		'', -- fund_code
		'', -- orgn_code
		'', -- acct_code
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

END;
/



