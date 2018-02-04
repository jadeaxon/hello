SET SERVEROUTPUT ON SIZE 1000000

-- Loop over a range of numbers.
-- Ranges in PL/SQL are inclusive (unlike in Python).
BEGIN
	FOR i IN 1 .. 10 LOOP
		dbms_output.put_line(i);
	END LOOP;
END;
/


