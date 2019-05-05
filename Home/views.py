from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from .forms import CompareForm


# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

class Analysis(TemplateView):
    template_name = 'analysis.html'

class Analyse(TemplateView):
    template_name = 'analysis1.html'

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        to_email = email
        print(email)
        message = render_to_string('sub_mail.html', {

        })
        mail_subject = "Newsletter"
        mail = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, to=[to_email])
        mail.send()
        return HttpResponseRedirect('/')
    return HttpResponse("Enter valid EmailId")

class Compare(View):
    template_name = 'compare.html'
    form_class = CompareForm
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            barc_player = form.cleaned_data['barc_player']
            madrid_player = form.cleaned_data['madrid_player']
            print(barc_player)
            print(madrid_player)
            plt.clf()
            df = pd.read_csv('/home/kalyan/PycharmProjects/fifa19/Home/elclasico.csv')
            player_features = (
                'Acceleration', 'Aggression', 'Agility',
                'Balance', 'BallControl', 'Composure',
                'Crossing', 'Dribbling', 'FKAccuracy',
                'Finishing', 'GKDiving', 'GKHandling',
                'GKKicking', 'GKPositioning', 'GKReflexes',
                'HeadingAccuracy', 'Interceptions', 'Jumping',
                'LongPassing', 'LongShots', 'Marking', 'Penalties'
            )
            player_feature = list(player_features)
            sel =df[player_feature]
            # number of variable
            categories=list(sel)
            N = len(categories)

            # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
            angles = [n / float(N) * 2 * pi for n in range(N)]
            angles += angles[:1]

            # Initialise the spider plot
            ax = plt.subplot(111, polar=True)

            # If you want the first axis to be on top:
            ax.set_theta_offset(pi / 2)
            ax.set_theta_direction(-1)

            # Draw one axe per variable + add labels labels yet
            plt.xticks(angles[:-1], categories)

            # Draw ylabels
            ax.set_rlabel_position(0)
            plt.yticks([25,50,75], ["25","50","75"], color="grey", size=7)
            plt.ylim(0,100)


            # ------- PART 2: Add plots

            # Plot each individual = each line of the data
            # I don't do a loop, because plotting more than 3 groups makes the chart unreadable
            first = df.loc[df['Name']==barc_player].index[0]
            second = df.loc[df['Name']==madrid_player].index[0]
            print(first)
            print(second)
            # Ind1
            values=sel.loc[first].values.flatten().tolist()
            values += values[:1]
            ax.plot(angles, values, linewidth=1, linestyle='solid', label=barc_player)
            ax.fill(angles, values, 'b', alpha=0.1)

            # Ind2
            values=sel.loc[second].values.flatten().tolist()
            values += values[:1]
            ax.plot(angles, values, linewidth=1, linestyle='solid', label=madrid_player)
            ax.fill(angles, values, 'r', alpha=0.1)

            # Add legend
            plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
            hey = ax.get_figure()
            hey.savefig("/home/kalyan/PycharmProjects/fifa19/Home/static/images/comparison.png")

            return render(request, 'sample.html')


def compareplayers(request):
    df = pd.read_csv('/home/kalyan/PycharmProjects/fifa19/Home/elclasico.csv')
    player_features = (
        'Acceleration', 'Aggression', 'Agility',
        'Balance', 'BallControl', 'Composure',
        'Crossing', 'Dribbling', 'FKAccuracy',
        'Finishing', 'GKDiving', 'GKHandling',
        'GKKicking', 'GKPositioning', 'GKReflexes',
        'HeadingAccuracy', 'Interceptions', 'Jumping',
        'LongPassing', 'LongShots', 'Marking', 'Penalties'
    )
    player_feature = list(player_features)
    sel =df[player_feature]
    # number of variable
    categories=list(sel)
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([25,50,75], ["25","50","75"], color="grey", size=7)
    plt.ylim(0,100)


    # ------- PART 2: Add plots

    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable

    # Ind1
    values=sel.loc[0].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Messi")
    ax.fill(angles, values, 'b', alpha=0.1)

    # Ind2
    values=sel.loc[1].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Suarez")
    ax.fill(angles, values, 'r', alpha=0.1)

    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    hey = ax.get_figure()
    hey.savefig("/home/kalyan/PycharmProjects/fifa19/Home/static/images/comparison.png")
    return render(request, 'sample.html')
