from apps.users.domain.entities import User

from django.contrib.auth.hashers import make_password
from apps.users.domain.entities import User
from apps.users.domain.exceptions import UserAlreadyExists
import uuid  # email verify token uchun

class RegisterUserService:
    """
    Register qilish service.
    Email service integratsiya qilingan.
    """

    def __init__(self, user_repository, email_service):
        self.user_repository = user_repository
        self.email_service = email_service

    def execute(self, email: str, password: str) -> User:
        # 1️⃣ User mavjudligini tekshirish
        if self.user_repository.get_by_email(email):
            raise UserAlreadyExists("User already exists")

        # 2️⃣ Password hash
        hashed_password = make_password(password)

        # 3️⃣ Domain entity yaratish
        user = User(email=email, password=hashed_password)

        # 4️⃣ Repository orqali saqlash
        self.user_repository.save(user)

        # 5️⃣ Email verify token yaratish
        verify_token = str(uuid.uuid4())

        # 6️⃣ Email yuborish
        self.email_service.send_verify_email(email=email, token=verify_token)

        return user


class EmailService:
    """
    Minimal email service. Hozir faqat verify email yuboradi.
    Keyinchalik real SMTP yoki third-party API bilan ishlaydi.
    """

    def send_verify_email(self, email: str, token: str):
        # Misol uchun print qilamiz
        print(f"Sending verify email to {email} with token {token}")
        # Real ishda: SMTP, SendGrid, Amazon SES, etc.
        return True