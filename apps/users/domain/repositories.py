from abc import ABC , abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def save(self,user):
        pass

    def get_by_email(self,email):
        pass