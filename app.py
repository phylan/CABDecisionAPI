from flask import Flask, jsonify, request, make_response, abort
from config import MONGO_URI, MONGO_PORT, DB_NAME, COLL_NAME
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient(MONGO_URI, int(MONGO_PORT))
db = client.get_database(DB_NAME)
coll = db.get_collection(COLL_NAME)

@app.route('/api/v1.0/decisions', methods=['GET'])
def getAll():
	
	cur = coll.find({},{'_id':0})
	results = list(cur)
	count = len(results)
	return jsonify({'count':count, 'results':results})
	
@app.route('/api/v1.0/search/<queryString>', methods=['GET'])
def search(queryString):
	
	cur = coll.find({"$text" : {"$search" : queryString }}, {'_id':0})
	results = list(cur)
	count = len(results)
	return jsonify({'count':count, 'results':results})
	
@app.route('/api/v1.0/decisions', methods=['POST'])
def addDecision():
	
	try:
		newDecision = request.get_json()
	except:
		abort(400)
	
	if newDecision == None:
		abort(400)
	
	try:
		coll.insert_one(newDecision)
		return jsonify({'decision' : newDecision}), 201	
		
	except:
		abort(400)

@app.errorhandler(404)
def not_found(error):
	
	return make_response(jsonify({'error':'Not Found'}), 404)
	
if __name__ == '__main__':
	app.run(debug=True)