from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
import os

# Create your views here.
def greetings(request):
	res = render(request,'ydownloader/home.html')
	return res

def download(request):
    if request.method == 'POST':
        video_url=request.POST['video_url']
        yt = YouTube(video_url)
        thumbnail_url = yt.thumbnail_url
        title = yt.title
        length = yt.length
        desc = yt.description
        view = yt.views
        rating = yt.rating
        age_restricted = yt.age_restricted
        res = render(request,'ydownloader/home.html',{"title":title,"thumbnail_url":thumbnail_url,"video_url":video_url})
        return res
    else:
        res = render(request,'ydownloader/home.html')
        return res

def downloading(request):
	if request.method == 'POST':
		# homedir = os.path.expanduser("~")
		# dirs = homedir + '\Downloads'
		formatRadio = request.POST['formatRadio']
		# print(dirs)
		if formatRadio != "audio":
			qualityRadio = request.POST['qualityRadio']
		video_url_d = request.POST['video_url_d']
		yt = YouTube(video_url_d)
		if formatRadio == "audio":
			yt.streams.filter(type = formatRadio).last().download()
		else:
			homedir = yt.streams.filter(type = formatRadio,resolution=qualityRadio).first().download()
	res = render(request,'ydownloader/home.html',{"msg":"downloading completed. Check your Download directory!", 'loca':homedir})
	return res
