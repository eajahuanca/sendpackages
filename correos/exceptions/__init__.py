from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException

class UserDoesnotAuthenticated(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {
        'message': _('Authentication credentials were not provided.'),
        'type': 'error',
        'status': status_code
    }
    default_code = 'not_authenticated'