SET SERVEROUTPUT ON SIZE 1000000

DECLARE
	truth BOOLEAN := TRUE;
	lies BOOLEAN := FALSE;
BEGIN
	IF lies THEN
		dbms_ouput.put_line('Dirty lies.');
	ELSIF NOT truth THEN
		dbms_output.put_line('There is no truth.');
	ELSE truth OR lies
		-- Note that we use '' for a literal ' here.
		dbms_output.put_line('It''s complicated.');
	END IF;
END;
/


