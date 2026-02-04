from dataclasses import dataclass


# later redo for a robot theme
@dataclass
class Pet:
    name: str
    data: int = 100
    energy: int = 100
    mood: int = 100
    health: int = 100
