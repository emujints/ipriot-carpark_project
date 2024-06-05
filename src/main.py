from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

#creating a car park
car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")

#creating sensors
entry_sensor = EntrySensor(id= 1, is_active=True, car_park=car_park)
exit_sensor = ExitSensor(id= 2, is_active=True, car_park=car_park)




