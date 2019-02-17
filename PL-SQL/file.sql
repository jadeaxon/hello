-- PRE: Grant permission to use SYS.UTL_FILE.
-- sqlplus / as sysdba
-- GRANT EXECUTE ON SYS.UTL_FILE TO <user running this script>;
SET SERVEROUTPUT ON SIZE 1000000;

-- Make Oracle able to see a file system directory.
-- This makes an entry in the DBA_DIRECTORIES table (?) that is visible in the ALL_DIRECTORIES view.
-- This allows Oracle to control who can access this directory.
CREATE OR REPLACE DIRECTORY MY_DIR AS 'C:\temp';

-- Yes, you just need read access to the directory to write files to it.
-- Read access makes the directory visible for you to use.
GRANT READ ON DIRECTORY MY_DIR TO PUBLIC;

DECLARE
	ofile UTL_FILE.FILE_TYPE; -- Declare a file variable for writing file.
	ifile UTL_FILE.FILE_TYPE; -- File var for reading file.
	mydir varchar2(256); -- Directory path.
	line varchar2(256); -- Line buffer.

BEGIN
	dbms_output.put_line('Writing myfile.txt in Oracle directory MY_DIR.');
	select directory_path into mydir from all_directories where upper(directory_name) = 'MY_DIR';
	dbms_output.put_line('MY_DIR: ' || mydir);

	-- Open file for writing.
	ofile := UTL_FILE.FOPEN('MY_DIR', 'myfile.txt', 'W');

	-- Write a line to the file and then close it (to flush buffers to disk).
	UTL_FILE.PUT_LINE(ofile, 'Hello, file!');
	UTL_FILE.FCLOSE(ofile);

	-- Open file for reading.
	dbms_output.put_line('Reading myfile.txt in Oracle directory MY_DIR.');
	ifile := UTL_FILE.FOPEN('MY_DIR', 'myfile.txt', 'R');
	IF UTL_FILE.IS_OPEN(ifile) THEN
		LOOP
			BEGIN
				UTL_FILE.GET_LINE(ifile, line);
				dbms_output.put_line(line);
			EXCEPTION WHEN No_Data_Found THEN
				EXIT;
			END;
		END LOOP;
	ELSE
		-- If the file DNE, Oracle will actually throw an "invalid file operation" error.
		dbms_output.put_line('ERROR: Failed to open myfile.txt for reading.');
	END IF;
END;
/


