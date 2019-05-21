from django.shortcuts import render


# Create your views here.


def index(req):
    return render(req, "kintai/index.html")

def shukkin_view(req):
    return render(req, "kintai/shukkin.html")

def taikin_view(req):
    return render(req, "kintai/taikin.html")
