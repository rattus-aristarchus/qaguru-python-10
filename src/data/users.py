import dataclasses

@dataclasses.dataclass
class User:
    name: str
    last_name: str
    email: str
    gender: str
    number: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    date_of_birth: str
    subject_0: str
    subject_1: str
    hobby_0: str
    hobby_1: str
    hobbies: str
    address: str
    state: str
    city: str


test_user = User(
    name="test_name",
    last_name="test_last_name",
    email="test@gmail.com",
    gender="Female",
    number="0123456789",
    day_of_birth="1",
    month_of_birth="January",
    year_of_birth="1942",
    date_of_birth="01 January,1942",
    subject_0="History",
    subject_1="Maths",
    hobby_0="Reading",
    hobby_1="Music",
    hobbies="Reading, Music",
    address="Some-street, Some-house, Some-apartment",
    state="Haryana",
    city="Panipat"
)