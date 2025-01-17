from behave import given, when, then

@given(u'j\'ai un support de cours (texte ou PDF)')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Given j\'ai un support de cours (texte ou PDF)')


@when(u'j\'envoie le support de cours pour analyse')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'envoie le support de cours pour analyse')


@then(u'des questions sont générées automatiquement')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then des questions sont générées automatiquement')