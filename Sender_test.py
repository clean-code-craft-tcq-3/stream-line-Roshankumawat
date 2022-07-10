import Sender
import unittest

class sender_test(unittest.TestCase):
  
  def test_generate_samples(self, min_value, max_value, no_of_samples):
    # Expected no of samples and detected no of samples shall be same
    samples= Sender.generate_samples(self.min_value, self.max_value, self.no_of_samples)
    samples_length= len(samples)
    assert(samples_length==no_of_samples)
  
  def test_celcious_to_farenheit_convertor(self):
    self.assertTrue(Sender.celcious_to_farenheit_convertor(50)==122)
  
  def test_get_temperature_in_C():
    self.assertTrue(Sender.get_temperature_in_C(10, 50, 50) in range (10, 50))
  
  def test_get_charge_rate():
    self.assertTrue(Sender.get_charge_rate(0, 50, 50) in range(0, 50)) 
  

 
  
if __name__ == '__main__':
  unittest.main()
