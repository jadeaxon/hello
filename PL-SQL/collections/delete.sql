-- Demonstrate the FIRST, LAST, EXISTS, and DELETE functions of the Oracle Collections API.

-- Nothing will print unless you set SERVEROUTPUT.
SET SERVEROUTPUT ON SIZE 1000000

DECLARE
	-- This is a nested table.  It is more like a list.
	-- Holds just one type of value.  Has just one column.
	-- Why it is called a "table" makes no sense to me.
	-- Maybe it is implemented as an Oracle table under the hood.
	TYPE number_table IS TABLE OF INTEGER;

	-- Create a variable of the nested table type we just declared.
	number_list NUMBER_TABLE; -- Not initialized.

	-- Declare a local procedure.
	PROCEDURE print_list(list_in NUMBER_TABLE) IS
	BEGIN
		dbms_output.put_line('-----------------------------------');
		FOR i IN list_in.FIRST .. list_in.LAST LOOP
			IF list_in.EXISTS(i) THEN
				dbms_output.put_line(list_in(i) || ' exists.');
			END IF;
		END LOOP;
	END print_list;

BEGIN
	-- Since we didn't init number_list above, it's first element will not exist.
	-- Remember, PL/SQL collections use 1-based indexes.
	IF NOT number_list.EXISTS(1) THEN
		number_list := NUMBER_TABLE(1, 2, 3, 4, 5);
	END IF;

	dbms_output.put_line('Nested table before element deletion:');
	print_list(number_list);

	-- Delete elements 2-4 inclusive.
	number_list.DELETE(2, 4);

	dbms_output.put_line(chr(10)); -- ASCII 10 newline.
	dbms_output.put_line('Nested table after element deletion:');
	-- Notice that the .FIRST .. .LAST loop goes over the whole range.
	-- It does not know for which indexes in that range elements exist or not.
	-- That is, the loop is not actually iterating over the list itself.
	print_list(number_list);

END;
/




