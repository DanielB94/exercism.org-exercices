class SpaceAge:
    def __init__(self, seconds: int | float) -> None:
        self.seconds = seconds
    
    EARTH_CONSTANT = 31557600
    ORBITALS = {
    'earth': 1.0,
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132,
}

    def age_math(self, planet: str) -> float:
        return round(self.seconds / (self.EARTH_CONSTANT * self.ORBITALS[planet]), 2)

    def on_earth(self) -> float:
        return self.age_math('earth')

    def on_mercury(self) -> float:
        return self.age_math('mercury')

    def on_venus(self) -> float:
        return self.age_math('venus')

    def on_mars(self) -> float:
        return self.age_math('mars')
    
    def on_jupiter(self) -> float:
        return self.age_math('jupiter')

    def on_saturn(self) -> float:
        return self.age_math('saturn')
    
    def on_uranus(self) -> float:
        return self.age_math('uranus')

    def on_neptune(self) -> float:
        return self.age_math('neptune')
