from flask import Flask, jsonify, request, render_template

app= Flask(__name__)

stores = [
{
'name': 'My Wonderful Store',
'items': [
	{
	'name': 'My item',
	'price': '77'
	}
		]
}
]

@app.route('/')
def home():
	return render_template('index.html')
#post - used to receive data

#get - used to send data back only

#post /store data: {name:}
@app.route('/store' , methods=['POST'])
def create_store():
	request_data = request.get_json()

	new_store = {
	'name':request_data['name']
	}
	stores.append(new_store)
	return jsonify(new_store)

#get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	#iterate over stores
	#if the store name matches , return it
	#if none match, return a error message

	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return jsonify({'message': 'store not found'})

#get /store
@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})

#post /store/<string:name>/item {name: , price:}
@app.route('/store/<string:name>/item', methods=['POST','GET'])
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
			'name': request_data['name'],
			'price': request_data['price']
				}
			store['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message': 'store not found' })

#get /store/<string:name>/item
@app.route('/store/<string:name>/items', methods=['GET'])
def get_item_in_store(name):
	for store in stores:
		if store['name']==name:
			return jsonify({'items': store['items']})
	return jsonify({'message': 'store not found'})



app.run(port=5000)

#    for store in stores:
#		if store['name'] == name:
#			return jsonify({'items': store['items']})
#	return jsonify({'message': 'store not found'})
