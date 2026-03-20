import datetime
import pandas as pd
from sqlalchemy import NVARCHAR, ForeignKey, String, create_engine, select, text
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


# Создание подключения к БД:   'Тип_БД+драйвер://пользователь:пароль@хост/имя_БД?driver=ODBC+driver+17+for+SQL+Server'

database_url = "mssql+pyodbc://:@10.100.0.6\\MIWN36/yzsr31?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(database_url, echo=True)

class Base(DeclarativeBase):
    pass

class GROUPS(Base):
    __tablename__ = "GROUPS"

    ID: Mapped[int] = mapped_column(primary_key=True)
    GROUPS_NAME: Mapped[str] = mapped_column(NVARCHAR(15))
    COURSE: Mapped[int] = mapped_column()

class SUBJECTS(Base):
    __tablename__ = "SUBJECTS"

    ID: Mapped[int] = mapped_column(primary_key=True)
    SUBJECT_NAME: Mapped[str] = mapped_column(NVARCHAR(50))
    SUBJECT_TIME: Mapped[int] = mapped_column()

class STUDENTS(Base):
    __tablename__ = "STUDENTS"

    ID: Mapped[int] = mapped_column(primary_key=True)
    FIRST_NAME: Mapped[str] = mapped_column(NVARCHAR(15))
    SURNAME: Mapped[str] = mapped_column(NVARCHAR(15))
    SECONDNAME: Mapped[str] = mapped_column(NVARCHAR(15))
    BIRTHDAY: Mapped[datetime.date] = mapped_column()
    GROUP_ID: Mapped[int] = mapped_column(ForeignKey("GROUPS.ID"))


class PLAN_(Base):
    __tablename__ = "PLAN_"

    GROUP_ID: Mapped[int] = mapped_column(ForeignKey("GROUPS.ID"), primary_key=True)
    SUBJECT_ID: Mapped[int] = mapped_column(ForeignKey("SUBJECTS.ID"), primary_key= True)

#Base.metadata.create_all(engine)


def input_groups(session):
    groups_input_data = [["ПО135", 1], ["ПО235", 2], ["ПО335", 3]]
    for name, course in groups_input_data:
        session.add(GROUPS(GROUPS_NAME=name, COURSE=course))
    session.commit()


def input_subjects(session):
    subjects_input_data = [['Физика', 200],["Математика", 120],["Основы алгоритмизации", 70],["Проектирование БД", 130],["Средства визуального программирования", 90], ["Объектно-ориентированное программирование", 70]]
    for subject_name, subject_time in subjects_input_data:
        session.add(SUBJECTS(SUBJECT_NAME=subject_name, SUBJECT_TIME=subject_time))
    session.commit()


def input_students(session):
    students_input_data = [["Федоренко", "П.", "Р.", "1997-12-25", 1],
                           ["Зингел", "О.", "", "1985-12-25", 1],
                           ["Савицкаян", "Н.", "", "1987-09-22", 2],
                           ["Ковальчук", "М.", "Е.", "1992-06-17", 2],
                           ["Ковриго", "Т.", "Р.", "1992-05-13",  3],
                           ["Шарапо", "Н.", "", "1992-08-14",  3]
                           ]
    for name, surname, secondname, birthday, group_id in students_input_data:
        session.add(STUDENTS(FIRST_NAME=name, SURNAME=surname, SECONDNAME=secondname, BIRTHDAY=birthday, GROUP_ID=group_id))
    session.commit()


def input_plan(session):
    plan_input_data = [
        [1, 1],
        [1, 2],
        [2, 3],
        [2, 4],
        [3, 5],
        [3, 6]
    ]
    for group_id, subject_id in plan_input_data:
        session.add(PLAN_(GROUP_ID=group_id, SUBJECT_ID=subject_id))
    session.commit()


def update_subjects(session, name):
    subject = session.query(SUBJECTS).filter(SUBJECTS.SUBJECT_NAME == name).first()
    subject.SUBJECT_TIME += 30
    session.commit()


def input_db(session):
    input_groups(session=session)
    input_subjects(session=session)
    input_students(session=session)
    input_plan(session=session)


def updating_db(session):
    update_subjects(session, "Средства визуального программирования")
    update_subjects(session, "Объектно-ориентированное программирование")

Session = sessionmaker(bind=engine)
session = Session()

with session:
    #input_db(session=session)
    #updating_db(session=session)
    session.commit()



sel = select(GROUPS, SUBJECTS, STUDENTS, PLAN_)

table = session.scalars(sel).all()
session.commit()
session.close()

for table in ["GROUPS", "SUBJECTS", "STUDENTS", "PLAN_"]:
    df = pd.read_sql(text(f"SELECT * FROM {table}"), engine)
    print(df)
