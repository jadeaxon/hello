SET SERVEROUTPUT ON SIZE 1000000

BEGIN
	-- Loop over a range of numbers.
	-- Ranges in PL/SQL are inclusive (unlike in Python).
	FOR i IN 1 .. 10 LOOP
		dbms_output.put_line(i);
	END LOOP;
	dbms_output.put(chr(10));

	-- Loop using a cursor.
	-- Dual is a weird pseudo table that has one column named dummy.
	-- It has one row containing the value 'X'.
	FOR c IN (select * from dual) LOOP
		dbms_output.put_line(c.dummy);
	END LOOP;
END;
/



