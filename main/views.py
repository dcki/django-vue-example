from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect


def root(request: HttpRequest) -> HttpResponse:
    return redirect('notes:index')
