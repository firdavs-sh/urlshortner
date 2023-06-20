from django.views.generic import CreateView, DetailView
from django.shortcuts import render
from bgremove.models import UserActivity




class UploadView(CreateView):
    model = UserActivity
    fields = ["image"]
    template_name = "bg/index.html"



class ResultView(DetailView):
    model = UserActivity
    template_name = "bg/result.html"
    context_object_name = "user_activity"
