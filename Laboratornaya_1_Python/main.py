import datetime
import pandas as pd
from sqlalchemy import NVARCHAR, ForeignKey, Identity, String, create_engine, select, text
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


# Создание подключения к БД:   'Тип_БД+драйвер://пользователь:пароль@хост/имя_БД?driver=ODBC+driver+17+for+SQL+Server'

database_url = "mssql+pyodbc://@10.100.0.6\\MIWN36/yzsr31?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(database_url, echo=True)

class Base(DeclarativeBase):
    pass

class STUD(Base):
    __tablename__ = "STUD"

    ID: Mapped[int] = mapped_column(Identity(start=1, increment=1), primary_key=True)
    LAST_NAME: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    FIRST_NAME: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    SECOND_NAME: Mapped[str | None] = mapped_column(NVARCHAR(25), nullable=True)
    FORM: Mapped[str] = mapped_column(NVARCHAR(10), nullable=False, default='очная')
    FACULTY: Mapped[str] = mapped_column(NVARCHAR(10), nullable=False, default='ФПМ')
    YEAR: Mapped[int] = mapped_column(nullable=False, default=1)
    ALL_HOURS: Mapped[int] = mapped_column(default=None)
    INCLASS_HOURS: Mapped[int] = mapped_column(default=None)
    BIRTH_DATE: Mapped[datetime.date] = mapped_column()
    IN_DATE: Mapped[datetime.date] = mapped_column()
    EXM: Mapped[float] = mapped_column(default=None)
    """     Create table stud
        (id int not  null IDENTITY(1,1),
        last_name nvarchar(25) not null,
        f_name nvarchar(25) not null,
        s_name nvarchar(25),
        form nvarchar(10) not null default 'очная',
        faculty nvarchar(10) not null default 'ФПМ',
        year int  not null default 1,
        all_h int default NULL,
        inclass_h int default NULL,
        br_date date,
        in_date date,   
        exm float default NULL,
        CONSTRAINT PK_stud Primary key (id) """

class TEACH(Base):
    __tablename__ = "TEACH"

    ID: Mapped[int] = mapped_column(Identity(start=1, increment=1), primary_key=True)
    LAST_NAME: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    FIRST_NAME: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    SECOND_NAME: Mapped[str | None] = mapped_column(NVARCHAR(25), nullable=True)
    SUBJ: Mapped[str] = mapped_column(NVARCHAR(150))
    FORM: Mapped[str] = mapped_column(NVARCHAR(10), nullable=False, default='очная')
    FACULTY: Mapped[str] = mapped_column(NVARCHAR(10), nullable=False, default='ФПМ')
    YEAR: Mapped[int] = mapped_column(nullable=False, default=1)
    HOURS: Mapped[int] = mapped_column(default=None)
    BIRTH_DATE: Mapped[datetime.date] = mapped_column()
    START_WORK_DATE: Mapped[datetime.date] = mapped_column()

    """     (id int not  null IDENTITY(1,1),
            last_name nvarchar(25) not null,
            f_name nvarchar(25) not null,
            s_name nvarchar(25),
            subj nvarchar(150),
            form nvarchar(10) not null default 'очная',
            faculty nvarchar(10) not null default 'ФПМ',
            year int default 1 not NULL,
            hours int default NULL,
            br_date date,
            start_work_date date,
            CONSTRAINT PK_teach Primary key (id)
            ); """


#Base.metadata.create_all(engine)


def input_students(session):
    student_input_data = [
            ['Стрынгель','К', None,'заочная','ФПК',1,300,100,'19831212','20160901',8],
            ['Козлова', 'Д', 'Е', 'заочная', 'ФПК',2,300,100,'19831012','20150901',8.4],
            ['Федоров', 'Н', 'Н', 'заочная', 'ФПК',3,300,100,'19811207','20140901',7],
            ['Рингель', 'П', 'О', 'заочная', 'ФПК',3,300,100,'19730215','20160901',8],
            ['Бежик', 'Н', 'Н', 'вечерняя', 'ФПК',1,500,400,'19931211','20160901',4.5],
            ['Осипчик', 'Н', 'Н', 'вечерняя', 'ФПК',1,500,400,'19831216','20150901',7.7],
            ['Белый', 'С', 'С', 'вечерняя', 'ФПК',2,450,370,'19870627','20150901',6.7],
            ['Ботяновский', 'А', 'С', 'вечерняя', 'ФПК',2,450,370,'19870723','20150901',7.6],
            ['Слободницкий', 'С', 'А', 'вечерняя', 'ФПК',2,450,370,'19870803','20150901',6.7],
            ['Рогатка', 'П', 'Р', 'очная', 'ФПМ',1,500,450,'19861027','20160901',7.4],
            ['Федоренко', 'П', 'Р', 'очная', 'ФПМ',1,500,450,'19950426','20160901',5.6],
            ['Зингель', 'П', 'В', 'очная', 'ФПМ',2,500,450,'19900425','20150901',3.4],
            ['Михеенок', 'Л', 'Н', 'очная', 'ФПМ',2,500,450,'19890313','20150901',5.3],
            ['Савицкая', 'Л', 'Н', 'очная', 'ФПМ',3,450,400, '19950705','20140901',7.7],
            ['Ковальчук', 'О', 'Е', 'заочная', 'ФПМ',1,350,100,'19640523','20160901',7.6],
            ['Заболотная', 'Л', 'И', 'заочная', 'ФПМ',1,350,100,'19860914','20160901',4.7],
            ['Ковриго', 'И', None, 'заочная', 'ФПМ',2,360,120,'19920301', '20150901',7.7],
            ['Шарапо', 'М', None, 'заочная', 'ФПМ',2,360,120,'19970325', '20150901',8.7],
            ['Сафроненко', 'Н', 'Л', 'заочная', 'ФПМ',3,370,130, '19920525','20140901',7.7],
            ['Зайцева', 'Т', 'Я', 'заочная', 'ФПМ',3,370,130,'19940725','20140901',5.6]
        ]
    for last_name, f_name, s_name, form, faculty, year, all_h, inclass_h, br_date, in_date, exm in student_input_data:
        session.add(STUD(LAST_NAME=last_name, FIRST_NAME=f_name,
                        SECOND_NAME=s_name, FORM=form, 
                        FACULTY=faculty, YEAR=year, 
                        ALL_HOURS=all_h, INCLASS_HOURS=inclass_h, 
                        BIRTH_DATE=datetime.datetime.strptime(br_date, '%Y%m%d').date(), 
                        IN_DATE=datetime.datetime.strptime(in_date, '%Y%m%d').date(), EXM=exm))
    session.commit()

    """ insert into stud 
            (last_name,f_name,s_name,form,faculty,year,all_h,inclass_h,br_date,in_date,exm) values
            (N'Стрынгель',N'К',null,N'заочная',N'ФПК',1,300,100,'19831212','20160901',8),
            (N'Козлова',N'Д',N'Е',N'заочная',N'ФПК',2,300,100,'19831012','20150901',8.4),
            (N'Федоров',N'Н',N'Н',N'заочная',N'ФПК',3,300,100,'19811207','20140901',7),
            (N'Рингель',N'П',N'О',N'заочная',N'ФПК',3,300,100,'19730215','20160901',8),
            (N'Бежик',N'Н',N'Н',N'вечерняя',N'ФПК',1,500,400,'19931211','20160901',4.5),
            (N'Осипчик',N'Н',N'Н',N'вечерняя',N'ФПК',1,500,400,'19831216','20150901',7.7),
            (N'Белый',N'С',N'С',N'вечерняя',N'ФПК',2,450,370,'19870627','20150901',6.7),
            (N'Ботяновский',N'А',N'С',N'вечерняя',N'ФПК',2,450,370,'19870723','20150901',7.6),
            (N'Слободницкий',N'С',N'А',N'вечерняя',N'ФПК',2,450,370,'19870803','20150901',6.7),
            (N'Рогатка',N'П',N'Р',N'очная',N'ФПМ',1,500,450,'19861027','20160901',7.4),
            (N'Федоренко',N'П',N'Р',N'очная',N'ФПМ',1,500,450,'19950426','20160901',5.6),
            (N'Зингель',N'П',N'В',N'очная',N'ФПМ',2,500,450,'19900425','20150901',3.4),
            (N'Михеенок',N'Л',N'Н',N'очная',N'ФПМ',2,500,450,'19890313','20150901',5.3),
            (N'Савицкая',N'Л',N'Н',N'очная',N'ФПМ',3,450,400, '19950705','20140901',7.7),
            (N'Ковальчук',N'О',N'Е',N'заочная',N'ФПМ',1,350,100,'19640523','20160901',7.6),
            (N'Заболотная',N'Л',N'И',N'заочная',N'ФПМ',1,350,100,'19860914','20160901',4.7),
            (N'Ковриго',N'И',null,N'заочная',N'ФПМ',2,360,120,'19920301', '20150901',7.7),
            (N'Шарапо',N'М',null,N'заочная',N'ФПМ',2,360,120,'19970325', '20150901',8.7),
            (N'Сафроненко',N'Н',N'Л',N'заочная',N'ФПМ',3,370,130, '19920525','20140901',7.7),
            (N'Зайцева',N'Т',N'Я',N'заочная',N'ФПМ',3,370,130,'19940725','20140901',5.6); """


def input_teachers(session):
    teachers_input_data = [
        ['Скворцов', 'К', None, 'Дифференциальные исчисления', 'очная', 'ФПМ',1,150,'19831212','20160901'],
        ['Скворцов', 'К', None, 'Геометрия и алгебра', 'очная', 'ФПМ',1,200,'19831212','20160901'],
        ['Сидоренко', 'Л', 'К', 'Теория вероятности', 'очная', 'ФПМ',1,100,'19831212','20160901'],
        ['Скворцов', 'К', None, 'Дифференциальные исчисления', 'заочная', 'ФПМ',1,34,'19831212','20160901'],
        ['Сидоренко', 'Л', 'К', 'Геометрия и алгебра', 'заочная', 'ФПМ',1,50,'19831212','20160901'],
        ['Сидоренко', 'Л', 'К', 'Теория вероятности', 'заочная', 'ФПМ',1,16,'19831212','20160901'],
        ['Круглов', 'К', 'Д', 'Теория множеств', 'очная', 'ФПМ',2,150,'19860825','20140901'],
        ['Круглов', 'К', 'Д', 'Методы численного анализа', 'очная', 'ФПМ',2,150,'19860825','20140901'],
        ['Загорова', 'К', 'Д', 'Прикладная статистика', 'очная', 'ФПМ',2,150,'19791005','20100901'],
        ['Круглов', 'К', 'Д', 'Теория множеств', 'заочная', 'ФПМ',2,40,'19860825','20140901'],
        ['Круглов', 'К', 'Д', 'Методы численного анализа', 'заочная', 'ФПМ',2,40,'19860825','20140901'],
        ['Загорова', 'К', 'Д', 'Прикладная статистика', 'заочная', 'ФПМ',2,40,'19791005','20100901'],
        ['Зуров', 'П', None, 'Философия', 'очная', 'ФПМ',3,50,'19780712','20160901'],
        ['Зуров', 'П', None, 'Социология', 'очная', 'ФПМ',3,50,'19780712','20160901'],
        ['Сидоренко', 'Л', 'К', 'Методы машинного обучения', 'очная', 'ФПМ',3,150,'19831212','20160901'],
        ['Журков', 'К', None, 'Методы выпуклой оптимизации', 'очная', 'ФПМ',3,150,'19861116','20150901'],
        ['Курт', 'П', 'Р', 'Философия', 'заочная', 'ФПМ',3,20,'19780712','20160901'],
        ['Курт', 'П', 'Р', 'Социология', 'заочная', 'ФПМ',3,20,'19780712','20160901'],
        ['Сидоренко', 'Л', 'К', 'Методы машинного обучения', 'заочная', 'ФПМ',3,50,'19831212','20160901'],
        ['Журков', 'К', None, 'Методы выпуклой оптимизации', 'заочная', 'ФПМ',3,40,'19861116','20150901'],

        ['Скворцов', 'К', None, 'Основы алгоритмизации', 'заочная', 'ФПК',1,30,'19780212','20160901'],
        ['Скворцов', 'К', None, 'Основы операционных систем', 'заочная', 'ФПК',1,20,'19780212','20160901'],
        ['Сидоренко', 'Л', 'К', 'Объектно-ориенторованное программирование', 'заочная', 'ФПК',1,50,'19831212','20160901'],

        ['Скворцов', 'К', None, 'Основы алгоритмизации', 'вечерняя', 'ФПК',1,100,'19780212','20160901'],
        ['Скворцов', 'К', None, 'Основы операционных систем', 'вечерняя', 'ФПК',1,100,'19780212','20160901'],
        ['Сидоренко', 'Л', 'К', 'Объектно-ориенторованное программирование', 'вечерняя', 'ФПК',1,200,'19831212','20160901'],

        ['Кипеня', 'Д', 'А', 'Компонентное программирование', 'заочная', 'ФПК',2,30,'19840109','20130901'],
        ['Зорков', 'К', 'А', 'Средства визуального программирования', 'заочная', 'ФПК',2,40,'19891212','20160901'],
        ['Иридова', 'Т', 'К', 'Объектно-ориенторованное программирование', 'заочная', 'ФПК',1,50,'19830412','20160901'],

        ['Кипеня', 'Д', 'А', 'Компонентное программирование', 'вечерня', 'ФПК',2,130,'19840109','20130901'],
        ['Зорков', 'К', 'А', 'Средства визуального программирования', 'вечерняя', 'ФПК',2,140,'19891212','20160901'],
        ['Иридова', 'Т', 'К', 'Объектно-ориенторованное программирование', 'вечерняя', 'ФПК',2,110,'19830412','20160901'],

        ['Курт', 'П', 'Р', 'Философия', 'заочная', 'ФПК',3,20,'19780712','20160901'],
        ['Курт', 'П', 'Р', 'Социология', 'заочная', 'ФПК',3,20,'19780712','20160901'],
        ['Иридова', 'Т', 'К', 'Современные языки программирования', 'заочная', 'ФПК',3,30,'19830412','20160901'],
        ['Иридова', 'Т', 'К', 'Тестирование программного обеспечения', 'заочная', 'ФПК',3,30,'19830412','20160901'],

        ['Курт', 'П', 'Р', 'Философия', 'вечерня', 'ФПК',3,40,'19780712','20160901'],
        ['Курт', 'П', 'Р', 'Социология', 'вечерня', 'ФПК',3,40,'19780712','20160901'],
        ['Иридова', 'Т', 'К', 'Современные языки программирования', 'вечерня', 'ФПК',3,150,'19830412','20160901'],
        ['Иридова', 'Т', 'К', 'Тестирование программного обеспечения', 'вечерня', 'ФПК',3,160,'19830412','20160901']
    ]
    
    for last_name, f_name, s_name, subject, form, faculty, year, hours, br_date, start_work_date in teachers_input_data:
        session.add(TEACH(LAST_NAME=last_name, FIRST_NAME=f_name,
                        SECOND_NAME=s_name, SUBJ=subject,
                        FORM=form, FACULTY=faculty,
                        YEAR=year, HOURS=hours,
                        BIRTH_DATE=datetime.datetime.strptime(br_date, '%Y%m%d').date(),
                        START_WORK_DATE=datetime.datetime.strptime(start_work_date, '%Y%m%d').date()))
    session.commit()

    """ insert into teach values
        (N'Скворцов',N'К',null,N'Дифференциальные исчисления',N'очная',N'ФПМ',1,150,'19831212','20160901'),
        (N'Скворцов',N'К',null,N'Геометрия и алгебра',N'очная',N'ФПМ',1,200,'19831212','20160901'),
        (N'Сидоренко',N'Л',N'К',N'Теория вероятности',N'очная',N'ФПМ',1,100,'19831212','20160901'),
        (N'Скворцов',N'К',null,N'Дифференциальные исчисления',N'заочная',N'ФПМ',1,34,'19831212','20160901'),
        (N'Сидоренко',N'Л',N'К',N'Геометрия и алгебра',N'заочная',N'ФПМ',1,50,'19831212','20160901'),
        (N'Сидоренко',N'Л',N'К',N'Теория вероятности',N'заочная',N'ФПМ',1,16,'19831212','20160901'),
        (N'Круглов',N'К',N'Д',N'Теория множеств',N'очная',N'ФПМ',2,150,'19860825','20140901'),
        (N'Круглов',N'К',N'Д',N'Методы численного анализа',N'очная',N'ФПМ',2,150,'19860825','20140901'),
        (N'Загорова',N'К',N'Д',N'Прикладная статистика',N'очная',N'ФПМ',2,150,'19791005','20100901'),
        (N'Круглов',N'К',N'Д',N'Теория множеств',N'заочная',N'ФПМ',2,40,'19860825','20140901'),
        (N'Круглов',N'К',N'Д',N'Методы численного анализа',N'заочная',N'ФПМ',2,40,'19860825','20140901'),
        (N'Загорова',N'К',N'Д',N'Прикладная статистика',N'заочная',N'ФПМ',2,40,'19791005','20100901'),
        (N'Зуров',N'П',null,N'Философия',N'очная',N'ФПМ',3,50,'19780712','20160901'),
        (N'Зуров',N'П',null,N'Социология',N'очная',N'ФПМ',3,50,'19780712','20160901'),
        (N'Сидоренко',N'Л',N'К',N'Методы машинного обучения',N'очная',N'ФПМ',3,150,'19831212','20160901'),
        (N'Журков',N'К',null,N'Методы выпуклой оптимизации',N'очная',N'ФПМ',3,150,'19861116','20150901'),
        (N'Курт',N'П',N'Р',N'Философия',N'заочная',N'ФПМ',3,20,'19780712','20160901'),
        (N'Курт',N'П',N'Р',N'Социология',N'заочная',N'ФПМ',3,20,'19780712','20160901'),
        (N'Сидоренко',N'Л',N'К',N'Методы машинного обучения',N'заочная',N'ФПМ',3,50,'19831212','20160901'),
        (N'Журков',N'К',null,N'Методы выпуклой оптимизации',N'заочная',N'ФПМ',3,40,'19861116','20150901'),

        (N'Скворцов',N'К',null,N'Основы алгоритмизации',N'заочная',N'ФПК',1,30,'19780212','20160901'),
        (N'Скворцов',N'К',null,N'Основы операционных систем',N'заочная',N'ФПК',1,20,'19780212','20160901'),
        (N'Сидоренко',N'Л',N'К',N'Объектно-ориенторованное программирование',N'заочная',N'ФПК',1,50,'19831212','20160901'),

        (N'Скворцов',N'К',null,N'Основы алгоритмизации',N'вечерняя',N'ФПК',1,100,'19780212','20160901'),
        (N'Скворцов',N'К',null,N'Основы операционных систем',N'вечерняя',N'ФПК',1,100,'19780212','20160901'),
        (N'Сидоренко',N'Л',N'К',N'Объектно-ориенторованное программирование',N'вечерняя',N'ФПК',1,200,'19831212','20160901'),

        (N'Кипеня',N'Д',N'А',N'Компонентное программирование',N'заочная',N'ФПК',2,30,'19840109','20130901'),
        (N'Зорков',N'К',N'А',N'Средства визуального программирования',N'заочная',N'ФПК',2,40,'19891212','20160901'),
        (N'Иридова',N'Т',N'К',N'Объектно-ориенторованное программирование',N'заочная',N'ФПК',1,50,'19830412','20160901'),

        (N'Кипеня',N'Д',N'А',N'Компонентное программирование',N'вечерня',N'ФПК',2,130,'19840109','20130901'),
        (N'Зорков',N'К',N'А',N'Средства визуального программирования',N'вечерняя',N'ФПК',2,140,'19891212','20160901'),
        (N'Иридова',N'Т',N'К',N'Объектно-ориенторованное программирование',N'вечерняя',N'ФПК',2,110,'19830412','20160901'),

        (N'Курт',N'П',N'Р',N'Философия',N'заочная',N'ФПК',3,20,'19780712','20160901'),
        (N'Курт',N'П',N'Р',N'Социология',N'заочная',N'ФПК',3,20,'19780712','20160901'),
        (N'Иридова',N'Т',N'К',N'Современные языки программирования',N'заочная',N'ФПК',3,30,'19830412','20160901'),
        (N'Иридова',N'Т',N'К',N'Тестирование программного обеспечения',N'заочная',N'ФПК',3,30,'19830412','20160901'),

        (N'Курт',N'П',N'Р',N'Философия',N'вечерня',N'ФПК',3,40,'19780712','20160901'),
        (N'Курт',N'П',N'Р',N'Социология',N'вечерня',N'ФПК',3,40,'19780712','20160901'),
        (N'Иридова',N'Т',N'К',N'Современные языки программирования',N'вечерня',N'ФПК',3,150,'19830412','20160901'),
        (N'Иридова',N'Т',N'К',N'Тестирование программного обеспечения',N'вечерня',N'ФПК',3,160,'19830412','20160901'); """


def input_db(session):
    input_students(session=session)
    input_teachers(session=session)


def first_task():
    df = pd.read_sql(text(f"SELECT LAST_NAME FROM STUD WHERE LAST_NAME LIKE '%об%' or  LAST_NAME LIKE '%бо%'"), engine)
    print(f"\n\n ПЕРВОЕ ЗАДАНИЕ\n {df}\n\n\n")


def second_task():
    df = pd.read_sql(text(f"SELECT * FROM STUD WHERE SECOND_NAME IS NULL AND LAST_NAME LIKE 'К%'"), engine)
    print(f"\n\n ВТОРОЕ ЗАДАНИЕ\n {df}\n\n\n")


def third_task():
    df = pd.read_sql(text(f"SELECT * FROM STUD WHERE LEN(LAST_NAME) >= 8"), engine)
    print(f"\n\n ТРЕТЬЕ ЗАДАНИЕ\n {df}\n\n\n")


def fourth_task():
    df = pd.read_sql(text(f"SELECT * FROM STUD WHERE LAST_NAME LIKE '%а%' AND (LEN(LAST_NAME) > 7 OR LEN(LAST_NAME) < 7)"), engine)
    print(f"\n\n ЧЕТВЕРТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def fifth_task():
    df = pd.read_sql(text(f"SELECT * FROM STUD WHERE FACULTY = 'ФПМ' AND FORM = 'очная' AND (YEAR = 1 OR YEAR = 2) ORDER BY SECOND_NAME"), engine)
    print(f"\n\n ПЯТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def sixth_task():
    df = pd.read_sql(text(f"SELECT * FROM STUD WHERE FACULTY = 'ФПК' AND FORM = 'заочная' AND EXM > 6 ORDER BY EXM DESC"), engine)
    print(f"\n\n ШЕСТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def seventh_task():
    df = pd.read_sql(text(f"SELECT * FROM TEACH WHERE FACULTY = 'ФПК' ORDER BY FORM, LAST_NAME"), engine)
    print(f"\n\n СЕДЬМОЕ ЗАДАНИЕ\n {df}\n\n\n")


def eighth_task():
    df = pd.read_sql(text(f"SELECT * FROM TEACH WHERE FACULTY = 'ФПМ' AND YEAR = 1 AND HOURS > 100"), engine)
    print(f"\n\n ВОСЬМОЕ ЗАДАНИЕ\n {df}\n\n\n")


def nineth_task():
    df = pd.read_sql(text(f"SELECT * FROM TEACH WHERE SECOND_NAME IS NULL AND DATEDIFF(year, START_WORK_DATE, GETDATE()) > 3"), engine)
    print(f"\n\n ДЕВЯТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def tenth_task():
    df = pd.read_sql(text(f"SELECT SUBJ, YEAR, FORM, LAST_NAME, FIRST_NAME, SECOND_NAME, HOURS FROM TEACH WHERE FACULTY = 'ФПМ' AND YEAR = 3"), engine)
    print(f"\n\n ДЕСЯТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def eleven_task():
    df = pd.read_sql(text(f"SELECT SUBJ, YEAR, FORM, LAST_NAME, FIRST_NAME, SECOND_NAME, HOURS FROM TEACH WHERE FACULTY = 'ФПК' AND HOURS > 100"), engine)
    print(f"\n\n ОДИННАДЦАТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def twelve_task():
    df = pd.read_sql(text(f"SELECT SUBJ, FACULTY, YEAR, FORM, LAST_NAME, FIRST_NAME, SECOND_NAME FROM TEACH WHERE SECOND_NAME IS NULL"), engine)
    print(f"\n\n ДВЕНАДЦАТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def thourteen_task():
    df = pd.read_sql(text(f"SELECT DISTINCT LAST_NAME, FIRST_NAME, SECOND_NAME, BIRTH_DATE FROM TEACH WHERE DATEDIFF(year, BIRTH_DATE, GETDATE()) > 30"), engine)
    print(f"\n\n ТРИНАДЦАТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def fourteen_task():
    df = pd.read_sql(text(f"SELECT DISTINCT LAST_NAME, FIRST_NAME, SECOND_NAME, BIRTH_DATE FROM TEACH WHERE DATEDIFF(year, BIRTH_DATE, GETDATE()) BETWEEN 35 AND 40 ORDER BY LAST_NAME"), engine)
    print(f"\n\n ЧЕТЫРНАДЦАТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def fifteen_task():
    df = pd.read_sql(text(f"SELECT DISTINCT LAST_NAME, FIRST_NAME, SECOND_NAME, BIRTH_DATE FROM TEACH WHERE MONTH(BIRTH_DATE) = 10 ORDER BY BIRTH_DATE"), engine)
    print(f"\n\n ПЯТНАДЦАТОЕ ЗАДАНИЕ\n {df}\n\n\n")


def all_tasks_start():
    first_task(),
    second_task(),
    third_task(),
    fourth_task(),
    fifth_task(),
    sixth_task(),
    seventh_task(),
    eighth_task(),
    nineth_task(),
    tenth_task(),
    eleven_task(),
    twelve_task(),
    thourteen_task(),
    fourteen_task(),
    fifteen_task()

Session = sessionmaker(bind=engine)
session = Session()

with session:
    #input_db(session=session)
    all_tasks_start()


    session.commit()



session.close()


