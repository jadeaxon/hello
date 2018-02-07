-- Loop over a nested table of numbers.

-- This only has to be set once per session.
SET SERVEROUTPUT ON SIZE 1000000;

DECLARE
	-- Declare the nested table type.
	-- A nested table is essentially an array that isn't fixed in size.
	TYPE NumberTable IS TABLE OF NUMBER;
	-- Init the nested table by calling its constructor.
	mytable NumberTable := NumberTable(1, 2, 3);
BEGIN
	-- Arrays use limit(); nested tables use count().
	FOR i IN 1 .. mytable.count() LOOP
		dbms_output.put_line(mytable(i));
	END LOOP;
END;
/

