from django.shortcuts import render

from pytube import YouTube


# link = input("Url kiriting :")
# yt = YouTube(link)
# stream = yt.streams.get_highest_resolution()

# stream.download()

# print("video yuklandi")


def yd(request):
    x=""
    try:
      if request.method=='GET':
        link=request.GET.get('video')
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        result=stream.download()
        data=result.objects.all()
        
    except:
        x="Url noto'g'ri !"
    return render(request,'yd.html')

# Create your views here.
def index (request):

    return render(request,"index.html")

