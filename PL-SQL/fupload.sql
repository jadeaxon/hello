SET SERVEROUTPUT ON SIZE 1000000

/*
CREATE OR REPLACE TYPE FuploadDocumentRecord AS OBJECT (

);
/
*/

DROP TYPE FuploadHeaderRecord;
DROP TYPE FuploadTrailerRecord;


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


-- Show specific compilation errors, if any.
show errors;


-- Test using the FUPLOAD object types.
DECLARE
	hr1 FuploadHeaderRecord;
	tr1 FuploadTrailerRecord;
	txr1 FuploadTextRecord;
	r varchar2(148);

BEGIN
	dbms_output.put_line('Testing FUPLOAD object types.');

	hr1 := FuploadHeaderRecord('DATALOAD', '', '1', '20190216', '');
	r := hr1.toString();
	dbms_output.put_line(REPLACE(r, ' ', '_'));
	dbms_output.put_line(LENGTH(r));

	tr1 := FuploadTrailerRecord('DATALOAD', '', '2', '20190216', '3', '123.45');
	r := tr1.toString();
	dbms_output.put_line(REPLACE(r, ' ', '_'));
	dbms_output.put_line(LENGTH(r));

	txr1 := FuploadTextRecord('DATALOAD', '', '3', '20190216', 'This is a sample transaction.');
	r := txr1.toString();
	dbms_output.put_line(REPLACE(r, ' ', '_'));
	dbms_output.put_line(LENGTH(r));


END;
/



