import Sender


def test_generate_samples(min_value, max_value, no_of_samples):
  # Expected no of samples and detected no of samples shall be same
  samples= Sender.generate_samples(min_value, max_value, no_of_samples)
  samples_length= len(samples)
  assert(samples_length==no_of_samples)
  
def test_celcious_to_farenheit_convertor():
  assertTrue(Sender.celcious_to_farenheit_convertor(50)==122)
  
def test_get_temperature_in_C():
  assertTrue(Sender.get_temperature_in_C(10, 50, 50) in range (10, 50))
  
def test_get_charge_rate():
  assertTrue(Sender.get_charge_rate(0, 50, 50) in range(0, 50)) 
 
  
if __name__ == '__main__':
  test_generate_samples(0, 40, 20)
  test_generate_samples(-10, 40, 40)
  test_get_charge_rate()
  test_get_temperature_in_C()
  assert(Sender.formate_message('Temperature', [10,20,30])=='The Temperature readings- [10, 20, 30]')
  assert(Sender.display_readings('The Temperature readings- [10, 20, 30]')=='The Temperature readings- [10, 20, 30]')
