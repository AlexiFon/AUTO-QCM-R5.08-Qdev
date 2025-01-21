from behave import given
from app.models import Utilisateur, Question, QCM, Reponse, Plage
from datetime import timedelta
from django.contrib.auth.models import Group
from django.test import Client
from django.utils import timezone
from behave.api.pending_step import StepNotImplementedError
import os
from django.conf import settings

@given(u'je suis connecté en tant qu\'étudiant')
def step_impl(context):
    eleve,_ = Group.objects.get_or_create(name="Etudiant")
    user = Utilisateur.objects.create_user(
        username="eleve",
        email="eleve@gmail.com",
        password="eleve"
    )

    user.groups.add(eleve)
    user.save()

    context.client = Client()
    context.client.login(username="eleve", password="eleve")
    context.user = user


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

@given(u'j\'ai une question à exporter')
def step_impl(context):
    quest =  Question.objects.create(
        nom="Question à exporter",
        texte="Texte",
        note=1,
        melange_rep=False,
        creator=context.user
    )

    Reponse.objects.create(
        question=quest,
        texte="Réponse",
        is_correct=True,
        creator=context.user
    )

    context.question = quest
    context.dirFiles = os.path.join(settings.BASE_DIR, '..', 'features', 'steps', 'fichiersIntegration')

@given(u'j\'ai un QCM à exporter')
def step_impl(context):
    quest =  Question.objects.create(
        nom="Question1",
        texte="Texte",
        note=1,
        melange_rep=False,
        creator=context.user
    )

    Reponse.objects.create(
        question=quest,
        texte="Réponse",
        is_correct=True,
        creator=context.user
    )

    qcm = QCM.objects.create(
        titre="Qcm",
        description="Texte",
        date_modif=timezone.now(),
        creator=context.user
    )

    promo1,_ = Group.objects.get_or_create(name="BUT1")
    g1a,_ = Group.objects.get_or_create(name="1A")

    Plage.objects.create(
        debut=timezone.now(),
        fin=timezone.now()+timedelta(days=2),
        promo=promo1,
        groupe=g1a,
        qcm=qcm,
    )

    qcm.questions.add(quest)

    context.qcm = qcm
    context.dirFiles = os.path.join(settings.BASE_DIR, '..', 'features', 'steps', 'fichiersIntegration')

    

