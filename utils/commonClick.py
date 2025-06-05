from playwright.sync_api import Page, TimeoutError

class commonClick:
    def __init__(self, page):
        self.page = page
        
    def click_by_id(self, element_id):
        try:
            self.page.click(f"#{element_id}")
        except TimeoutError:
            print(f"Element with ID '{element_id}' not found or not clickable.")
            raise
        except Exception as e:
            print(f"An error occurred while clicking element with ID '{element_id}': {e}")
            raise

    def click_by_xpath(self, xpath):
        try:
            locator = self.page.locator(f"xpath={xpath}")
            locator.wait_for(state='visible', timeout=30000)  # Wait for the element to be visible
            locator.click()  # Click the element
            #self.page.click(f"xpath={xpath}")
        except TimeoutError:
            print(f"Element with XPath '{xpath}' not found or not clickable.")
            raise
        except Exception as e:
            print(f"An error occurred while clicking element with XPath '{xpath}': {e}")
            raise

    def click_by_css(self, selector):
        try:
            self.page.click(selector)
        except TimeoutError:
            print(f"Element with CSS selector '{selector}' not found or not clickable.")
            raise
        except Exception as e:
            print(f"An error occurred while clicking element with CSS selector '{selector}': {e}")
            raise

    def click_by_class(self, class_name):
        try:
            self.page.click(f".{class_name}")
        except TimeoutError:
            print(f"Element with class '{class_name}' not found or not clickable.")
            raise
        except Exception as e:
            print(f"An error occurred while clicking element with class '{class_name}': {e}")
            raise
        
    def by_text(self, text):
        try:
            self.page.get_by_text(text).click()
        except TimeoutError:
            print(f"Element with text '{text}' not found or not clickable.")
            raise
        except Exception as e:
            print(f"An error occurred while clicking element with text '{text}': {e}")
            raise

    def by_role(self, role, name=None):
        try:
            if name:
                self.page.get_by_role(role, name=name).click()
            else:
                self.page.get_by_role(role).click()
    
        except TimeoutError:
            print(f"Element with role '{role}' and name '{name}' not found or not clickable.")
            raise
        except Exception as e:
            print(f"An error occurred while clicking element with role '{role}' and name '{name}': {e}")
            raise