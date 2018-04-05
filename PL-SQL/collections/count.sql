-- Demonstrate the COUNT function of the Oracle Collections API.

-- Nothing will print unless you set SERVEROUTPUT.
SET SERVEROUTPUT ON SIZE 1000000

DECLARE
	-- This is a nested table.  It is more like a list.
	-- Holds just one type of value.  Has just one column.
	-- Why it is called a "table" makes no sense to me.
	-- Maybe it is implemented as an Oracle table under the hood.
	TYPE number_table IS TABLE OF INTEGER;

	-- Create a variable of the nested table type we just declared.
	-- The initializer function has the same name as the type.
	number_list NUMBER_TABLE := number_table(1, 2, 3, 4, 5);

BEGIN
	-- The COUNT function returns the number of elements in a collection.
	-- Note that in PL/SQL, functions calls using no args often omit the parenthesis.
	dbms_output.put_line('The nested table list thing has '||number_list.COUNT||' elements.');
	dbms_output.put_line('You can use the parentheses: '||number_list.COUNT()||'.');
END;
/




