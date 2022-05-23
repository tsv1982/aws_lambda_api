import json
import boto3
from flask_lambda import FlaskLambda
from flask import request

app = FlaskLambda(__name__)
ddb = boto3.resource('dynamodb')
table = ddb.Table('car_table04')

@app.route('/car/<id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def get_patch_delete_car(id):
    key = {'id': id}
    if request.method == 'GET':
  
       if id == "all":
          return get_item_all()
       return get_item(key)

    elif request.method == 'PUT':
       return update_item(key)

    elif request.method == "DELETE":
       return delete_item(key)

    elif request.method == 'POST':
       return add_item()

def get_item(key):
    car = table.get_item(Key=key).get('Item')
    if car:
        return myJson(car, 200)
    else:
        return myJson({"message": "car not found"}, 404)

def get_item_all():
    car = table.scan()['Items']
    return myJson(car, 200)

def add_item():
    table.put_item(Item=request.form.to_dict())
    return myJson({"message": "car add"}, 200) 

def update_item(key):
    attribute_updates = {key: {'Value': value, 'Action': 'PUT'} for key, value in request.form.items()}
    table.update_item(Key=key, AttributeUpdates=attribute_updates)
    return myJson({"message": "car update"}, 200) 

def delete_item(key):
    table.delete_item(Key=key)
    return myJson({"message": "car delete"}, 200) 

def myJson(data, status):
    return (json.dumps(data), status, {'Content-Type': "application/json"})

