from django.utils import timezone
from app.models import Question, QCM, Plage
from behave import when, then
from behave.api.pending_step import StepNotImplementedError
from django.urls import reverse

@when(u'je sélectionne une banque de questions')
def step_impl(context):
    # Création de questions fictives
    question1 = Question.objects.create(nom="Question 1", texte="Contenu 1", creator=context.user)
    question2 = Question.objects.create(nom="Question 2", texte="Contenu 2", creator=context.user)

    # Liste des IDs des questions sélectionnées
    selected_question = [question1, question2]

    qcm = QCM.objects.create(
                titre="QCM1",
                description="Description QCM1",
                date_modif=timezone.now(),
                creator=context.user
                )
    qcm.save()

    plage = Plage.objects.create(
                dateDeb=timezone.now(),
                dateFin=timezone.now(),
                qcm=qcm
                )
    plage.save()

    qcm.questions.set(selected_question)
    qcm.save()
    context.qcm = qcm
    context.selected_question= selected_question


@then(u'un QCM de contrôle est généré avec les questions sélectionnées')
def step_impl(context):
    # Vérification de l'existence du QCM dans la base de données
    qcm = QCM.objects.last()
    assert qcm is not None, "Aucun QCM n'a été créé."
    assert qcm.questions.count() == len(context.selected_question), (
        f"Le nombre de questions sélectionnées ({len(context.selected_question)}) "
        f"ne correspond pas au nombre dans le QCM ({qcm.questions.count()})."
    )
    print(f"Le QCM '{qcm.nom}' a été généré avec succès avec les questions sélectionnées.")