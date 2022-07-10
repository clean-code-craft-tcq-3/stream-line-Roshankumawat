import random 
import json

def get_temperature_in_C(min_value,max_value,no_of_samples):
    return generate_samples(min_value,max_value,no_of_samples)

def celcious_to_farenheit_convertor(temp):
    return round((temp * 1.8) + 32,2)
     
def generate_samples(min_value,max_value,no_of_samples):
    return random.sample(range(min_value, max_value),no_of_samples)
  
def get_charge_rate(min_value,max_value,no_of_samples):
    return generate_samples(min_value,max_value,no_of_samples)

def process_data(temp_in_c, charge_rate):
    data= {}
    data.update({"Charge Rate" : charge_rate})
    data.update({"Temperature" : temp_in_c})
    return json.dumps(data)
  
def display_readings(message):
    print( message)
  
def formate_message(attribute,readings):
    return "The {} readings- {}".format(attribute,readings)  
  
  
