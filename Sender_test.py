import Sender
import unittest
import json
import os

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
    samples= Sender.get_temperature_in_C()
    for sample in samples:
        self.assertTrue(sample in range (0, 60))
  
  def test_get_charge_rate(self):
    samples= Sender.get_charge_rate()
    for sample in samples:
        self.assertTrue(sample in range (20, 80))
        
  def test_stream_data(self):
    self.assertTrue(Sender.stream_data(1) == "No of Streams Completed = 1")
  
  def test_main(self):
    result = os.system("python Sender.py")
    self.assertEqual(result, 0)
 
  def test_process_data(self):
    self.assertTrue(Sender.process_data(30, 1.0)==json.dumps({"Temperature":86.0,"Charge Rate":1.0}))
 
 
if __name__ == '__main__':
  unittest.main()
