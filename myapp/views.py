from django.shortcuts import redirect, render
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'us.html')

def create (request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url =Url(link =link ,uuid =uid)
        new_url.save()
        return HttpResponse(uid)

def go(request,pk):
    url_detials =Url.objects.get(uuid=pk)

    return redirect(url_detials.link)
