from behave import when, then
from behave.api.pending_step import StepNotImplementedError

@when(u'j\'accède au tableau de bord des résultats')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'accède au tableau de bord des résultats')


@then(u'je vois les statistiques anonymisées ou personnalisées')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then je vois les statistiques anonymisées ou personnalisées')

@then(u'je vois l\'historique des résultats des étudiants')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then je vois l\'historique des résultats des étudiants')