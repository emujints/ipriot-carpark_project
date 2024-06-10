import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class Test_Sensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
    def test_register_sensor(self):
        entry_sensor = EntrySensor(id = 1, car_park = self.car_park)
        self.car_park.register(entry_sensor)
        self.assertIn(entry_sensor, self.car_park.sensors)


    def test_register_exit_sensor(self):
        exit_sensor = ExitSensor(id = 1, car_park=self.car_park)
        self.car_park.register(exit_sensor)
        self.assertIn(exit_sensor, self.car_park.sensors)