-- PRE: Connected to Oracle 11gR2 XE.

CONNECT hf; -- This is the db name Head First SQL used.
ALTER SESSION SET CURRENT_SCHEMA = hf;

-- A table representing contact info for various people.
-- Drop table only if it does not exist.
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE my_contacts';
EXCEPTION
   WHEN OTHERS THEN
      IF SQLCODE != -942 THEN
         RAISE;
      END IF;
END;

CREATE TABLE my_contacts (
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(50),
	gender CHAR(1),
	birthday DATE,
	profession VARCHAR(50),
	location VARCHAR(50),
	status VARCHAR(20),
	interests VARCHAR(100),
	seeking VARCHAR(100)
);

COMMIT;
DESC my_contacts;
