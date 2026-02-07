from typing import Dict, Optional
from src.game.models import Pet
from src.game.actions import Pet, feed, play

_pets_by_user: Dict[int, Pet] = {}


def get_pet(user_id: int) -> Optional[Pet]:
    return _pets_by_user.get(user_id)


def create_pet(user_id: int, name: str = "Robogochi") -> Pet:
    pet = Pet(name=name)
    _pets_by_user[user_id] = pet
    print("DEBUG pets: ", _pets_by_user)
    return pet


def feed_pet(user_id: int) -> Optional[Pet]:
    pet = get_pet(user_id)
    if pet is None:
        return None

    return feed(pet)


def play_pet(user_id: int) -> Optional[Pet]:
    pet = get_pet(user_id)
    if pet is None:
        return None

    return play(pet)
