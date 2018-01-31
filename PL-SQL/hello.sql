-- If I run this in SQL*Plus, it should print to the console.
-- Once you have installed your Oracle client and put a tnsnames.ora there, you can connect to your
-- database with SQL*Plus, Toad, or whatever client front end.
-- The tnsnames.ora defines whatever connections you can make to the database (I think).
-- The sqlplus program and tnsnames.ora live in the dir tree of the Oracle client you installed.
-- The Windows-installed sqlplus does seem to run okay from Cygwin.
--
-- Schemas are usernames is Oracle.  So, to log in, you use username <schema>@<database instance>.
-- You might be running various database instances like PROD (production) and QA (test).
--
-- Once you log in with SQL*Plus, you run this external SQL file like so:
-- @hello.sql
-- Yup, it worked!

-- Nothing will print unless you set SERVEROUTPUT.  Unnecessary complexity right out of the box.
SET SERVEROUTPUT ON SIZE 1000000
-- Instead of simple characters or no characters (like Python), we get named block delimiters.
-- These are horrible in Bash and horrible here.
BEGIN
	dbms_output.put_line('Hello, PL/SQL!');
END;
/
-- The / actually causes the block above it to execute.  Weird.

-- My initial impressions: PL/SQL is a monstrosity.

