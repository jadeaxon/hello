SET SERVEROUTPUT ON SIZE 1000000

DECLARE
	counter NUMBER := 0;
BEGIN
	LOOP
		dbms_output.put_line(counter);
		IF counter >= 10 THEN
			EXIT;
		END IF;
		counter := counter + 1;
	END LOOP;
END;
/

