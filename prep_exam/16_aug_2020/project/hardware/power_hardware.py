from project.hardware.hardware import Hardware
from math import floor


class PowerHardware(Hardware):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        super().__init__(name, hardware_type, capacity, memory)
        self.name = name
        self.hardware_type = 'Power'
        self.capacity = floor(capacity * 0.25)
        self.memory = floor(memory * 1.75)
