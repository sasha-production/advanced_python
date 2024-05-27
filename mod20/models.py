from sqlalchemy import Column, Integer, Float, create_engine, String, Date, Boolean, DateTime, case, func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

engine = create_engine("sqlite:///library.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.count}, {self.release_date}, {self.author_id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(100), nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.surname}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(100), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    @classmethod
    def get_student_by_scholarship(cls):
        students = session.query(Student).filter(Student.scholarship == 1).all()
        students_list = [student.to_json() for student in students]
        return students_list

    @classmethod
    def get_students_by_high_average_score(cls, input_score):
        students = session.query(Student).filter(Student.average_score > input_score).all()
        students_list = [student.to_json() for student in students]
        return students_list

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.phone}, {self.email}, {self.average_score}, {self.scholarship}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False, default=datetime.datetime.now)
    date_of_return = Column(DateTime, nullable=True)

    @hybrid_property
    def count_date_with_book(self):
        end_date = self.date_of_return or datetime.datetime.now()
        return (end_date - self.date_of_issue).days

    @count_date_with_book.expression
    def count_date_with_book(cls):
        end_date = case(
    (cls.date_of_return != None, cls.date_of_return),
           else_=func.now())
        return func.julianday(end_date) - func.julianday(cls.date_of_issue)

    def __repr__(self):
        return (f"{self.book_id}, {self.student_id}, {self.date_of_issue}, "
        f"{self.date_of_return}")

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}