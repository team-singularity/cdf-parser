class SolarWind:
    def __init__(self, time, bulkspeed, iontemperature, isgood, templevel):
        self.time = time
        self.bulkSpeed = bulkspeed
        self.ionTemperature = iontemperature
        self.isGood = isgood
        self.tempLevel = templevel

    def __str__(self):
        return f"Speed: {self.time}, Density: {self.bulkSpeed}, ionTemperature: {self.ionTemperature}"