import logging

from sqlalchemy import create_engine, sql, func
from sqlalchemy.orm import sessionmaker

from app.declarative_base import Base
from config.init_logging import init_logging
from . import models

DATABASE_NAME = 'HR.db'


def create_db():
    engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=True)
    Base.metadata.create_all(engine)
    return engine


def query1(session: sessionmaker(bind=create_db())):
    return session.query(models.Employees).values(
        models.emloyees.Employees.first_name,
        models.emloyees.Employees.last_name
    )


def query2(session: sessionmaker(bind=create_db())):
    return session.query(models.Employees.first_name).distinct().order_by('first_name')


def query3(session: sessionmaker(bind=create_db())):
    return session.query(models.Employees).order_by(sql.expression.desc(models.Employees.first_name))


def query4(session: sessionmaker(bind=create_db())):
    return session.query(func.max(models.Employees.salary), func.min(models.Employees.salary))


def query5(session: sessionmaker(bind=create_db())):
    q = session.query(models.Employees).values(
        models.emloyees.Employees.first_name,
        models.emloyees.Employees.last_name,
        models.emloyees.Employees.salary / 12
    )
    return [(i[0], i[1], round(i[2], 2)) for i in q]


def make_actions():
    Session = sessionmaker(bind=create_db())  # базу заполнил данными при помощи копипастинга и ручек
    with Session() as session:
        q1 = query1(session=session)
        q2 = query2(session=session)
        q3 = query3(session=session)
        q4 = query4(session=session)
        q5 = query5(session=session)


def run_app():
    init_logging()
    logging.info('start')
    make_actions()
    logging.info('end')


if __name__ == '__main__':
    run_app()
