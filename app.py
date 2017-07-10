from flask import Flask, jsonify
from config import MONGO_URI, DB_NAME, COLL_NAME
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient(MONGO_URI)
db = client.get_database(DB_NAME)
coll = db.get_collection(COLL_NAME)

@app.route('/CAB/api/v1.0/decisions/', methods=['GET'])
def getAll()
	
	cur = coll.find({},{'_id':0})
	results = list(cur)
	count = len(results)
	return jsonify({'count':count, 'results':results})
	
@app.route('/CAB/api/v1.0/search/<queryString>', methods=['GET'])
def search(queryString):
	
	cur = coll.find({"$text" : {"$search" : queryString }}, {'_id':0})
	results = list(cur)
	count = len(results)
	return jsonify({'count':count, 'results':results})
	
if __name__ == '__main__':
	app.run(debug=True)