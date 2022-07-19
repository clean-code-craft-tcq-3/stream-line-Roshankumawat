import Sender
import unittest
import json
import os

class sender_test(unittest.TestCase):
  
  def test_generate_samples(self):
    self.assertTrue(Sender.generate_samples(10,80) in range(10,80))

  def test_celcious_to_farenheit_convertor(self):
    self.assertTrue(Sender.celcious_to_farenheit_convertor(50)==122.0)
  
  def test_get_temperature_in_C(self):
    self.assertTrue( Sender.get_temperature_in_C() in range (0, 60))
      
  def test_get_charge_rate(self):
    self.assertTrue(Sender.get_charge_rate() in range (20, 80))
            
  def test_stream_data(self):
    self.assertTrue(Sender.stream_data(1) == "No of Streams Completed = 1")
  
  def test_main(self):
    result = os.system("python Sender.py")
    self.assertEqual(result, 0)
 
  def test_process_data(self):
    self.assertTrue(Sender.process_data(30, 1.0)==json.dumps({"Temperature":86.0,"Charge Rate":1.0}))
 
 
if __name__ == '__main__':
  unittest.main()
