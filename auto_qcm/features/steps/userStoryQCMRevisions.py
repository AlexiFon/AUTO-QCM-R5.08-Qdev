from behave import when, then
from behave.api.pending_step import StepNotImplementedError

@when(u'je saisis ou envoie des questions pour un QCM')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When je saisis ou envoie des questions pour un QCM')


@then(u'un QCM de révision hebdomadaire est créé')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then un QCM de révision hebdomadaire est créé')