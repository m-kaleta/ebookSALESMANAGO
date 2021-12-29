from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import locators

class InitialSteps:
    def __init__(self, driver):
        self.driver = driver

    # locators to complete the form
        self.fill_name = locators.FillFields.input_name
        self.fill_email = locators.FillFields.input_email
        self.fill_company = locators.FillFields.input_company
        self.fill_phone = locators.FillFields.input_phoneNumber
        self.fill_url = locators.FillFields.input_url
        self.button_download = locators.FillFields.download_button

    # hovers over the menu and select EBOOK
    def firstSteps(self, driver):
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//li[4]"))
        menu_salesmanago = driver.find_element(By.XPATH, "//ul[@id='menu-list']/li[4]")
        webdriver.ActionChains(driver).move_to_element(menu_salesmanago).perform()
        driver.find_element(By.XPATH, "//ul[@id='menu-list']/li[4]/div/div/div[1]/div/ul/a[1]").click()

    # completes the form fields
    def fill_in(self, name, email, comapny, phone, url):
        self.driver.find_element(*self.fill_name).send_keys(name)
        self.driver.find_element(*self.fill_email).send_keys(email)
        self.driver.find_element(*self.fill_company).send_keys(comapny)
        self.driver.find_element(*self.fill_phone).send_keys(phone)
        self.driver.find_element(*self.fill_url).send_keys(url)

    # download button
    def click_download_button(self, driver):
        self.driver.find_element(*self.button_download).click()