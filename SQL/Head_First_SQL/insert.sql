-- Insert some rows into gregs_list.my_contacts.

USE gregs_list;

DELETE FROM my_contacts; -- Get rid of existing records.

INSERT INTO my_contacts (last_name, first_name, email, gender, birthday, profession, location, status, interests, seeking)
	VALUES ('Henderson', 'Jim', 'jimbob@aol.com', 'M', '1977-07-07', 'plumber', 'Iowa', 'alive', 'stuff', 'things to make him go');

INSERT INTO my_contacts (last_name, first_name, email, gender, birthday, profession, location, status, interests, seeking)
	VALUES ('Van Winkle', 'Rip', 'asleep@thewheel.org', 'M', '1023-04-05', 'sleeper', 'Europe', 'asleep', 'pillows', 'comfortable bed');

-- Partial insert.  Unlisted columns will get their default values.
INSERT INTO my_contacts (first_name, email, location, profession)
	VALUES ('Patty', 'patty@postoffice.gov', 'Washington, DC', 'mail carrier');



