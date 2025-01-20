from behave import when, then
from app.models import Question, Tag, Reponse

@when('j\'accède à l\'espace de gestion des questions')
def step_impl(context):
    response = context.client.get('/question/list/')
    assert response.status_code == 200
    context.response = response

@then('je peux modifier une question existante')
def step_impl(context):
    tag1 = Tag.objects.create(name="Tag test")
    question_initiale = Question.objects.create(
        nom="Question initiale",
        texte="Texte initial",
        note=1,
        melange_rep=False,
        creator=context.user
    )
    question_initiale.tags.add(tag1)

    rep1 = Reponse.objects.create(
        question=question_initiale,
        texte="Réponse initiale",
        is_correct=True,
        creator=context.user
    )

    updated_data = {
        'nom': "Question mise à jour",
        'texte': "Texte mis à jour",
        'note': 2,
        'melange_rep': True,
        'tags': [tag1.pk],
        'new_tags': '',
        'image': '',
        'reponses-TOTAL_FORMS': '1',
        'reponses-INITIAL_FORMS': '1',
        'reponses-MIN_NUM_FORMS': '0',
        'reponses-MAX_NUM_FORMS': '1000',
        'reponses-0-id': rep1.id,
        'reponses-0-texte': 'Réponse initiale',
        'reponses-0-is_correct': True,
        'reponses-0-DELETE': False
    }

    response = context.client.post(f'/question/edit/{question_initiale.pk}/', updated_data)

    if response.status_code == 200:
        print("Form errors:", response.context['form'].errors)
        print("Formset errors:", response.context['formset'].errors)

    assert response.status_code == 302

    question_initiale.refresh_from_db()
    assert question_initiale.nom == "Question mise à jour"
    assert question_initiale.texte == "Texte mis à jour"
    assert question_initiale.note == 2
    assert question_initiale.melange_rep is True

@then('je peux supprimer une question')
def step_impl(context):
    question,_ = Question.objects.get_or_create(
        nom="question a supprimer", texte="texte", creator=context.user
    )
    
    response = context.client.get(f'/question/delete/{question.id}/')
    print(response.url)
    print(response.status_code)
    assert response.status_code == 302
    assert not Question.objects.filter(id=question.id).exists()

@then('je peux ajouter une nouvelle question')
def step_impl(context):
    print(context.user.id)

    tag1 = Tag.objects.create(name="Tag test")
    question_data = {
        'nom': "Nouvelle question",
        'texte': "Contenu de la nouvelle question",
        'note': 1,
        'melange_rep': False,
        'tags': [tag1.pk],
        'new_tags': '',
        'image': '',
        'reponses-TOTAL_FORMS': '1',
        'reponses-INITIAL_FORMS': '0',
        'reponses-MIN_NUM_FORMS': '0',
        'reponses-MAX_NUM_FORMS': '1000',
        'reponses-0-texte': 'Première réponse',
        'reponses-0-is_correct': True,
        'reponses-0-DELETE': False
    }
    
    response = context.client.post('/question/create/', question_data)
    
    if response.status_code == 200:
        print("Form errors:", response.context['form'].errors)
        print("Formset errors:", response.context['formset'].errors)
    assert response.status_code == 302 
    assert Question.objects.filter(nom="Nouvelle question").exists()
