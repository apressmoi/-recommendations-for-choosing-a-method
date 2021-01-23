from http import HTTPStatus
from django.http import HttpResponse


class HttpResultResponse(HttpResponse):
    status_code = HTTPStatus.NO_CONTENT


