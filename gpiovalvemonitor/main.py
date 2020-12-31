from gpiozero import SmoothedInputDevice
import json


class ValveSensor(SmoothedInputDevice):
    def __init__(self, pin=None, pull_up=False):
        super(ValveSensor, self).__init__(pin, pull_up=pull_up, sample_wait=1 / 100, average=max)
        self._queue.start()


class SensorConfiguration(dict):
    def __init__(self, pin, octocoupler_port, pull_up, roth_channel, zone):
        dict.__init__(self,
                      pin=pin,
                      octocoupler_port=octocoupler_port,
                      pull_up=pull_up,
                      roth_channel=roth_channel,
                      zone=zone)


sensors_matrix = [
    SensorConfiguration(17, 'L8', False, 1, 'Förråd'),
    SensorConfiguration(27, 'L7', False, 2, 'Sovrum'),
    SensorConfiguration(22, 'L6', False, 3, 'Gästrum'),
    SensorConfiguration(5, 'L5', False, 4, 'Bibliotek'),
    SensorConfiguration(6, 'L4', False, 5, 'Vardagsrum'),
    SensorConfiguration(26, 'L3', False, 5, 'Vardagsrum'),
    SensorConfiguration(23, 'L2', False, 6, 'Tambur / WC'),
    SensorConfiguration(24, 'L1', False, 7, 'Arbetsrum'),
    SensorConfiguration(25, 'R4', True, 8, 'Kök'),
    SensorConfiguration(16, 'R3', True, 9, 'Hjälpkök'),
]

for sensor_configuration in sensors_matrix:
    sensor = ValveSensor(pin=sensor_configuration['pin'], pull_up=sensor_configuration['pull_up'])
    sensor_configuration['state'] = sensor.value

print(json.dumps(sensors_matrix))
