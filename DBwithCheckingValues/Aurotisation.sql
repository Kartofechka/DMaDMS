use yzsr31

drop table ROLES
drop table USERS

create table ROLES(
	Role_id int identity(1,1) primary key,
	Role_name nvarchar(25)
)


create table USERS(
	ID int identity(1,1) primary key,
	[Name] nvarchar(16),
	Surname nvarchar(32),
	[Login] nvarchar(16) UNIQUE CHECK ([Login] NOT LIKE '^[A-Za-z0-9_]+$^'),
	Email nvarchar(32) CHECK (Email LIKE '%@%.%'),
	[Role] int,
	[Password] nvarchar(100),
	Birthday date CHECK (Birthday <= DATEADD(year, -18, GETDATE()) AND Birthday > DATEADD(year, -100, GETDATE())),
	constraint FK foreign key ([Role]) references ROLES(Role_id)
)

DECLARE @role_name NVARCHAR(25)

select @role_name = 'Some role'

IF @role_name IS NOT NULL AND LEN(@role_name) > 0
BEGIN
    INSERT INTO ROLES VALUES (@role_name)
END
ELSE
BEGIN
	PRINT 'Bad role name'
END


DECLARE @Name nvarchar(16)
DECLARE @Surname nvarchar(32)
DECLARE @Login nvarchar(16)
DECLARE @Email nvarchar(32)
DECLARE @Role int
DECLARE @Password nvarchar(100)
DECLARE @Birthday date

select @Name = 'Имя'
select @Surname = 'Фамилия'
select @Login = 'login'
select @Email = 'Lupa@pupa.com'
select @Role = 1
select @Password = '1111'
select @Birthday = '22-02-2002'

IF @Name IS NULL OR LEN(@Name) < 1
	PRINT 'Incorrect input data in Name'
else
	IF @Surname IS NULL OR LEN(@Surname) = 0
		PRINT 'Incorrect input data in Surname'
	else
		If @Login IS NULL OR LEN(@Login) = 0 OR (@Login LIKE '^[A-Za-z0-9_]+$^') 
			PRINT 'Incorrect input data in Login'
		else
			IF @Email IS NULL OR LEN(@Email) = 0 OR @Email NOT LIKE '%@%.%'
				PRINT 'Incorrect input data in Email'
			else
				If @Role IS NULL OR LEN(@Role) = 0
					PRINT 'Incorrect input data in Role'
				else
					If @Password IS NULL OR LEN(@Password) = 0
						PRINT 'Incorrect input data in Password'
					else
						If @Birthday IS NULL OR LEN(@Birthday) = 0 OR (@Birthday >= DATEADD(year, -18, GETDATE()) OR @Birthday < DATEADD(year, -100, GETDATE()))
							PRINT 'Incorrect input data in Birthday'
						ELSE
							INSERT INTO USERS VALUES (@Name, @Surname, @Login, @Email, @Role, @Password, @Birthday)




insert into ROLES values ('Дензель')
insert into USERS values ('Тема', 'Солярка', 'inspector', 'diezel1488@tut.by', '1', '1234', '24-03-2005')

