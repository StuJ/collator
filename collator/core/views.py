from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    template = 'core/home.html'
    context = {
        'new_item_text': request.POST.get('node_name', ''),
    }
    return render(request, template, context)
