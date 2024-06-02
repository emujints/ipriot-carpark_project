from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json
class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 log_file = 'log.txt',
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
    @property
    def available_bays(self):
        # car park available bays
        return max(0, self.capacity - len(self.plates))

    def __str__(self):
        return f"Welcome to {self.location} car park"

    def register(self, component):
        if not isinstance(component, Sensor):
            raise TypeError("Invalid component type!")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def _log_car(self, action, plate):
        with self.log_file.open(mode='a') as file:
            file.write(f'{plate} {action} on the {datetime.now().strftime("%d-%m %H:%M")}\n')

    def add_car(self, plate):
        self.plates.append(plate)
        self._log_car("entered", plate)

    def remove_car(self, plate):
        self.plates.remove(plate)
        self._log_car("exited", plate)

    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 40,
                            "News": "something happened"})
            print(f"Updating: {display}")


