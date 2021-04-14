CREATE TABLE college (
id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
city_name VARCHAR(100) NOT NULL,
region_name VARCHAR(100) NOT NULL,
country_name VARCHAR(100) NOT NULL,
founded SMALLINT NOT NULL);

INSERT INTO college
(name, city_name, region_name, country_name, founded)
VALUES
('Des Moines Area Community College',' Des Moines',' Iowa','USA',1968);

INSERT INTO college
(name, city_name, region_name, country_name, founded)
VALUES
('Minneapolis College of Art and Design', 'Minneapolis', 'Minnesota', 'USA', 1886);

INSERT INTO college
(name, city_name, region_name, country_name, founded)
VALUES
('Simpson College',' Indianola', 'Iowa', 'USA', 1860);

INSERT INTO college
(name, city_name, region_name, country_name, founded)
VALUES
('Minnesota University', 'Minneapolis', 'Minnesota', 'USA', 1851);

INSERT INTO college
(name, city_name, region_name, country_name, founded)
VALUES
('Iowa State University', 'Ames', 'Iowa', 'USA', 1858);

CREATE TABLE student (
college_id SERIAL, 
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL);

INSERT INTO student
(first_name,last_name)
VALUES
('Kellen', 'Zanders')
;

INSERT INTO student
(first_name,last_name)
VALUES
('Dylan', 'Martis')
;

INSERT INTO student
(first_name,last_name)
VALUES
('Johnny', 'Herrera')
;

INSERT INTO student
(first_name,last_name)
VALUES
('Joshua', 'Eldrige')
;

INSERT INTO student
(first_name,last_name)
VALUES
('Sophia', 'Van Zee')
;

INSERT INTO student
(first_name,last_name)
VALUES
('Austin', 'Dunlap')
;



DROP TABLE student;
DROP TABLE


CREATE TABLE students(
id SERIAL PRIMARY KEY,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
college_id INT,
CONSTRAINT fk_college_id
FOREIGN KEY(college_id)
REFERENCES college(id)
ON DELETE CASCADE
);

INSERT INTO students(first_name, last_name, college_id)
VALUES
('Kellen','Zanders', 1);

INSERT INTO students(first_name, last_name, college_id)
VALUES
('Kellen','Zanders', 2);

INSERT INTO students(first_name, last_name, college_id)
VALUES
('Kellen','Zanders', 3);

INSERT INTO students(first_name, last_name, college_id)
VALUES
('Dylan','Martis', 2);

INSERT INTO students(first_name, last_name, college_id)
VALUES
('Sophie','Van Zee', 5);

INSERT INTO students(first_name, last_name, college_id)
VALUES
('Austn','Dunlap', 4);


SELECT * FROM college
FULL  OUTER JOIN students ON college.id=students.college_id;

CREATE VIEW catalog AS SELECT college.id, college.name , college.city_name, college.region_name, college.country_name, college.founded
FROM college;

SELECT * from catalog;
DELETE
FROM college
WHERE college.id = 5;

SELECT * FROM college
FULL  OUTER JOIN students ON college.id=students.college_id;