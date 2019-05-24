from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import AddPlayerForm,AddGaleriForm,AddDuyuruForm,AddHaberForm,AddPuanDurumuForm
from .models import Database,Galeri,Duyuru,Haber,PuanDurumu
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    keyword = request.GET.get("keyword")

    if keyword :
        anasayfa_haber = Haber.objects.filter(haber_title__contains = keyword)
        anasayfa_duyuru = Duyuru.objects.filter(duyuru_title__contains = keyword)
        
        

        
        return render(request,"index.html",{"anasayfa_haber":anasayfa_haber,"anasayfa_duyuru":anasayfa_duyuru})
    
    
    anasayfa_haber = Haber.objects.all()
    anasayfa_duyuru = Duyuru.objects.all()
    
    context = {
        "anasayfa_duyuru":anasayfa_duyuru,
        "anasayfa_haber": anasayfa_haber
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def clubdetails(request):
    return render(request,"clubdetails.html")

@login_required(login_url = "user:login")
def EditPlayer(request):
    databases = Database.objects.filter(author = request.user)
    context = {
        "databases" : databases
    }
    
    return render(request,"editplayer.html",context)

@login_required(login_url = "user:login")
def AddPlayer(request):
    form = AddPlayerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        database = form.save(commit=False)
        database.author = request.user
        database.save()

        messages.success(request,"Oyuncu Başarıyla Eklendi...")
        return redirect("database:addplayer")

    return render (request,"addplayer.html",{"form":form})


@login_required(login_url = "user:login")
def UpdatePlayer(request,id):
    player = get_object_or_404(Database,id = id)
    
    form = AddPlayerForm(request.POST or None,request.FILES or None,instance=player)

    if form.is_valid():
        player = form.save(commit=False)
        player.author = request.user
        player.save()
        messages.success(request,"Oyuncu Başarıyla Güncellendi...")
        return redirect("database:editplayer")
    return render(request,"updateplayer.html",{"form":form})

@login_required(login_url = "user:login")
def DeletePlayer(request,id):
    player = get_object_or_404(Database,id = id)
    player.delete()

    messages.success(request,"Oyuncu Başarıyla Silindi...")

    return redirect("database:editplayer")


@login_required(login_url = "user:login")
def EditGaleri(request):
    galeris = Galeri.objects.filter(author = request.user)
    context = {
        "galeris" : galeris
    }
    
    return render(request,"editgaleri.html",context)


@login_required(login_url = "user:login")
def AddGaleri(request):
    form = AddGaleriForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        galeri = form.save(commit=False)
        galeri.author = request.user
        galeri.save()

        messages.success(request,"Görsel Başarıyla Eklendi...")
        return redirect("database:editgaleri")

    return render (request,"addgaleri.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateGaleri(request,id):
    galeri = get_object_or_404(Galeri,id = id)
    
    form = AddGaleriForm(request.POST or None,request.FILES or None,instance=galeri)

    if form.is_valid():
        galeri = form.save(commit=False)
        galeri.author = request.user
        galeri.save()
        messages.success(request,"Görsel Başarıyla Güncellendi...")
        return redirect("database:editgaleri")
    return render(request,"updategaleri.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteGaleri(request,id):
    galeri = get_object_or_404(Galeri,id = id)
    galeri.delete()

    messages.success(request,"Görsel Başarıyla Silindi...")

    return redirect("database:editgaleri")


@login_required(login_url = "user:login")
def EditDuyuru(request):
    duyurular = Duyuru.objects.filter(author = request.user)
    context = {
        "duyurular" : duyurular
    }
    
    return render(request,"editduyuru.html",context)

@login_required(login_url = "user:login")
def AddDuyuru(request):
    form = AddDuyuruForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        duyuru = form.save(commit=False)
        duyuru.author = request.user
        duyuru.save()

        messages.success(request,"Duyuru Başarıyla Eklendi...")
        return redirect("database:editduyuru")

    return render (request,"addduyuru.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateDuyuru(request,id):
    duyuru = get_object_or_404(Duyuru,id = id)
    
    form = AddDuyuruForm(request.POST or None,request.FILES or None,instance=duyuru)

    if form.is_valid():
        duyuru = form.save(commit=False)
        duyuru.author = request.user
        duyuru.save()
        messages.success(request,"Duyuru Başarıyla Güncellendi...")
        return redirect("database:editduyuru")
    return render(request,"updateduyuru.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteDuyuru(request,id):
    duyuru = get_object_or_404(Duyuru,id = id)
    duyuru.delete()

    messages.success(request,"Duyuru Başarıyla Silindi...")

    return redirect("database:editduyuru")


@login_required(login_url = "user:login")
def EditHaber(request):
    haberler = Haber.objects.filter(author = request.user)
    context = {
        "haberler" : haberler
    }
    
    return render(request,"edithaber.html",context)

@login_required(login_url = "user:login")
def AddHaber(request):
    form = AddHaberForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        haber = form.save(commit=False)
        haber.author = request.user
        haber.save()

        messages.success(request,"Haber Başarıyla Eklendi...")
        return redirect("database:edithaber")

    return render (request,"addhaber.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateHaber(request,id):
    haber = get_object_or_404(Haber,id = id)
    
    form = AddHaberForm(request.POST or None,request.FILES or None,instance=haber)

    if form.is_valid():
        haber = form.save(commit=False)
        haber.author = request.user
        haber.save()
        messages.success(request,"Haber Başarıyla Güncellendi...")
        return redirect("database:edithaber")
    return render(request,"updatehaber.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteHaber(request,id):
    haber = get_object_or_404(Haber,id = id)
    haber.delete()

    messages.success(request,"Haber Başarıyla Silindi...")

    return redirect("database:edithaber")



@login_required(login_url = "user:login")
def EditPuanDurumu(request):
    
    puandurumları = PuanDurumu.objects.filter(author = request.user)
    context = {
        "puandurumları" : puandurumları
    }
    
    return render(request,"editpuandurumu.html",context)

@login_required(login_url = "user:login")
def AddPuanDurumu(request):
    form = AddPuanDurumuForm(request.POST or None,)

    if form.is_valid():
        puandurumu = form.save(commit=False)
        puandurumu.author = request.user
        puandurumu.save()

        messages.success(request,"Puan Durumu Başarıyla Eklendi...")
        return redirect("database:editpuandurumu")

    return render (request,"addpuandurumu.html",{"form":form})

@login_required(login_url = "user:login")
def UpdatePuanDurumu(request,id):
    puandurumu = get_object_or_404(PuanDurumu,id = id)
    
    form = AddPuanDurumuForm(request.POST or None,request.FILES or None,instance=puandurumu)

    if form.is_valid():
        puandurumu = form.save(commit=False)
        puandurumu.author = request.user
        puandurumu.save()
        messages.success(request,"Puan Durumu Başarıyla Güncellendi...")
        return redirect("database:editpuandurumu")
    return render(request,"updatepuandurumu.html",{"form":form})

@login_required(login_url = "user:login")
def DeletePuanDurumu(request,id):
    puandurumu = get_object_or_404(PuanDurumu,id = id)
    puandurumu.delete()

    messages.success(request,"Puan Durumu Başarıyla Silindi...")

    return redirect("database:editpuandurumu")

def Team(request,id):
    if id == 1:
        puandurumları = PuanDurumu.objects.filter(category = "A TAKIM")
        oyuncular = Database.objects.filter(category = "A TAKIM")

        context = {
            "puandurumları" : puandurumları,
            "oyuncular" : oyuncular
        }

    if id == 2:
        puandurumları = PuanDurumu.objects.filter(category = "A GENÇ")
        oyuncular = Database.objects.filter(category = "A GENÇ")

        context = {
            "puandurumları" : puandurumları,
            "oyuncular" : oyuncular
        }

    if id == 3:
        puandurumları = PuanDurumu.objects.filter(category = "U 17")

        context = {
            "puandurumları" : puandurumları
        }

    if id == 4:
        puandurumları = PuanDurumu.objects.filter(category = "U 16")

        context = {
            "puandurumları" : puandurumları
        }

    if id == 5:
        puandurumları = PuanDurumu.objects.filter(category = "U 15")

        context = {
            "puandurumları" : puandurumları
        }

    if id == 6:
        puandurumları = PuanDurumu.objects.filter(category = "U 14")

        context = {
            "puandurumları" : puandurumları
        }

    if id == 7:
        puandurumları = PuanDurumu.objects.filter(category = "U 13")

        context = {
            "puandurumları" : puandurumları
        }

    
        
    return render(request,"team.html",context)


def SporOkulu(request):
    return render(request,"sporokulu.html")

def Basarılarımız(request):
    return render(request,"basarılarımız.html")
    
def Oyuncularımız(request):

    keyword = request.GET.get("keyword")

    if keyword :
        oyuncular = Database.objects.filter(name__contains = keyword)
        
        return render(request,"oyuncularımız.html",{"oyuncular":oyuncular})

    oyuncular = Database.objects.all()
    context = {
        "oyuncular":oyuncular
    }
    return render(request,"oyuncularımız.html",context)

def Galerii(request):
    galeris = Galeri.objects.all()
    context={
        "galeris":galeris
    }
    return render(request,"galeri.html",context)

def Detail(request,id):
    oyuncu = get_object_or_404(Database,id = id)
    context = {
        "oyuncu":oyuncu
    }
    return render(request,"detail.html",context)

def HaberDetail(request,id):
    haber = get_object_or_404(Haber,id = id)
    context = {
        "haber":haber
    }
    return render(request,"haberdetail.html",context)


    

