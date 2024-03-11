from django.urls import path
from . import views

app_name = "tharack"
urlpatterns = [
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
<<<<<<< HEAD
    path("portfolio",views.portfolio,name="portfolio"),
    path("resume",views.resume,name="resume"),
    path("graph",views.graph,name="graph"),
=======
    path("portfolio/",views.portfolio,name="portfolio"),
    path("resume/",views.resume,name="resume"),
>>>>>>> 249352a1b7009db18fdc27056b030713ccf3ff5e
]
