from behave import given,when,then
from app.models import Utilisateur
from django.contrib.auth.models import Group
from django.test import Client
from behave.api.pending_step import StepNotImplementedError

@given(u'je suis connecté en tant qu\'étudiant')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Given je suis connecté en tant qu\'étudiant')

@given(u'je suis connecté en tant qu\'enseignant')
def step_impl(context):
    prof_group, _ = Group.objects.get_or_create(name="Enseignant")

    professeur = Utilisateur.objects.create_user(
        username="prof",
        email="prof@gmail.com",
        password="prof"
    )

    professeur.groups.add(prof_group)
    professeur.save()

    context.client = Client()
    context.client.login(username="prof", password="prof")
    context.user = professeur