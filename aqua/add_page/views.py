from django.shortcuts import render

def request_page(request):
    return render(request, 'add_page.html', {})