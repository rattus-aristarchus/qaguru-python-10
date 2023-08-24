from src.pages.registration_page import RegistrationPage
from src.data import users


def test_practice_form(setup_browser):
    page = RegistrationPage()
    page.open()
    page.register(users.test_user)
    page.should_have_user(users.test_user)
