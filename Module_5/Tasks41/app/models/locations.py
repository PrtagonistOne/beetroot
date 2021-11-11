from sqlalchemy import Column, Integer, String

from app.declarative_base import Base


class Locations(Base):
    __tablename__ = 'locations'
    location_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    street_address = Column(String(25))
    postal_code = Column(String(30))
    city = Column(String(30))
    state_province = Column(String(12))
    country_id = Column(String(2))

    def __str__(self):
        return f'{self.location_id}, {self.street_address}, {self.postal_code} \n' \
               f'{self.city}, {self.state_province}, {self.country_id}'
