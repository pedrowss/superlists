from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': '1: ' + request.POST.get('item_text', '')
    })
