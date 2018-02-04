-- Here we use an implicit cursor.
-- You need to run this one as plsql@localhost.
-- PRE: Run setup/00_create_user.sql.
-- PRE: Run setup/01_create_store.sql.

-- The example database from Oracle 11g PL/SQL Programming is for a book, CD, video game store.

SET SERVEROUTPUT ON SIZE 1000000

DECLARE
	n NUMBER := 0;
BEGIN
	-- This is a weird way of assigning 1 to n.
	-- Any select statement is really an implicit cursor.
	-- We're again using the weird pseudotable "dual".
	SELECT 1 INTO n FROM dual;

	-- The SQL keyword represents the last used implicit cursor.
	-- %ROWCOUNT is an attribute of a cursor.  It stores # of rows selected/affected.
	dbms_output.put_line('The cursor''s SQL statement selected ' || SQL%ROWCOUNT || ' rows.');
END;
/

DECLARE
	-- We use whatever the data types of the columns are by using %TYPE.
	id item.item_id%TYPE;
	title item.item_title%TYPE;
	subtitle item.item_subtitle%TYPE;
BEGIN
	-- Select a single row.
	SELECT item_id, item_title, item_subtitle INTO id, title, subtitle FROM item WHERE ROWNUM < 2;
	dbms_output.put_line('Selected "' || title || '".');
END;
/


