import Sender
import unittest

class sender_test(unittest.TestCase):
  
  def test_generate_samples(self):
    # Expected no of samples and detected no of samples shall be same
    expected_samples= 30
    samples= Sender.generate_samples(10,50, 30)
    samples_length= len(samples)
    assert(samples_length==expected_samples)
  
  def test_celcious_to_farenheit_convertor(self):
    self.assertTrue(Sender.celcious_to_farenheit_convertor(50)==122)
  
  def test_get_temperature_in_C(self):
    samples= Sender.get_temperature_in_C(0, 70, 50)
    for sample in samples:
        self.assertTrue(sample in range (0, 70))
  
  def test_get_charge_rate(self):
    samples= Sender.get_charge_rate(0, 80, 50)
    for sample in samples:
        self.assertTrue(sample in range (0, 80))
        
  def test_display_readings(self):
    self.assertTrue(Sender.display_readings('Temperature is 50')=='Temperature is 50')
    
  def test_formate_message(self):
    self.assertTrue(Sender.formate_message('Temperatue', 30)=='Temperature is 30')
 
 
if __name__ == '__main__':
  unittest.main()
