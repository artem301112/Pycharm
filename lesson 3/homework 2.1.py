class Engine:
    def __init__(self, power):
        self.power = power

    def start_engine(self):
        print(f"Engine with power {self.power} started.")

    def stop_engine(self):
        print("Engine stopped.")

class Sensor:
    def __init__(self, sensitivity):
        self.sensitivity = sensitivity

    def detect(self):
        print(f"Sensor with sensitivity {self.sensitivity} is detecting.")

    def calibrate(self):
        print("Sensor calibrated.")

class Arm:
    def __init__(self, strength):
        self.strength = strength

    def lift(self, weight):
        if weight <= self.strength:
            print(f"Lifting {weight}kg.")
        else:
            print(f"Cannot lift {weight}kg. Strength is only {self.strength}kg.")

    def rotate(self, angle):
        print(f"Rotating arm by {angle} degrees.")

class Robot(Engine, Sensor, Arm):
    def __init__(self, power, sensitivity, strength):
        Engine.__init__(self, power)
        Sensor.__init__(self, sensitivity)
        Arm.__init__(self, strength)

    def perform_task(self, weight, angle):
        self.start_engine()
        self.detect()
        self.lift(weight)
        self.rotate(angle)
        self.stop_engine()


r2d2 = Robot(power=100, sensitivity=80, strength=50)
r2d2.perform_task(weight=30, angle=90)