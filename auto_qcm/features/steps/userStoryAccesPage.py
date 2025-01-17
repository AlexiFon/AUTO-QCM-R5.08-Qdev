from behave import when, then


@when(u'je tente d\'accéder à une page destinée aux étudiants')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When je tente d\'accéder à une page destinée aux étudiants')


@when(u'je tente d\'accéder à une page destinée aux enseignants')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When je tente d\'accéder à une page destinée aux enseignants')


@then(u'je devrais voir le contenu de la page')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then je devrais voir le contenu de la page')
