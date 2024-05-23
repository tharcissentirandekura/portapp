from django.urls import path # type: ignore
from . import views

app_name = "tharack"
urlpatterns = [
    path("",views.graph,name="graph"),
]
