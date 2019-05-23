from django.shortcuts import render


# Create your views here.


def index(req):
    return render(req, "kintai/index.html")

def shukkin_view(req):
    res_dict = {
        "title": "出勤報告",
        "status": "shukkin"
    }
    return render(req, "kintai/kintai.html", res_dict)

def taikin_view(req):
    res_dict = {
        "title": "退勤報告",
        "status": "taikin"
    }
    return render(req, "kintai/kintai.html", res_dict)

def confirm_view(req):
    data = req.POST

    res_dict = {
        "status": data["status"],
        "hour": data["hour"],
        "minute": data["minute"],
    }
    return render(req, "kintai/confirm.html", res_dict)