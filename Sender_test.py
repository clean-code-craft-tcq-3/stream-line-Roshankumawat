import Sender


def test_generate_samples(min_value, max_value, no_of_samples):
  # Expected no of samples and detected no of samples shall be same
  samples= Sender.generate_samples(min_value, max_value, no_of_samples)
  samples_length= len(samples)
  assert(samples_length==no_of_samples)
  
  
if __name__ == '__main__':
  test_generate_samples(0, 40, 20)
  test_generate_samples(0, 40, 40)
  
