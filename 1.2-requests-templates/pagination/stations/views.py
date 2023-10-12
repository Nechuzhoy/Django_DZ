import csv

import django.conf
import django.template.backends.django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


with open(django.conf.settings.BUS_STATION_CSV, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=None)
    list_bus_stations = []
    for j in reader:
        list_bus_stations.append({'Name': j['Name'], 'Street': j['Street'], 'District': j['District']})

CONTENT = list_bus_stations


def bus_stations(request):
    per_pag = 10
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, per_pag)
    page = paginator.get_page(page_num)
    context = {
        'bus_stations': CONTENT[:per_pag],
        'page': page,
    }
    return render(request, 'stations/index.html', context)
