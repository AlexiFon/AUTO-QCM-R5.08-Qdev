from behave import given, when, then
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import Group
from app.models import QCM, Question, Reponse, ReponseQCM, Utilisateur

@given(u"j'ai un QCM à réaliser")
def step_impl(context):
    prof_group, _ = Group.objects.get_or_create(name="Enseignant")

    professeur = Utilisateur.objects.create_user(
        username="prof",
        email="prof@gmail.com",
        password="prof"
    )

    professeur.groups.add(prof_group)
    professeur.save()

    qcm = QCM.objects.create(
        titre="QCM à réaliser",
        description="Ceci est un QCM de test",
        date_modif=timezone.now(),
        creator=professeur
    )

    # Créer une question pour le QCM
    question = Question.objects.create(
        nom="Question 1",
        texte="Quelle est la capitale de la France ?",
        note=1,
        melange_rep=False,
        creator=professeur
    )

    # Ajouter des réponses à la question
    Reponse.objects.create(
        question=question,
        texte="Paris",
        is_correct=True,
        creator=professeur
    )
    Reponse.objects.create(
        question=question,
        texte="Londres",
        is_correct=False,
        creator=professeur
    )

    # Ajouter la question au QCM
    qcm.questions.add(question)

    # Créer une réponse QCM pour l'utilisateur connecté
    rep_qcm = ReponseQCM.objects.create(
        utilisateur=context.user,  # Utilisateur connecté
        qcm=qcm,
        date_debut=timezone.now()
    )

    # Enregistrer le QCM et la réponse QCM dans le contexte
    context.qcm = qcm
    context.rep_id = rep_qcm.id

@when(u'je démarre un QCM')
def step_impl(context):
    # Simuler la connexion de l'utilisateur
    context.client.login(username="eleve_qcm", password="eleve_qcm")

    # Accéder à la vue repondre_qcm avec le QCM et la réponse QCM créés
    context.url = reverse('qcm-answer', args=[context.qcm.id, context.rep_id])
    context.response = context.client.get(context.url)

    # Vérifier que la réponse est réussie
    assert context.response.status_code == 302

@then(u'je peux répondre aux questions à mon rythme')
def step_impl(context):
    # Récupérer les questions du QCM
    questions = context.qcm.questions.all()

    # Simuler la soumission des réponses aux questions
    post_data = {}

    for question in questions:
        if question.reponses.filter(is_correct=True).count() > 1:
            # Si la question accepte plusieurs réponses, sélectionnez plusieurs réponses
            reponse_ids = [str(reponse.id) for reponse in question.reponses.all()[:2]]  # Sélectionnez les deux premières réponses
            post_data[f"question_{question.id}"] = reponse_ids
        else:
            # Si la question n'accepte qu'une seule réponse, sélectionnez la première réponse
            reponse_id = str(question.reponses.first().id)
            post_data[f"question_{question.id}"] = reponse_id

    # Soumettre les réponses avec le client Django
    context.response = context.client.post(context.url, post_data)
    assert context.response.status_code == 302
