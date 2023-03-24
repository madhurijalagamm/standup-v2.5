from django.shortcuts import render

# Create your views here.
def homeaction(request):
    return render(request, 'home.html')

# def testaction(request):
#     return render(request, 'test1.html')