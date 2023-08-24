import dataclasses
import datetime


@dataclasses.dataclass
class User:
    name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth: datetime.date
    subjects: list
    hobbies: list
    address: str
    state: str
    city: str

    @property
    def date_of_birth_str(self):
     #   if len(self.day_of_birth) < 2:
   #         day_string = "0" + self.day_of_birth
     #   else:
     #       day_string = self.day_of_birth

        return self.date_of_birth.strftime("%d %B,%Y")
      #  return datetime.strftime()
     #   return f"{day_string} {self.month_of_birth},{self.year_of_birth}"

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
    date_of_birth=datetime.date(1942, 1, 1),
    subjects=["History", "Maths"],
    hobbies=["Reading", "Music"],
    address="Some-street, Some-house, Some-apartment",
    state="Haryana",
    city="Panipat"
)