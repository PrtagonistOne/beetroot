from sqlalchemy import Column, String

from app.declarative_base import Base


class Countries(Base):
    __tablename__ = 'countries'
    country_id = Column(String(2), primary_key=True, unique=True, nullable=False)
    country_name = Column(String(40))
    region_id = Column(String(2))

    def __str__(self):
        return f'Countries: country_id = {self.country_id}\n' \
               f'Country name = {self.country_name}\n' \
               f'Region id = {self.region_id}\n'

    def __repr__(self):
        return str(self)
