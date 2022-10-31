class SignalStatistic:
    def __init__(self):
        self.last_five_values_temp = []
        self.last_five_values_charge = []
        self.min_temp_value = self.min_charge_value = 999
        self.max_temp_value = self.max_charge_value = 0
        self.temp_avg = self.charge_avg = 'N/A'

    def update_moving_avg(self, new_temp_value, new_charge_value):
        self.last_five_values_temp.append(new_temp_value)
        self.last_five_values_charge.append(new_charge_value)
        if len(self.last_five_values_temp) > 5:
            self.last_five_values_temp.pop(0)     # remove item from front of queue
            self.last_five_values_charge.pop(0)

        self.temp_avg = sum(self.last_five_values_temp)/len(self.last_five_values_temp)
        self.charge_avg = sum(self.last_five_values_charge)/len(self.last_five_values_charge)

    def update_max_value(self, new_temp_value, new_charge_value):
        if new_temp_value > self.max_temp_value:
            self.max_temp_value = new_temp_value
        if new_charge_value > self.max_charge_value:
            self.max_charge_value = new_charge_value

    def update_min_value(self, new_temp_value, new_charge_value):
        if new_temp_value < self.min_temp_value:
            self.min_temp_value = new_temp_value
        if new_charge_value < self.min_charge_value:
            self.min_charge_value = new_charge_value


def derive_signal_values(sensor_signals):
    sensor_values = sensor_signals.split(', ')
    temperature_value = sensor_values[0].split(': ')[-1]
    charge_value = sensor_values[1].split(': ')[-1][:-1]
    return float(temperature_value), int(charge_value)


def process_input_signal(sensor_signals, signal_statistic):
    temperature_value, charge_value = derive_signal_values(sensor_signals)
    signal_statistic.update_moving_avg(temperature_value, charge_value)
    signal_statistic.update_min_value(temperature_value, charge_value)
    signal_statistic.update_max_value(temperature_value, charge_value)


def print_signal_statistics(input_from_sender, signal_statistics):
    print("------------------------------------------------------------------------")
    print("New Signal from sender - " + input_from_sender)
    print(f"Moving temperature avg = {round(signal_statistics.temp_avg, 2)}")
    print(f"Moving charge avg = {signal_statistics.charge_avg}")
    print(f"Max temp = {signal_statistics.max_temp_value}")
    print(f"Min temp = {signal_statistics.min_temp_value}")
    print(f"Max charge = {signal_statistics.max_charge_value}")
    print(f"Min charge = {signal_statistics.min_charge_value}")

    
    

if __name__ == '__main__':
    signal_stat = SignalStatistic()
    while True:
        try:
            input_signal = input()
        except EOFError:
            break
        process_input_signal(input_signal, signal_stat)
        print_signal_statistics(input_signal, signal_stat)
