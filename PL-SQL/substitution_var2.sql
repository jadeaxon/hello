-- Use a substitution varible.
-- Set a user variable to its value so user only has to input it once.
-- How do we define it on the command line instead?
DEFINE x=&input_x;
SELECT '&x' x1, 'Hello, ' || '&x' || '!' x2 FROM dual;
exit


