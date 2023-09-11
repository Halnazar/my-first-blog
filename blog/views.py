from django.shortcuts import render



def Aylar(request):
    return render(request, 'blog/base.html')

