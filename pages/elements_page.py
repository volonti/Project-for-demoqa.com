from generator.generator import generated_person
from locators.locators_text_box import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        email = person_info.email
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        current_address = person_info.current_address
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.hide_ads()
        self.element_is_clickable(self.locators.BUTTON).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        created_full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        created_email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        created_current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        created_permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return created_full_name, created_email, created_current_address, created_permanent_address








