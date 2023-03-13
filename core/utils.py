from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse

from sales.models import Sellers


def check_seller_superuser(request: HttpRequest) -> HttpResponse:
    is_seller = False
    if Sellers.objects.filter(user=request.user):
        is_seller = True
    if request.user.is_authenticated:
        if request.user.is_superuser or is_seller:
            request.is_ok = True
            return request
    raise PermissionDenied
