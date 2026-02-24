class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element("id", "user-name").send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        self.driver.find_element("id", "login-button").click()