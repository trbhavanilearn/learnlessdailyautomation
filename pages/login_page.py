from config import BASE_URL, PASSWORD

class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self, BASE_URL): 
        self.page.goto(BASE_URL) 

    def get_title(self): 
        return self.page.title()