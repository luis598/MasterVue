from flask import jsonify, Blueprint, request
from api import db
from api.models import User,UserSchema,RewardSchema, Reward

core = Blueprint('core', __name__)

@core.route('/usuarios', methods=['GET', 'POST'])
def index():
 if request.method == 'POST':
  post_data = request.get_json()
  user = User(name = post_data.get('name'))
  db.session.add(user)
  db.session.commit()
 
 
 users = User.query.all()
 rewards = Reward.query.all()
 user_schema = UserSchema(many=True)
 reward_schema= RewardSchema(many=True)
 output = user_schema.dump(users)
 output1= reward_schema.dump(rewards)
 return jsonify({'usuarios':output})
 #return jsonify(response_object)

@core.route('/usuarios/<int:usuario_id>', methods=['PUT', 'DELETE'])
def single_usuario(usuario_id):
 response_object = {'status': 'success'}
 if request.method == 'DELETE':
  usuario_remover = User.query.get_or_404(usuario_id)
  db.session.delete(usuario_remover)
  db.session.commit()
 if request.method == 'PUT':
  post_data= request.get_json()
  usuario_actualizar = User.query.get_or_404(usuario_id)
  usuario_actualizar.name = post_data.get('name')
  db.session.commit()

 return jsonify(response_object)

