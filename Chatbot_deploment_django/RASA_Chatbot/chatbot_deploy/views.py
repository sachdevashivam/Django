from django.shortcuts import render

# Create your views here.

def mychatbot(request):
    return render(request, 'index.html')
