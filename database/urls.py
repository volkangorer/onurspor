from . import views

from django.contrib import admin
from django.urls import path,include


app_name = "database"


urlpatterns = [
    path('clubdetails/', views.clubdetails,name = "clubdetails"),

    path('editplayer/', views.EditPlayer,name = "editplayer"),
    path('addplayer/', views.AddPlayer,name = "addplayer"),
    path('updateplayer/<int:id>', views.UpdatePlayer,name = "updateplayer"),
    path('deleteplayer/<int:id>', views.DeletePlayer,name = "deleteplayer"),
    
    path('editgaleri/', views.EditGaleri,name = "editgaleri"),
    path('addgaleri/', views.AddGaleri,name = "addgaleri"),
    path('updategaleri/<int:id>', views.UpdateGaleri,name = "updategaleri"),
    path('deletegaleri/<int:id>', views.DeleteGaleri,name = "deletegaleri"),
    
    path('editduyuru/', views.EditDuyuru,name = "editduyuru"),
    path('addduyuru/', views.AddDuyuru,name = "addduyuru"),
    path('updateduyuru/<int:id>', views.UpdateDuyuru,name = "updateduyuru"),
    path('deleteduyuru/<int:id>', views.DeleteDuyuru,name = "deleteduyuru"),

    path('edithaber/', views.EditHaber,name = "edithaber"),
    path('addhaber/', views.AddHaber,name = "addhaber"),
    path('updatehaber/<int:id>', views.UpdateHaber,name = "updatehaber"),
    path('deletehaber/<int:id>', views.DeleteHaber,name = "deletehaber"),

    
    path('puandurumu/', views.EditPuanDurumu,name = "editpuandurumu"),
    path('addpuandurumu/', views.AddPuanDurumu,name = "addpuandurumu"),
    path('updatepuandurumu/<int:id>', views.UpdatePuanDurumu,name = "updatepuandurumu"),
    path('deletepuandurumu/<int:id>', views.DeletePuanDurumu,name = "deletepuandurumu"),

    path('team/<int:id>', views.Team,name = "team"),

    path('sporokulu/', views.SporOkulu,name = "sporokulu"),
    path('basarılarımız/', views.Basarılarımız,name = "basarılarımız"),
    path('galeri', views.Galerii,name = "galeri"),
    path('oyuncularımız/', views.Oyuncularımız,name = "oyuncularımız"),
    path('detail/<int:id>', views.Detail,name = "detail"),
    path('haber_detail/<int:id>', views.HaberDetail,name = "haber_detail"),
    
]

