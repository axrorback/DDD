from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from apps.users.domain.exceptions import DomainError


def custom_exception_handler(exc, context):
    """
    DRF global exception handler.

    - DomainError → business error
    - Qolganlari → DRF default
    """

    if isinstance(exc, DomainError):
        return Response(
            {
                "error": exc.__class__.__name__,
                "message": str(exc),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    return exception_handler(exc, context)
