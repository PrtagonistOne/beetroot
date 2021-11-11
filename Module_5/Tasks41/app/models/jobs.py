from sqlalchemy import Column, Integer, String, DECIMAL

from app.declarative_base import Base


class Jobs(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    job_title = Column(String(25))
    min_salary = Column(DECIMAL(20))
    max_salary = Column(DECIMAL(20))

    def __str__(self):
        return f'{self.job_id}, {self.job_title}, {self.min_salary}, {self.max_salary}'

    def __repr__(self):
        return self.__str__()
