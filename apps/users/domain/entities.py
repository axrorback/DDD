class User:
    def __init__(self, email: str,password:str,is_active:bool=False):
        self.email = email
        self.password = password
        self.is_active = is_active
    def activate(self):
        self.is_active = True