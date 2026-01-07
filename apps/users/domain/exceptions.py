
class DomainError(Exception):
    """
    Base exception for all domain-level (business) errors.

    QOIDALAR:
    - HTTP bilmaydi
    - Django bilmaydi
    - Faqat biznes ma'noni ifodalaydi
    """
    default_message = "Domain error"

    def __init__(self, message: str | None = None):
        self.message = message or self.default_message
        super().__init__(self.message)

class UserAlreadyExists(DomainError):
    default_message = "User already exists"
    status_code = 400
    code = "user_already_exists"
