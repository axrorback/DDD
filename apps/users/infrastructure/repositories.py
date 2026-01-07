from apps.users.domain.repositories import UserRepository
from apps.users.infrastructure.models import UserModel


class DjangoUserRepository(UserRepository):

    def save(self, user):
        UserModel.objects.create(
            email=user.email,
            password=user.password
        )

    def get_by_email(self, email):
        try:
            obj = UserModel.objects.get(email=email)
            return obj
        except UserModel.DoesNotExist:
            return None
