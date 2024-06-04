import unittest
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from pathlib import Path
from display import Display
class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        with self.car_park.log_file.open('w'):
            pass
    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))
    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)


    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_register_sensor(self):
        sensor = EntrySensor(id = 1, car_park = self.car_park)
        self.car_park.register(sensor)
        self.assertIn(sensor, self.car_park.sensors)

    def test_register_exit_sensor(self):
        exit_sensor = ExitSensor(id = 1, car_park=self.car_park)
        self.car_park.register(exit_sensor)
        self.assertIn(exit_sensor, self.car_park.sensors)

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    def tearDown(self):
        Path("new_log.txt").unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
        new_carpark.add_car("NEW-001")
        with new_carpark.log_file.open() as f:
            lines = f.readlines()
            self.assertTrue(lines)
            last_line = lines[-1].strip()
            self.assertIn("NEW-001 entered", last_line)

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
        new_carpark.add_car("NEW-001")
        new_carpark.remove_car("NEW-001")
        with new_carpark.log_file.open() as f:
            lines = f.readlines()
            self.assertTrue(lines)
            last_line = lines[-1].strip()
            self.assertIn("NEW-001 exited", last_line)

        with self.car_park.log_file.open('w'):
            pass


if __name__ == "__main__":
    unittest.main()
