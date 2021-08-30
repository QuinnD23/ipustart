from aiogram.dispatcher.filters.state import StatesGroup, State


class StateMachine(StatesGroup):
    Start = State()

    ClothesSelect = State()

    ColourSelect = State()

    CheckLevel = State()

    EnterLevel = State()

    CheckPhoto = State()

    EnterPlace = State()
    CheckPlace = State()

    EnterName = State()
    CheckName = State()

    Finally = State()

    Admin = State()
    CheckAdmin = State()
    SendAdmin = State()