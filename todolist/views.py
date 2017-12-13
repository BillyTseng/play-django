from django.http import HttpResponse
import datetime


def index(request):
    message = "current Time:{}".format(datetime.datetime.now())
    return HttpResponse(message)
