CREATE TABLE Workers(
    id integer primary key,
    first_name text,
    last_name text);

ALTER TABLE test RENAME TO Employers;

ALTER TABLE Employers ADD Status text NOT NULL default Junior;

INSERT INTO Workers VALUES(1,'John', 'Doe');
INSERT INTO Workers VALUES(2,'Mark', 'Zuckerberg');

DELETE FROM Workers WHERE id = 2;
UPDATE Workers SET first_name = "Jonathan" WHERE first_name = "John";

