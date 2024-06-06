from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

#creating a car park
car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")

#creating sensors
entry_sensor = EntrySensor(id= 1, is_active=True, car_park=car_park)
exit_sensor = ExitSensor(id= 2, is_active=True, car_park=car_park)

#registering sensors with car park
car_park.register(entry_sensor)
car_park.register(exit_sensor)

#creating display object
display = Display(id= 1, message = "Welcome to Moondalup", is_on=True, car_park=car_park)
car_park.register(display)

#detecting car entering
entry_sensor.detect_vehicle()

#updating display
car_park.update_displays()

#detecting car leaving
exit_sensor.detect_vehicle()

#updating display
car_park.update_displays()

# Drive 10 cars into the car park
for _ in range(10):
    entry_sensor.detect_vehicle()
    car_park.update_displays()

# Drive 2 cars out of the car park
for _ in range(2):
    exit_sensor.detect_vehicle()
    car_park.update_displays()
