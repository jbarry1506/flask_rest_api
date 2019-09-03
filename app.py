from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'Superstore',
        'items':  [
            {
                'name': 'My Item',
                'price': 15.99
            }
    }
]

# create a POST store
@app.route('/store', methods=['POST'])
def create_store():
    pass
    

# GET single store
@app.route('/store/<string:name>')
def get_store(name):
    pass
    

# GET all stores
@app.route('/store')
def get_stores():
    return jsonify(stores)
    
    
# POST item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass
    
    
# GET item
@app.route('/store/<string:storename>/item/<string:itemname>')
def get_item(storename, itemname):
    pass
    

# GET all items from one store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass
    
