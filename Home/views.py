from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
import pandas as pd
import numpy as np


# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

class Analysis(TemplateView):
    template_name = 'analysis.html'
