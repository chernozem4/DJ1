from django.http import HttpResponse
from django.shortcuts import render

# Первое представление, которое отдает текстовый ответ
def text_response(request):
    return HttpResponse("Это текстовый ответ от Django.")

# Второе представление, которое отдает HTML шаблон
def html_response(request):
    return render(request, 'template.html')

