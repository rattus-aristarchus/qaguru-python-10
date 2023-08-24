from src.pages.registration_page import RegistrationPage
from src.data import users


def test_practice_form(setup_browser):
    page = RegistrationPage()
    test_user = users.test_user

    page.open()
    page.set_name(test_user.name)
    page.set_last_name(test_user.last_name)
    page.set_email(test_user.email)

    # fill in the basic stuff

    page.set_gender(test_user.gender)
    page.set_number(test_user.number)
    page.set_birthday(test_user.year_of_birth, test_user.month_of_birth, test_user.day_of_birth)

    # fill in the hobbies
    page.add_interest(test_user.subjects[0])
    page.add_interest(test_user.subjects[1])
    page.add_hobby(test_user.hobbies[0])
    page.add_hobby(test_user.hobbies[1])

    # fill in the full address
    page.set_address(test_user.address)
    page.set_state(test_user.state)
    page.set_city(test_user.city)

    page.submit()

    # now, check it all
    page.should_register_user_with(test_user.name,
                                   test_user.last_name,
                                   test_user.email,
                                   test_user.gender,
                                   test_user.number,
                                   test_user.date_of_birth,
                                   test_user.subjects_str,
                                   test_user.hobbies_str,
                                   test_user.address,
                                   test_user.state,
                                   test_user.city)
