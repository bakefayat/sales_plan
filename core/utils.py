from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse


def check_seller_superuser(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.is_seller:
            request.is_ok = True
            return request
    raise PermissionDenied
