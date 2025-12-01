class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, celsius: float):
        if celsius < -273.15:
            raise ValueError("Celsius must be >= -273.15")
        self._celsius = celsius

    @property
    def farenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32

    @farenheit.setter
    def farenheit(self, farenheit: float):
        if self.farenheit < (-459 - 2/3):
            raise ValueError("Farenheit must be above -459.67")
        self.celsius = (farenheit - 32) * 5 / 9

    @property
    def kelvin(self) -> float:
        return self.celsius + 273.15

    @kelvin.setter
    def kelvin(self, kelvin: float):
        if kelvin < 0:
            raise ValueError("Kelvin must be >= 0")
        self.celsius = (kelvin - 273.15)