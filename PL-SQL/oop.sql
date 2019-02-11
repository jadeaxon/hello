SET SERVEROUTPUT ON SIZE 1000000

-- Object types (classes) are defined at the database level.
-- You cannot define them within a package.

-- Person class interface.
-- NOT FINAL => the class or method can be inherited from or overriden.
-- By default, all object types are final.
CREATE OR REPLACE TYPE Person AS OBJECT (
	name varchar2(20),
	NOT FINAL MEMBER PROCEDURE display
) NOT FINAL;
/

-- Person class implementation.
CREATE OR REPLACE TYPE BODY Person AS
	MEMBER PROCEDURE display IS
	BEGIN
		-- Instead of 'this', PL/SQL uses 'self'.
		-- You don't have to explicitly use 'self', but it can be clearer to do so.
		-- Member access is via the . operator (like in most languages).
		dbms_output.put_line('I am a person named ' || self.name || '.');
	END display;
END;
/

-- Employee class interface.
-- Create Employee as a subclass of Person (under it) in the class hierarchy.
CREATE OR REPLACE TYPE Employee UNDER Person (
	salary number,
	-- Override a non-final instance method of the base class.
	OVERRIDING member procedure display
);
/

-- Employee class implementation.
-- Note that you have to use OVERRIDING in the body too (whereas you don't have to use NOT FINAL here).
CREATE OR REPLACE TYPE BODY Employee AS
	OVERRIDING MEMBER PROCEDURE display IS
	BEGIN
		-- How do you call the base class method?
		(self as Person).display();

		dbms_output.put_line('I am an employee named ' || self.name || '.');
		dbms_output.put_line('I make $' || self.salary || ' per year.');
	END display;
END;
/

-- Use the Person and Employee class.
DECLARE
	p1 Person;
	e1 Employee;

BEGIN
	dbms_output.put_line('Hello, OOP in PL/SQL!');
	-- PL/SQL gives you a default constructor whose args are the object attributes in order of declaration.
	p1 := Person('YodbobenbobR2');
	-- You can use the optional :=new syntax if you want it to be clear you are calling a -- construtor.
	e1 :=new Employee('Yobama', 150000);

	p1.display();
	e1.display();

END;
/


