from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.game.service import get_pet, create_pet, feed_pet, play_pet

router = Router()


async def reply(message: Message, text: str):
    await message.answer(text)


def get_user_id(message: Message) -> int | None:
    if message.from_user is None:
        return None
    return message.from_user.id


@router.message(Command("start"))
async def start_handler(message: Message):
    user_id = get_user_id(message)
    if user_id is None:
        return
    pet = get_pet(user_id)

    if pet is None:
        pet = create_pet(user_id)
        await reply(message, f"So let`s begin. Just created your pet: {pet.name}")
    else:
        await reply(
            message,
            f"Don`t need to start. You already have a pet! His name is {pet.name}",
        )


@router.message(Command("status"))
async def status_handler(message: Message):
    user_id = get_user_id(message)
    if user_id is None:
        return
    pet = get_pet(user_id)

    if pet is None:
        await reply(
            message,
            "You don`t own a pet at the moment. Created one with the command /start",
        )
        return
    await reply(
        message,
        f"{pet.name}\n"
        f"Data Hunger: {pet.data}\n"
        f"Energy: {pet.energy}\n"
        f"Mood: {pet.mood}\n"
        f"Health: {pet.health}\n",
    )


# check what will be if no used_id passed
@router.message(Command("feed"))
async def feed(message: Message):
    user_id = get_user_id(message)
    if user_id is None:
        return
    pet = feed_pet(user_id)
    if pet is None:
        await reply(message, "No Robogochi detected. Create one usinf /start command")
        return

    await reply(message, "Informaition received. Data hunger level lowers")


@router.message(Command("play"))
async def play(message: Message):
    user_id = get_user_id(message)
    if user_id is None:
        return
    pet = play_pet(user_id)
    if pet is None:
        await reply(message, "No Robogochi detected. Create one usinf /start command")
        return

    await reply(message, "Interaction succesfull. Neuron processes stimulated")
