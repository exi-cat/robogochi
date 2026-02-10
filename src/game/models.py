import time
from dataclasses import dataclass


# later redo for a robot theme
@dataclass
class Pet:
    name: str
    last_tick: float = time.time()
    data: int = 100
    energy: int = 100
    mood: int = 100
    # redo into structure for body health and something like software health, e.g. data integrity
    health: int = 100
