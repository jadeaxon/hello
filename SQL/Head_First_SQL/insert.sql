-- Insert some rows into hf.my_contacts.

-- PRE: You are connected as hf.
-- CONNECT hf;
-- ALTER SESSION SET CURRENT_SCHEMA = hf;

DELETE FROM my_contacts; -- Get rid of existing records.

-- Notice the ANSI date literals.
INSERT INTO my_contacts (last_name, first_name, email, gender, birthday, profession, location, status, interests, seeking)
	VALUES ('Henderson', 'Jim', 'jimbob@aol.com', 'M', DATE '1977-07-07', 'plumber', 'Iowa', 'alive', 'stuff', 'things to make him go');

INSERT INTO my_contacts (last_name, first_name, email, gender, birthday, profession, location, status, interests, seeking)
	VALUES ('Van Winkle', 'Rip', 'asleep@thewheel.org', 'M', DATE '1023-04-05', 'sleeper', 'Europe', 'asleep', 'pillows', 'comfortable bed');

-- Partial insert.  Unlisted columns will get their default values.
INSERT INTO my_contacts (last_name, first_name, email, location, profession)
	VALUES ('Turner', 'Patty', 'patty@postoffice.gov', 'Washington, DC', 'mail carrier');

COMMIT;


