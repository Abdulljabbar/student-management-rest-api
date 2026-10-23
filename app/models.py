
from sqlalchemy import Column, Integer, String
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    rollNo = Column(String(20), unique=True, nullable=False)

    department = Column(String(100), nullable=False)

    semester = Column(Integer, nullable=False)
