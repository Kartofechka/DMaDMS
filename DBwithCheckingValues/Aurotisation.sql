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




insert into ROLES values ('Два'), ('Три'), ('Четыре')
insert into USERS values ('Тема', 'Солярка', 'inspector', 'diezel1488@tut.by', '1', '1234', '24-03-2005')

GO
	CREATE PROCEDURE First_procedure
	@name nvarchar(16),
	@surname nvarchar(32),
	@login nvarchar(16),
	@email nvarchar(32),
	@role int,
	@password nvarchar(100),
	@birthday date

	AS
	PRINT 'Hello world'
GO



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

EXEC First_procedure @Name, @Surname, @Login, @Email, @Role, @Password, @Birthday


GO
	CREATE PROCEDURE Check_and_input_values 
	@name nvarchar(16),
	@surname nvarchar(32),
	@login nvarchar(16),
	@email nvarchar(32),
	@role int,
	@password nvarchar(100),
	@birthday date

	AS
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

GO

DECLARE @Name nvarchar(16)
DECLARE @Surname nvarchar(32)
DECLARE @Login nvarchar(16)
DECLARE @Email nvarchar(32)
DECLARE @Role int
DECLARE @Password nvarchar(100)
DECLARE @Birthday date

select @Name = 'Имя2'
select @Surname = 'Фамилия2'
select @Login = 'login2'
select @Email = 'Lupa2@pupa.com'
select @Role = 1
select @Password = '2222'
select @Birthday = '11-01-2001'

EXEC Check_and_input_values @Name, @Surname, @Login, @Email, @Role, @Password, @Birthday


GO
	CREATE PROCEDURE input_values 
	@name nvarchar(16),
	@surname nvarchar(32),
	@login nvarchar(16),
	@email nvarchar(32),
	@role int,
	@password nvarchar(100),
	@birthday date

	AS
	INSERT INTO USERS VALUES (@Name, @Surname, @Login, @Email, @Role, @Password, @Birthday)
GO


GO
	CREATE FUNCTION Checking_function (
	@name nvarchar(16),
	@surname nvarchar(32),
	@login nvarchar(16),
	@email nvarchar(32),
	@role int,
	@password nvarchar(100),
	@birthday date
	)
	RETURNS int
	AS
		BEGIN
		IF @Name IS NULL OR LEN(@Name) < 1
			RETURN 1
		else
			IF @Surname IS NULL OR LEN(@Surname) = 0
				RETURN 2
			else
				If @Login IS NULL OR LEN(@Login) = 0 OR (@Login LIKE '^[A-Za-z0-9_]+$^') 
					RETURN 3
				else
					IF @Email IS NULL OR LEN(@Email) = 0 OR @Email NOT LIKE '%@%.%'
						RETURN 4
					else
						If @Role IS NULL OR LEN(@Role) = 0
							RETURN 5
						else
							If @Password IS NULL OR LEN(@Password) = 0
								RETURN 6
							else
								If @Birthday IS NULL OR LEN(@Birthday) = 0 OR (@Birthday >= DATEADD(year, -18, GETDATE()) OR @Birthday < DATEADD(year, -100, GETDATE()))
									RETURN 7
								ELSE
									RETURN 0
		RETURN 1
		END
GO


GO
CREATE PROCEDURE Input_procedure
    @name nvarchar(16),
    @surname nvarchar(32),
    @login nvarchar(16),
    @email nvarchar(32),
    @role int,
    @password nvarchar(100),
    @birthday date
AS
BEGIN
    IF dbo.Checking_function(@name, @surname, @login, @email, @role, @password, @birthday) = 0
    BEGIN
        EXEC Input_values @name, @surname, @login, @email, @role, @password, @birthday;
        PRINT 'OK';
        RETURN;
    END
    ELSE
    BEGIN
        PRINT 'Something went wrong';
        RETURN;
    END
END
GO


DECLARE @Name nvarchar(16)
DECLARE @Surname nvarchar(32)
DECLARE @Login nvarchar(16)
DECLARE @Email nvarchar(32)
DECLARE @Role int
DECLARE @Password nvarchar(100)
DECLARE @Birthday date

select @Name = 'Имя3'
select @Surname = 'Фамилия3'
select @Login = 'login3'
select @Email = 'Lupa3@pupa.com'
select @Role = 1
select @Password = '3333'
select @Birthday = '01-10-2003'

EXEC Input_procedure @Name, @Surname, @Login, @Email, @Role, @Password, @Birthday

GO
	CREATE PROCEDURE Updating_procedure
	@role int,
	@new_role int

	AS
	BEGIN
		UPDATE USERS SET USERS.Role = @new_role WHERE USERS.Role = @role
	END
GO

DECLARE @Role int = 1
DECLARE @New_role int = 4

EXEC Updating_procedure @Role, @New_role

