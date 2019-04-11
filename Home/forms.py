from django import forms
import numpy as np
import pandas as pd

class CompareForm(forms.Form):
    df = pd.read_csv('/home/kalyan/PycharmProjects/fifa19/Home/elclasico.csv')
    barca = df[df['Club'] == 'FC Barcelona']
    madrid = df[df['Club'] == 'Real Madrid']
    barc_list = barca['Name']
    madrid_list = madrid['Name']
    print(barc_list)
    barc_player = forms.CharField(widget=forms.Select(choices=((x, x) for x in barc_list)))
    madrid_player = forms.CharField(widget=forms.Select(choices=[(x, x) for x in madrid_list]))
