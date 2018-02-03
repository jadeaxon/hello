-- This only has to be set once per session.
SET SERVEROUTPUT ON SIZE 1000000;

-- Here we have the declaration section of an anonymous block.
DECLARE
	truth BOOLEAN := TRUE;
	lies BOOLEAN := FALSE;
BEGIN
	IF lies THEN
		dbms_output.put_line('Dirty lies.');
	ELSIF (NOT truth) THEN
		dbms_output.put_line('There is no truth.');
	ELSE
		-- Note that we use '' for a literal ' here.
		dbms_output.put_line('It''s complicated.');
	END IF;
END;
/


