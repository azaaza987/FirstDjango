import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:root@localhost/testdb",encoding='utf-8')
Base = declarative_base()#生成orm基类
class User(Base):
  __tablename__ = 'user'#表名
  id = Column(Integer,primary_key=True)
  name = Column(String(32))
  password = Column(String(64))

  def __repr__(self):
      return "<%s name:%s>" % (self.id, self.name)

Base.metadata.create_all(engine)#创建表结构
Session_class = sessionmaker(bind=engine)#创建与数据库的会话session class ,注意这里返回给session的是一个类，不是实例
Session = Session_class()#生成session实例

print('----------------查询所有名字为xiaoming的数据')
data=Session.query(User).filter_by(name="xiaoming").all()
print(data[0].name,data[0].password)
print(data)

print('----------------查询所有数据')
data=Session.query(User).filter_by().all()
print(data)

print('----------------查询第一条数据')
data=Session.query(User).filter_by().first()
print(data)


print('----------------查询id大于 1 的数据')
data=Session.query(User).filter(User.id > 1 ).all()
print (data)

print('----------------查询id大于 1 小于 4 的数据')
data=Session.query(User).filter(User.id > 1 ).filter(User.id < 4).all()
print (data)

print('----------------查询id不等于 1 4 的数据')
data=Session.query(User).filter(User.id != 1 ).filter(User.id != 4).all()
print (data)

#查询到你要修改的这个数据，然后想修改面向对象里的数据一样，对数据进行修改，最后commit（）
data=Session.query(User).filter(User.id == 4).first()
print(data)
data.name = "Jack Chen4"
data.password = "555555"
Session.commit()

# 删除数据
#data = Session.query(User).filter_by(name = 'Hello').first()
#Session.delete(data)
#Session.commit()


fake_user = User(name = 'Rain',password = "123456")
Session.add(fake_user)
Session.commit()


