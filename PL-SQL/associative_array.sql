-- Loop over an associative array.

-- This only has to be set once per session.
SET SERVEROUTPUT ON SIZE 1000000;

DECLARE
	-- Declare an associative array.
	-- This is not realistic because some zip codes start with 0.
	TYPE Zip2StateMap IS TABLE OF VARCHAR(2) INDEX BY PLS_INTEGER;

	-- Associative arrays do not have a constructor, so just declare.
	myaarray Zip2StateMap;
	key PLS_INTEGER;
BEGIN
	-- Init the associative array.
	myaarray(84601) := 'UT';
	myaarray(92008) := 'CA';

	key := myaarray.first;
	while (key is not null) loop
		dbms_output.put_line(myaarray(key));
		key := myaarray.next(key);
	end loop;

	-- Trying to access an undefined entry raises an exception.  You have to use exists().
	if not myaarray.exists(90210) then
		dbms_output.put_line('No entry exists for 90210');
	end if;

END;
/

