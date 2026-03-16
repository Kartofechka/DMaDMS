CREATE TABLE Students(
ID INT IDENTITY(1,1),
FIO NVARCHAR (70),
Grades INT,
PRIMARY KEY(ID),
FOREIGN KEY (Grades) REFERENCES Grades (ID),
)
CREATE TABLE Grades(
ID INT IDENTITY(1,1),
Grades INT,
Teacher INT,
PRIMARY KEY(ID),
FOREIGN KEY (Teacher) REFERENCES Teachers (ID),
)
CREATE TABLE Teachers(
ID INT IDENTITY(1,1),
FIO NVARCHAR(70),
Grades INT,
Subj INT,
PRIMARY KEY(ID),
FOREIGN KEY (Subj) REFERENCES Subjects (ID),
)
CREATE TABLE Subjects(
ID INT IDENTITY(1,1),
Name NVARCHAR(25),
Grades INT,
PRIMARY KEY(ID),
)


insert into Subjects values ('Proga', '10')
insert into Teachers values ('ChinGinShan', '10', '1')
insert into Grades values ('10', '1')
insert into Students values ('Shurupovert', '1')

SELECT Students.ID, Students.FIO, Grades.Grades, Teachers.FIO, Subjects.Name FROM Students
	JOIN Grades ON Grades.ID = Students.Grades
	JOIN Teachers ON Teachers.ID = Grades.Teacher
	JOIN Subjects ON Subjects.ID = Teachers.Subj;



