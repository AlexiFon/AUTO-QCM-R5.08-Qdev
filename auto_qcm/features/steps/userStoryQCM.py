from behave import  when, then
from behave.api.pending_step import StepNotImplementedError

@when(u'je démarre un QCM')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When je démarre un QCM')


@then(u'je peux répondre aux questions à mon rythme')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then je peux répondre aux questions à mon rythme')