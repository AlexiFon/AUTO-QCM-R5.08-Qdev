from django.utils import timezone
from app.models import Question, QCM, Plage
from behave import given,when, then
from behave.api.pending_step import StepNotImplementedError
from django.urls import reverse
from django.contrib.auth.models import Group


@when(u'je crée un nouveau QCM')
def step_impl(context):
    question1 = Question.objects.create(
        nom="Question 1",
        texte="Texte de la question 1",
        creator=context.user
    )
    question2 = Question.objects.create(
        nom="Question 2",
        texte="Texte de la question 2",
        creator=context.user
    )

    promo=Group.objects.create(name="BUT1")
    groupe=Group.objects.create(name="1A")

    selected_questions = [question1.id, question2.id]
    
    form_data = {
        'titre': 'test',
        'description': 'test1',
        'nb_tentatives': '1',
        'est_accessible': 'on',
        'form-TOTAL_FORMS': '1',
        'form-INITIAL_FORMS': '0',
        'form-MIN_NUM_FORMS': '0',
        'form-MAX_NUM_FORMS': '1000',
        'form-0-debut': '2024-10-10T13:45',
        'form-0-fin': '2024-12-12T12:00',
        'form-0-promo': promo.id,
        'form-0-groupe': groupe.id,
        'form-0-id': '',
        'form-__prefix__-debut': '',
        'form-__prefix__-fin': '',
        'form-__prefix__-promo': '',
        'form-__prefix__-groupe': '',
        'form-__prefix__-id': '',
        'selected_questions': selected_questions
    }
    
    create_url = reverse('qcm-create')
    context.response = context.client.post(create_url, form_data)

@then(u'le QCM est crée')
def step_impl(context):
    assert context.response.status_code in [200, 302], f"La création a échoué avec le code {context.response.status_code}"
    
    new_qcm = QCM.objects.last()
    assert new_qcm is not None, "Le QCM n'a pas été créé"
    
    assert new_qcm.titre, "Le titre est vide"
    assert new_qcm.description, "La description est vide"
    assert new_qcm.nb_tentatives > 0, "Le nombre de tentatives doit être supérieur à 0"
    
    assert new_qcm.questions.exists(), "Aucune question n'est associée au QCM"
    
    plage = new_qcm.plages.first()
    assert plage is not None, "Aucune plage horaire n'a été créée"
    assert plage.debut is not None, "La date de début est vide"
    assert plage.fin is not None, "La date de fin est vide"
    assert plage.promo is not None, "Aucune promo n'est associée"
    assert plage.groupe is not None, "Aucun groupe n'est associé"
    
    print(f"Le QCM '{new_qcm.titre}' a été créé avec succès avec {new_qcm.questions.count()} questions et une plage horaire configurée")

@given(u"j'ai créé un QCM")
def step_impl(context):
    promo=Group.objects.create(name="BUT1")
    groupe=Group.objects.create(name="1A")

    qcm = QCM.objects.create(
        titre="QCM de test",
        description="Description du QCM de test",
        creator=context.user
    )
    
    plage = Plage.objects.create(
        debut=timezone.now(),
        fin=timezone.now() + timezone.timedelta(days=1),
        promo=promo,
        groupe=groupe,
        qcm=qcm
    )
    
    question1 = Question.objects.create(
        nom="Question 1",
        texte="Texte de la question 1",
        creator=context.user
    )
    question2 = Question.objects.create(
        nom="Question 2",
        texte="Texte de la question 2",
        creator=context.user
    )
    
    qcm.questions.set([question1, question2])
    
    context.qcm = qcm
    context.selected_question = [question1, question2]

@when(u'je modifie un QCM')
def step_impl(context):

    qcm = context.qcm
    plage = qcm.plages.first()

    print(f"Plage: {plage.promo.id} - {plage.groupe.id}")
    
    form_data = {
        'titre': 'test modifié',
        'description': 'test1 modifié',
        'nb_tentatives': '1',
        'est_accessible': 'on',
        'form-TOTAL_FORMS': '1',
        'form-INITIAL_FORMS': '1',
        'form-MIN_NUM_FORMS': '0',
        'form-MAX_NUM_FORMS': '1000',
        'form-0-debut': '2024-10-10T13:45',
        'form-0-fin': '2024-12-12T12:00',
        'form-0-promo': plage.promo.id,
        'form-0-groupe': plage.groupe.id,
        'form-0-id': str(plage.id),
        'form-__prefix__-debut': '',
        'form-__prefix__-fin': '',
        'form-__prefix__-promo': '',
        'form-__prefix__-groupe': '',
        'form-__prefix__-id': '',
        'selected_questions': [str(q.id) for q in context.selected_question]
    }
    
    update_url = reverse('qcm-edit', kwargs={'pk': qcm.id})
    context.response = context.client.post(update_url, form_data)
    
@then(u'le QCM est mis à jour')
def step_impl(context):
   assert context.response.status_code in [200, 302], f"La mise à jour a échoué avec le code {context.response.status_code}"
   
   updated_qcm = QCM.objects.get(id=context.qcm.id)
   assert updated_qcm is not None, "Le QCM n'existe plus"

   assert updated_qcm.titre, "Le titre est vide"
   assert updated_qcm.description, "La description est vide" 
   assert updated_qcm.nb_tentatives > 0, "Le nombre de tentatives doit être supérieur à 0"

   assert updated_qcm.questions.exists(), "Aucune question n'est associée au QCM"

   plage = updated_qcm.plages.first()
   assert plage is not None, "La plage horaire n'existe plus"
   assert plage.debut is not None, "La date de début est vide"
   assert plage.fin is not None, "La date de fin est vide"
   assert plage.promo is not None, "Aucune promo n'est associée"
   assert plage.groupe is not None, "Aucun groupe n'est associé"
   
   print(f"Le QCM '{updated_qcm.titre}' a été mis à jour avec succès avec {updated_qcm.questions.count()} questions et une plage horaire configurée")

@when(u'je supprime un QCM')
def step_impl(context):
    context.qcm_id = context.qcm.id
    
    delete_url = reverse('qcm-delete', kwargs={'qcm_id': context.qcm.id})
    context.response = context.client.post(delete_url)

@then(u'le QCM est supprimé')
def step_impl(context):
    assert context.response.status_code in [200, 302], f"La suppression a échoué avec le code {context.response.status_code}"
    
    deleted_qcm_exists = QCM.objects.filter(id=context.qcm_id).exists()
    assert not deleted_qcm_exists, "Le QCM n'a pas été supprimé de la base de données"
    
    print("Le QCM a été supprimé avec succès")

@when(u'je consulte un QCM')
def step_impl(context):
    qcm_url = reverse('qcm-acces', kwargs={'qcm_id': context.qcm.id})
        
    context.response = context.client.get(qcm_url)

@then(u'le QCM est affiché')
def step_impl(context):
    assert context.response.status_code == 200, f"La page n'a pas été chargée correctement (status code: {context.response.status_code})"
    
    content = context.response.content.decode()
    assert context.qcm.titre in content, "Le titre du QCM n'est pas affiché"
    assert context.qcm.description in content, "La description du QCM n'est pas affichée"
    
    print(f"Le QCM '{context.qcm.titre}' est affiché correctement")