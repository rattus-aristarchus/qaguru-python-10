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
    subjects: list
    hobbies: list
    address: str
    state: str
    city: str

    @property
    def date_of_birth(self):
        if len(self.day_of_birth) < 2:
            day_string = "0" + self.day_of_birth
        else:
            day_string = self.day_of_birth
        return f"{day_string} {self.month_of_birth},{self.year_of_birth}"

    @property
    def subjects_str(self):
        return ", ".join(self.subjects)

    @property
    def hobbies_str(self):
        return ", ".join(self.hobbies)


test_user = User(
    name="test_name",
    last_name="test_last_name",
    email="test@gmail.com",
    gender="Female",
    number="0123456789",
    day_of_birth="1",
    month_of_birth="January",
    year_of_birth="1942",
    subjects=["History", "Maths"],
    hobbies=["Reading", "Music"],
    address="Some-street, Some-house, Some-apartment",
    state="Haryana",
    city="Panipat"
)