import json
import requests

url = "https://zv8l5i3i9k.execute-api.eu-central-1.amazonaws.com/Prod/"

def get_all_car(url):
    response =  requests.get(f"{url}/car/all")
    my_print(response, "")

def get_id_car(url, id):
    response =  requests.get(f"{url}/car/{id}")
    json_response = response.json()
    my_print(response, "")
    return response

def add_car(url, id, model):
    response =  requests.post(f"{url}/car/0", data = {'id': {id}, 'model': {model}})
    json_response = response.json()
    my_print(response, "message")

def delete_car(url, id):
    response = requests.delete(f"{url}/car/{id}")
    json_response = response.json()
    my_print(response, "message")

def update_car(url, id, model):
    response = requests.put(f"{url}/car/{id}", data = {'model': {model}})
    my_print(response, "message")

def my_print(response, mes):
    json_response = response.json()
    if mes == "message":
       json_response['message']
    print( json_response)
    print("---------------------")
    print(response)

def main(car_url):
    get_num = ""
    while get_num != "0":
      print(" 1. get all list\n 2. get car by id\n 3. add car\n 4. delete car\n 5. update car\n 0. exit")
      get_num = input("enter number ")
      if get_num == "1":
          get_all_car(car_url)
      elif get_num == "2":
          id = input("enter id ")
          get_id_car(car_url, id)
      elif get_num == "3":
          id = input ("enter id ")
          model = input ("enter model ")
          add_car(car_url, id, model)
          get_id_car(car_url, id)
      elif get_num == "4":
          id = input("enter id ")
          delete_car(car_url, id)
      elif get_num == "5":
          id = input ("enter id ")
          get_id_car(car_url, id)
          model = input ("enter model ")
          update_car(car_url, id, model)
          get_id_car(car_url, id)
      elif get_num == "0":
          return
      print("----------------------------")
      input("next enter y")

main(url)