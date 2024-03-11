from django.urls import path
from . import views

app_name = "tharack"
urlpatterns = [
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("portfolio",views.portfolio,name="portfolio"),
    path("resume",views.resume,name="resume"),
    path("graph",views.graph,name="graph"),
]
