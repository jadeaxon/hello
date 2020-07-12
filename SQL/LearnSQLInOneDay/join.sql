CREATE TABLE one(
	A int,
	B int
);

CREATE TABLE two(
	C int,
	B double, 
	D VARCHAR(255)
);


INSERT INTO one VALUES
(1, 259),
(2, 125),
(3, 731)
;

INSERT INTO two VALUES
(2, 218.1, 'ABC'),
(3, 511.5, 'DEF'), 
(4, 219.9, 'GHI')
;


SELECT A, C, one.B AS 'one B', two.B AS 'two B'
FROM
one
RIGHT JOIN
two
ON
A = C;


