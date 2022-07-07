import random 

def get_temperature(min_value,max_value,no_of_samples):
    temperature_in_c=generate_samples(min_value,max_value,no_of_samples)
    message= formate_message('Temperature', temperature_in_c)
    return display_readings(message)
  
    
def generate_samples(min_value,max_value,no_of_samples):
    result=random.sample(range(min_value, max_value),no_of_samples)
    return result
  
def get_charge_rate(min_value,max_value,no_of_samples):
    charge_rate=generate_samples(min_value,max_value,no_of_samples)
    message= formate_message('Charge Rate', charge_rate)
    return display_readings(message)
  
  
def display_readings(message):
    return message
  
def formate_message(attribute,readings):
    return "The {} readings- {}".format(attribute,readings)  
  
  
