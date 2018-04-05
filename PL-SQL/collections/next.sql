-- Demonstrate the NEXT function of the Oracle Collections API.

-- Nothing will print unless you set SERVEROUTPUT.
SET SERVEROUTPUT ON SIZE 1000000

DECLARE
	-- This is an associative array that maps country codes to English country names.
	TYPE CountryMap IS TABLE OF VARCHAR2(40 CHAR) INDEX BY VARCHAR2(3 CHAR);
	country_map CountryMap;

	c VARCHAR2(3 CHAR); -- Current index.

BEGIN
	-- Do we need to use EXTEND before assigning these?  No.
	country_map('USA') := 'United States of America';
	country_map('CAN') := 'Canada';
	country_map('FRA') := 'France';

	-- Loop over the associate array (aka map).
	c := country_map.FIRST; -- Set current index to index of first element.
	dbms_output.put_line('Initial c: ' || c );
	-- Do not use c <> NULL.  Direct comparisons to NULL don't work.
	WHILE c IS NOT NULL LOOP
		dbms_output.put_line(country_map(c));
		c := country_map.NEXT(c); -- Next index.
	END LOOP;
END;
/





