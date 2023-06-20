from django.urls import path

from bgremove.views import ResultView, UploadView

app_name = "bgremove"

urlpatterns = [
    path("bg/", UploadView.as_view(), name="home"),
    path("result/<slug:slug>/", ResultView.as_view(), name="result"),
]
