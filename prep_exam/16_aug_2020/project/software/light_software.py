from project.software.software import Software
from math import floor


class LightSoftware(Software):
    def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.name = name
        self.software_type = "Light"
        self.capacity_consumption = floor(capacity_consumption * 1.5)
        self.memory_consumption = floor(memory_consumption * 0.5)
