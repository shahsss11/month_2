class Distance:
    conversion_dict = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }
    
    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)
    
    def __init__(self, value, unit):
        if unit not in Distance.conversion_dict:
            raise ValueError("Неизвестная единица измерения")
        self.value = value
        self.unit = unit
    
    def __str__(self):
        return f"{self.value} {self.unit}"
        
    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно складывать только Distance")

        total_meters = self.convert() + other.convert()
        
        new_value = total_meters / Distance.conversion_dict[self.unit]
        return Distance(new_value, self.unit)
    
d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(50, "cm")

print(d1)
print(d2)

print(d1 + d2)
print(d2 + d1) 
print(d1 + d3) 