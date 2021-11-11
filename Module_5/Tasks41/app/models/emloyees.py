from sqlalchemy import Column, Integer, String, DATE, Float, NUMERIC

from app.declarative_base import Base


class Employees(Base):
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    first_name = Column(String(20))
    last_name = Column(String(25))
    email = Column(String(25))
    phone_number = Column(String(20))
    hire_date = Column(DATE)
    salary = Column(Float(20))
    commission_pct = Column(Integer)
    manager_id = Column(Integer)
    avg_salary = Column(NUMERIC(25))

    def __str__(self):
        return f'{self.employee_id}, {self.first_name}, {self.last_name}\n ' \
               f'{self.email}, {self.phone_number}, {self.hire_date}\n ' \
               f'{self.salary}, {self.commission_pct}, {self.manager_id},' \
               f'{self.avg_salary}\n'

    def __repr__(self):
        return self.__str__()