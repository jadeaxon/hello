-- PRE: MySQL database connected to in MySQL Shell.

-- In MySQL Shell:
-- \source C:\Users\jadeaxon\projects\hello\SQL\create_table.sql

USE gregs_list; -- This is the db name Head First SQL used.

-- A table representing contact info for various people.
DROP TABLE my_contacts;
CREATE TABLE my_contacts (
	first_name VARCHAR(20),
	last_name VARCHAR(30),
	email VARCHAR(50),
	gender CHAR(1),
	birthday DATE,
	profession VARCHAR(50),
	location VARCHAR(50),
	status VARCHAR(20),
	interests VARCHAR(100),
	seeking VARCHAR(100)
);

DESC my_contacts;


