from selene import browser, have, command
from selenium import webdriver


class RegistrationPage:

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def set_name(self, name):
        browser.element("#firstName").type(name)

    def set_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def set_gender(self, gender):
        if gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        elif gender == "Male":
            browser.element('[for="gender-radio-1"]').click()

    def set_number(self, number):
        browser.element("#userNumber").type(number)

    def set_email(self, email):
        browser.element("#userEmail").type(email)

    def set_birthday(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(
            f".react-datepicker__day.react-datepicker__day--00{day}"
        ).click()

    def add_interest(self, subject):
        browser.element("#subjectsInput").type(subject).press_enter()

    def add_hobby(self, hobby):
        if hobby == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif hobby == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').click()
        elif hobby == "Music":
            browser.element('[for="hobbies-checkbox-3"]').click()

    def set_address(self, address):
        browser.element("#currentAddress").type(address)

    def set_state(self, state):
        browser.element("#react-select-3-input").type(state).press_enter()

    def set_city(self, city):
        browser.element("#react-select-4-input").type(city).press_enter()

    def should_register_user_with(self, *args):
        for arg in args:
            browser.element(".table").should(have.text(arg))

    def submit(self):
        browser.element("#submit").press_enter()
