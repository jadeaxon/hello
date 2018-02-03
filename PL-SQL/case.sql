SET SERVEROUTPUT ON SIZE 1000000

BEGIN
	-- The result of each case expression is compared to the value of the selector expression.
	-- If the two values are equal, the case logic executes.
	-- There is no fall through as in C, Java, etc.  It acts just like an if/else if/else.
	CASE TRUE
		WHEN 2 = 1 THEN -- First case expression.
			dbms_output.put_line('Two equals one.');
		WHEN 3 = 1 THEN
			NULL;
		WHEN 1 = 1 THEN
			dbms_output.put_line('One equals one.');
		ELSE
			NULL;
	END CASE;

	CASE 5 + 4 + 1 -- Note that the selector can also be an expression.
		WHEN 7 THEN
			dbms_output.put_line('The result is 7.');
		WHEN 10 THEN
			dbms_output.put_line('The result is 10.');
		ELSE
			NULL;
	END CASE;
END;
/


