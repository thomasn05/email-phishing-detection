from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, 'index.html')

def msg(request):
    return render(request, 'msg.html')