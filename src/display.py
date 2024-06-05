class Display:
    def __init__(self,
                 id,
                 car_park,
                 message = "",
                 is_on = False,
                 ):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
            print(f"{key}: {value}")

    def __str__(self):
        return f"{self.id}: , {self.message}, Display is {'is on' if self.is_on else 'if off'}"
