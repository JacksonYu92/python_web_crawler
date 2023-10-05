from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):

    __tablename__ = 'testtable'

    id = Column(Integer(), primary_key=True)
    name = Column(String(45))
    sex = Column(String(45))

    def __init__(self, id, name, sex):
        self.id = id
        self.name = name
        self.sex = sex

    engine = create_engine('mysql+pymysql://root:toor@localhost:3306/testdb', echo=False)

    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    item1 = Person(id=1, name='xgx', sex='male')
    session.add(item1)

    item2 = Person(id=2, name='xgx1', sex='female')
    session.add(item2)

    item3 = Person(id=3, name='xgx1', sex='male')
    session.add(item3)

    item4 = Person(id=4, name='xgx2', sex='female')
    session.add(item4)

    session.commit()
    session.close()

    # session1 = DBSession()
    # persons = session1.query(Person).filter(Person.id < '4').all()
    #
    # for i in range(len(persons)):
    #     print(persons[i].id)
    #     print(persons[i].name)
    #     print(persons[i].sex)
    #
    # session1.close()
    #
    # session2 = DBSession()
    # session2.query(Person).filter(Person.id == '2').update({Person.name:'xxx'}, synchronize_session)
    # session2.commit()
    # session2.close()
    #
    # session3 = DBSession()
    # print('\n')
    # print(session3.query(Person).filter(Person.id == '2').one().name)
    # session3.close()
    #
    # session4 = DBSession()
    # session4.query(Person).filter(Person.id == '3').delete()
    # session4.commit()
    # session4.close()
