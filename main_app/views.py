from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dawg, Toy
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def dawg_index(request):
    dawgs = Dawg.objects.all()
    return render(request, "dawgs/index.html", {"dawgs": dawgs})


def dawg_detail(request, dawg_id):
    dawg = Dawg.objects.get(id=dawg_id)

    toys_dawg_doesnt_have = Toy.objects.exclude(id__in = dawg.toys.all().values_list('id'))

    feeding_form = FeedingForm()
    return render(request, 'dawgs/detail.html', {
        'dawg': dawg,
        'feeding_form': feeding_form,
        'toys': toys_dawg_doesnt_have 
    })

class DawgCreate(CreateView):
    model = Dawg
    fields = ["name", "breed", "description", "age"]
    success_url = "/dawgs/"


class DawgUpdate(UpdateView):
    model = Dawg
    fields = ["breed", "description", "age"]


class DawgDelete(DeleteView):
    model = Dawg
    success_url = "/dawgs/"


def add_feeding(request, dawg_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dawg_id = dawg_id
        new_feeding.save()
    return redirect("dawg-detail", dawg_id=dawg_id)


class ToyCreate(CreateView):
    model = Toy
    fields = "__all__"


class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyUpdate(UpdateView):
    model = Toy
    fields = ["name", "color"]


class ToyDelete(DeleteView):
    model = Toy
    success_url = "/toys/"

def associate_toy(request, dawg_id, toy_id):
    Dawg.objects.get(id=dawg_id).toys.add(toy_id)
    return redirect('dawg-detail', dawg_id=dawg_id)

def remove_toy(request, dawg_id, toy_id):
    Dawg.objects.get(id=dawg_id).toys.remove(toy_id)
    return redirect('dawg-detail', dawg_id=dawg_id)