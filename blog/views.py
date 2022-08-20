from django.shortcuts import render

def person_list(request):
    return render(request, 'blog/person_list.html',{})

# Create your views here.
