from django.shortcuts import render


# Create your views here.
def links(request):
    return render(request, 'config/links.html', context={"name": "links"})
