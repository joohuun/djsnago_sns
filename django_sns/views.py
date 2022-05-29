from django.http import HttpResponse
from django.shortcuts import render


def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작 입니다!")


def first_view(request):
    return render(request, 'user/../templates/my_test.html')
