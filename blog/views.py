from django.shortcuts import render



def aylar(request):
    return render(request, 'blog/base.html')

