from behave import when, then
from app.models import Question, Tag

@when('j\'accède à l\'espace de gestion des questions')
def step_impl(context):
    response = context.client.get('/question/list/')
    assert response.status_code == 200
    context.response = response

@then('je peux modifier une question existante')
def step_impl(context):
    question,_ = Question.objects.get_or_create(
        nom="question a modifier", texte="texte", creator=context.user
    )

    tag1 = Tag.objects.create(name="Tag existant")

    response = context.client.post(f'/question/edit/{question.id}/', {
        'nom': "Question modifiée",
        'texte': "Contenu modifié",
        'tags': [tag1.id],
        'note': 1,
        'melange_rep': False,
        'image': ''

    })
    print(response.status_code)
    assert response.status_code == 302
    question.refresh_from_db()
    assert question.nom == "Question modifiée"
    assert question.texte == "Contenu modifié"

@then('je peux supprimer une question')
def step_impl(context):
    question,_ = Question.objects.get_or_create(
        nom="question a supprimer", texte="texte", creator=context.user
    )
    print(question)
    response = context.client.post(f'/question/delete/{question.id}')
    assert response.status_code == 302
    assert not Question.objects.filter(id=question.id).exists()

@then('je peux ajouter une nouvelle question')
def step_impl(context):
    response = context.client.post('/question/create/', {
        'titre': "Nouvelle question",
        'texte': "Contenu de la nouvelle question",
        'creator': context.user
    })
    assert response.status_code == 302  # Redirection après ajout
    assert Question.objects.filter(title="Nouvelle question").exists()
