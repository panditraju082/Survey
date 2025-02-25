from django.urls import path
from . import views

urlpatterns = [
   path("", views.Indexpageview, name="indexpage"),
   path("agepage/", views.InsertData, name="Insertage"),
   path("Genderpage/", views.InsertAge, name="Insertgender"),
   path("Open_endpage/", views.InsertGender, name="Insertopen_end"),
   path("com_page/", views.InsertOpen_End, name="Compleate"),
   path("error/", views.ErrorPage, name="error_page"),
   path("clientpage1page/",views.clientpage1page,name="client1")

]
