-- Here we use an implicit cursor.

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

