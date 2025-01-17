from behave import when, then
from django.contrib.auth.models import Group
from app.models import Utilisateur, Question
from django.test.client import Client

@when('j\'accède à l\'espace de gestion des questions')
def step_impl(context):
    response = context.client.get('/question/list/')
    assert response.status_code == 200
    context.response = response

@then('je peux modifier une question existante')
def step_impl(context):
    question = Question.objects.get_or_create(
        nom="question a modifier", texte="texte", creator=context.user
    )
    response = context.client.post(f'/questions/edit/{question.id}', {
        'nom': "Question modifiée",
        'texte': "Contenu modifié",
        'creator': context.user
    })
    assert response.status_code == 302
    question.refresh_from_db()
    assert question.title == "Question modifiée"
    assert question.content == "Contenu modifié"

@then('je peux supprimer une question')
def step_impl(context):
    question = Question.objects.get_or_create(
        nom="question a supprimer", texte="texte", creator=context.user
    )
    print(question)
    response = context.client.post(f'/questions/delete/{question.id}')
    assert response.status_code == 302
    assert not Question.objects.filter(id=question.id).exists()

@then('je peux ajouter une nouvelle question')
def step_impl(context):
    response = context.client.post('/questions/create/', {
        'titre': "Nouvelle question",
        'texte': "Contenu de la nouvelle question",
        'creator': context.user
    })
    assert response.status_code == 302  # Redirection après ajout
    assert Question.objects.filter(title="Nouvelle question").exists()
