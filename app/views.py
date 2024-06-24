from django.shortcuts import render, redirect
from django.http import Http404
from .models import Urls
import string, random

def generate_furl(length=15):
    characters = string.ascii_letters + string.digits
    furl = ''.join(random.choice(characters) for _ in range(length))
    return furl

def homepage(request):
    furl = None
    if request.method == 'POST':
        ourl = request.POST.get('url')
        furl = generate_furl()
        while Urls.objects.filter(furl=furl).exists():
            furl = generate_furl()
        ins = Urls.objects.create(ourl=ourl, furl=furl)
        ins.save()
        return render(request, 'index.html', {'furl': furl})
    return render(request,'index.html')

def redirect_url(request, furl):
    urls = Urls.objects.filter(furl=furl)
    if not urls.exists():
        raise Http404("URL not found")
    url = urls.first()
    return redirect(url.ourl)
