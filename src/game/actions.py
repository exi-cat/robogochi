from src.game.models import Pet


def clamp(value: int, min_value: int = 0, max_value: int = 100):
    return max(min_value, min(max_value, value))


def feed(pet: Pet) -> Pet:
    """Robogochi 'eats' data packets."""
    pet.data = clamp(pet.data + 25)
    pet.energy = clamp(pet.energy - 5)
    pet.mood = clamp(pet.mood + 2)
    return pet
