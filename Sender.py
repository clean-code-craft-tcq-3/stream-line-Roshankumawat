import random 
import json

def get_temperature_in_C():
    return generate_samples(0, 60, 50)

def celcious_to_farenheit_convertor(temp):
    return round((temp * 1.8) + 32,2)
     
def generate_samples(min_value,max_value,no_of_samples):
    return random.sample(range(min_value, max_value),no_of_samples)
  
def get_charge_rate():
    return generate_samples(20,80, 50)

def process_data(temp_in_c, charge_rate):
    data= {}
    data.update({"Temperature" : celcious_to_farenheit_convertor(temp_in_c)})
    data.update({"Charge Rate" : charge_rate})
    return json.dumps(data)
 
  
def stream_data(number):
    for i in range(number):
        print(process_data(get_temperature_in_C(), get_charge_rate()))
    return "No of Streams Completed = {}".format(number)
  
if __name__ == '__main__':
    stream_data(50)
    
