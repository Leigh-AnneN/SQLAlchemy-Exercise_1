"""Seed file to make sample data for db"""

from models import User, Post, Tag, PostTag, db
from app import app

#Create all tables

db.drop_all()
db.create_all()

u1 = User(first_name="Bono", last_name="Adams", image_url="https://variety.com/wp-content/uploads/2021/12/Bono-Sing-2-Music-for-Screens.jpg?w=1000")
u2 = User(first_name="Sheryl", last_name="Crow", image_url="https://i.guim.co.uk/img/media/4648cdd96a680b584091e06961ea876190f829ea/0_142_2523_1514/master/2523.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=7578bbc323f92ff7a3f4619a45b89a55")
u3 = User(first_name="Gracie", last_name="May", image_url="https://assets-au-01.kc-usercontent.com/a74cc67d-6861-022b-4d6d-57679e9d331f/eef5fc42-285b-446c-9f2f-80e5984e7fec/e2f9c36b-86d6-4216-802a-978da6f8e8cc.jpg")

p1 = Post(title ="First Post", content="Hello, this is the first post, nice to meet you", user_id="1")
p2 = Post(title ="Hello World", content="Learning SQLAlchemy is awesome", user_id="1")
p3 = Post(title ="All I want to do", content="All I want to do is have some fun", user_id="2")
p4 = Post(title ="And send it soaring!", content="Let's go ride a kite, up to the highest height", user_id="3")

t1= Tag(name="music")

pt1=PostTag(post_id="3", tag_id="1")

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.commit()

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.commit()

db.session.add(t1)
db.session.commit()

db.session.add(pt1)
db.session.commit()