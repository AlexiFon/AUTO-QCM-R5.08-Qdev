from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError


@given(u'j\'ai des questions Moodle XML à importer')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Given j\'ai des questions à importer')

@given(u'j\'ai des questions AMC à importer')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Given j\'ai des questions à importer')

@given(u'j\'ai des questions AMC.txt à importer')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Given j\'ai des questions à importer')

@when(u'j\'exporte le qcm au format moodle xml')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'exporte le qcm au format moodle xml')


@then(u'j\'ai un qcm prêt à être importé dans Moodle')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then j\'ai un qcm prêt à être importé dans Moodle')

@when(u'j\'exporte la question au format moodle xml')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'exporte la question au format moodle xml')


@then(u'j\'ai une question prête à être importé dans Moodle')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then j\'ai une question prête à être importé dans Moodle')

@when(u'j\'exporte le qcm au format amc')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'exporte le qcm au format amc')


@then(u'j\'ai un qcm au format AMC')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then j\'ai un qcm au format AMC')


@when(u'j\'exporte le qcm au format amc.txt')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'exporte le qcm au format amc.txt')


@then(u'j\'ai un qcm au format AMC.txt')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then j\'ai un qcm au format AMC.txt')

@when(u'j\'importe les questions au format moodle xml')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'importe les questions au format moodle xml')

@when(u'j\'importe les questions au format amc')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'importe les questions au format amc')


@when(u'j\'importe les questions au format amc.txt')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: When j\'importe les questions au format amc.txt')


@then(u'j\'ai des questions prêtes à être utilisées dans un QCM')
def step_impl(context):
    raise StepNotImplementedError(u'STEP: Then j\'ai des questions prêtes à être utilisées dans un QCM')