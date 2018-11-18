import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:root@localhost/testdb",encoding='utf-8',echo=True)
Base = declarative_base()#生成orm基类
class User(Base):
  __tablename__ = 'user'#表名
  id = Column(Integer,primary_key=True)
  name = Column(String(32))
  password = Column(String(64))
Base.metadata.create_all(engine)#创建表结构
Session_class = sessionmaker(bind=engine)#创建与数据库的会话session class ,注意这里返回给session的是一个类，不是实例
Session = Session_class()#生成session实例
user_obj = User(name = "xiaoming" , password = "123456")#生成你要创建的数据对象
user_obj2 = User(name = "jack" , password = "123564")#生成你要创建的数据对象
print(user_obj.name,user_obj.id)#此时还没有创建对象，打印一下会发现id还是None
Session.add(user_obj)
Session.add(user_obj2)
print(user_obj.name,user_obj.id)#此时也依然还没有创建
Session.commit()