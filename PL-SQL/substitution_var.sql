-- Use a substitution varible.

-- I think these are essentially command-line args.
-- No, actually using them interactively prompts user for input when you run this code.
-- Beyond that, it looks like the substitution happens precompilation.
-- So these are like prompts for preprocessor defines.  Seems like a recipe for disaster.
DECLARE
	-- You declare variables in this section.
	-- PL/SQL is based on ADA, so it tries to be all formal like this.
	-- Looks like variables can have the same data types as database columns.
	-- Note that the type comes after the name.
	my_var VARCHAR2(30);
BEGIN
	-- This is the execution section of the block.
	-- Note that PL/SQL uses single quotes.
	-- There's also a special quoting mechanism using q that is similar to Perl's arbitrary quote
	-- char mechanism.
	my_var := '&input'; -- This is our substitution variable.
	-- A substitution variable should never be assigned to anything in the DECLARE section.
	-- || is the string concatenation operator.
	dbms_output.put_line('Hello, ' || my_var || '!');
END;
/

