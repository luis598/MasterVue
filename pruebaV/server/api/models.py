from api import db
from api import ma 
from marshmallow import fields

class User(db.Model):
  __tablename__='users'

  rewards= db.relationship('Reward', backref='rewards', lazy=True)
  id = db.Column(db.Integer, primary_key= True)
  name = db.Column(db.String(50))

class Reward(db.Model):
  __tablename__= 'rewards'
  id = db.Column(db.Integer, primary_key=True)
  reward_name = db.Column(db.String(250))
  user_id= db.Column(db.Integer, db.ForeignKey('users.id'))



class UserSchema(ma.SQLAlchemyAutoSchema):
  
  id = fields.Int()
  name= fields.Str()
  rewards= fields.Nested('RewardSchema', many=True)
    
class RewardSchema(ma.SQLAlchemyAutoSchema):

  class Meta:
    model = Reward
    load_data=True

