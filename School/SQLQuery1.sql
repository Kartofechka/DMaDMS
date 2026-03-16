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


insert into Subjects values ('Matan', '10')
insert into Teachers values ('Pididi', '10', '2')
insert into Grades values ('9', '1')
insert into Grades values ('10', '2')
insert into Grades values ('2', '1')
insert into Grades values ('6', '1')
insert into Grades values ('5', '2')
insert into Grades values ('7', '2')
insert into Grades values ('3', '2')
insert into Students values ('Vladik', '2')
insert into Students values ('Georje', '3')
insert into Students values ('Denchik', '4')
insert into Students values ('Antonina', '5')
insert into Students values ('Dizel', '6')
insert into Students values ('Kirpich', '7')
insert into Students values ('Kiryusha', '8')

SELECT Teachers.FIO as teachers, Students.FIO as students, Students.Grades FROM Teachers
	JOIN Grades on Teachers.ID = Grades.Teacher
	JOIN Students on Grades.ID = Students.Grades
	where Teachers.FIO = 'ChinGinShan'




