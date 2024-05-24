from django.urls import path # type: ignore
from . import views

app_name = "tharack"
urlpatterns = [
    path("",views.graph,name="graph"),
    path("login",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
]
