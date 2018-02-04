SET SERVEROUTPUT ON SIZE 1000000

DECLARE
	i NUMBER := 0;
BEGIN
	WHILE i < 7 LOOP
		i := i + 1;
		dbms_output.put_line(i);
	END LOOP;
END;
/

