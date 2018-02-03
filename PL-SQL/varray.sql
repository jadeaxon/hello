-- Loop over an array of strings.

-- This only has to be set once per session.
SET SERVEROUTPUT ON SIZE 1000000;

DECLARE
	-- Declare the array type.
	TYPE VA_STRING IS VARRAY(3) OF VARCHAR2(80);
	-- Init the array by calling its constructor.
	myarray VA_STRING := VA_STRING('fee', 'fie', 'foe');
BEGIN
	FOR i IN 1 .. myarray.limit LOOP
		-- Yes, arrays use () instead of [].
		dbms_output.put_line(myarray(i));
	END LOOP;
END;
/

