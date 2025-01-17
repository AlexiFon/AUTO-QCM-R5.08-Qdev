from behave import given, when, then

@given(u'j\'ai un QCM prêt à être intégré')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Given j\'ai un QCM prêt à être intégré')


@when(u'je synchronise le QCM avec Moodle ou AMC')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When je synchronise le QCM avec Moodle ou AMC')


@then(u'le QCM devrait apparaître automatiquement sur la plateforme')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then le QCM devrait apparaître automatiquement sur la plateforme')