from behave import when, then
from django.urls import reverse_lazy

@when(u'j\'accède au tableau de bord')
def step_impl(context):
    print(context.user.username)
    response = context.client.get(reverse_lazy('enseignant-dashboard', kwargs={'pk': context.user.pk}))  
    assert response.status_code == 200, "Impossible d'accéder au tableau de bord."
    context.response = response


@then(u'je vois les statistiques anonymisées ou personnalisées')
def step_impl(context):
    content = context.response.content.decode('utf-8')
    assert 'Voir les statistiques des QCM' in content, "Les statistiques ne sont pas affichées sur la page."

@then(u'je vois l\'historique des résultats des étudiants')
def step_impl(context):
    content = context.response.content.decode('utf-8')
    assert 'QCM avec vos questions' in content, "L'historique des résultats des étudiants n'est pas visible."
