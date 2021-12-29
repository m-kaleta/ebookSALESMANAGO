from selenium.webdriver.common.by import By

class FillFields:

    # completes the form fields
    input_name = (By.NAME, "name")
    input_email = (By.NAME, "email")
    input_company = (By.NAME, "company")
    input_phoneNumber = (By.ID, "phoneNumber")
    input_url = (By.NAME, "url")

    # download button
    download_button = (By.XPATH, '//button[contains(text(),"Pobierz eBooka")]')