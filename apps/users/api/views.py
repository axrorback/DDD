from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.application.services import RegisterUserService , EmailService
from apps.users.infrastructure.repositories import DjangoUserRepository


class RegisterView(APIView):
    """
    POST /api/users/register/
    """

    def post(self, request):
        service = RegisterUserService(
            user_repository=DjangoUserRepository(),
            email_service=EmailService()
        )

        user = service.execute(
            email=request.data["email"],
            password=request.data["password"]
        )

        return Response(
            {"email": user.email, "message": "User registered. Verification email sent."},
            status=status.HTTP_201_CREATED
        )
