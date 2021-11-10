from sqlalchemy import Column, Integer, String

from app.declarative_base import Base


class Departments(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    depart_name = Column(String(20))
    manager_id = Column(Integer)
    location_id = Column(Integer)

    def __str__(self):
        return f'Department id: {self.department_id}, Department name: {self.depart_name} \n' \
               f'Manager id: {self.manager_id}, Location id: {self.location_id}'

    def __repr__(self):
        return self.__str__()
