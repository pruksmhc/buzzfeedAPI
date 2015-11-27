from django.conf.urls import url
import views

urlpatterns = [
    url(r'^buzzfeed/$', views.JSONResponse.buzzfeed_list),
]