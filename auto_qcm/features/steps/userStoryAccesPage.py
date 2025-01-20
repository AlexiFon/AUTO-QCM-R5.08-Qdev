from behave import when, then, given
from django.contrib.auth.models import Group
from app.models import Utilisateur
from django.test.client import Client

@when(u'je tente d\'accéder à une page destinée aux étudiants')
def step_impl(context):
    # Tentative d'accès à une page étudiante
    user_id = context.user_id
    url = f'/etudiant-dashboard/{user_id}/'
    response = context.client.get(url)
    context.response = response
    print("Tentative d'accès à une page étudiante avec l'url : ", url)

@when(u'je tente d\'accéder à une page destinée aux enseignants')
def step_impl(context):
    # Tentative d'accès à une page enseignante
    user_id = context.user_id  # Récupérer l'ID utilisateur
    url = f'/enseignant-dashboard/{user_id}/'
    response = context.client.get(url)
    context.response = response
    print("Tentative d'accès à une page enseignante")

@then(u'je devrais voir le contenu de la page')
def step_impl(context):
    # Vérification du contenu de la page
    assert context.response.status_code == 200, f"Statut attendu: 200, obtenu: {context.response.status_code}"
    print("Accès autorisé et contenu visible")
