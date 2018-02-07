SET SERVEROUTPUT ON SIZE 1000000

DECLARE
	counter NUMBER := 0;
BEGIN
	-- Count from 0 to 5.
	LOOP
		dbms_output.put_line(counter);
		IF counter >= 5 THEN
			EXIT;
		END IF;
		counter := counter + 1;
	END LOOP;
	-- dbms_output.put_line(''); -- This does not work!
	-- dbms_output.new_line; -- Nor does this!
	dbms_output.put(chr(10)); -- This works.

	-- Print all odd numbers from 0 to 10.
	counter := 0;
	LOOP
		counter := counter + 1;
		CONTINUE WHEN MOD(counter, 2) = 0; -- Skip even numbers.
		EXIT WHEN counter >= 10;
		dbms_output.put_line(counter);
	END LOOP;
END;
/

