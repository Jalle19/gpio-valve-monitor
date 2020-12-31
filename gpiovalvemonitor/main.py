from gpiozero import SmoothedInputDevice
import json


class ValveSensor(SmoothedInputDevice):
    def __init__(self, pin=None):
        super(ValveSensor, self).__init__(pin, sample_wait=1 / 100, average=max)
        self._queue.start()


class SensorConfiguration(dict):
    def __init__(self, pin, octocoupler_port, roth_channel, zone):
        dict.__init__(self,
                      pin=pin,
                      octocoupler_port=octocoupler_port,
                      roth_channel=roth_channel,
                      zone=zone)


sensors_matrix = [
    SensorConfiguration(17, 'L8', 1, 'Förråd'),
    SensorConfiguration(27, 'L7', 2, 'Sovrum'),
    SensorConfiguration(22, 'L6', 3, 'Gästrum'),
    SensorConfiguration(5, 'L5', 4, 'Bibliotek'),
    SensorConfiguration(6, 'L4', 5, 'Vardagsrum'),
    SensorConfiguration(26, 'L3', 5, 'Vardagsrum'),
    SensorConfiguration(23, 'L2', 6, 'Tambur / WC'),
    SensorConfiguration(24, 'L1', 7, 'Arbetsrum'),
    SensorConfiguration(25, 'R4', 8, 'Kök'),
    SensorConfiguration(16, 'R3', 9, 'Hjälpkök'),
]

for sensor_configuration in sensors_matrix:
    sensor = ValveSensor(pin=sensor_configuration['pin'])
    sensor_configuration['state'] = sensor.value

print(json.dumps(sensors_matrix))
