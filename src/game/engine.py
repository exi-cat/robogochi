from src.game.models import Pet
from src.game.actions import clamp


def apply_tick(pet: Pet, now: float = 0.1) -> Pet:
    pet.energy = clamp(pet.energy - 5)
    pet.data = clamp(pet.data - 7)
    pet.mood = clamp(pet.mood - 4)
    pet.health = clamp(pet.health - 1)
    pet.last_tick = now
    return pet
