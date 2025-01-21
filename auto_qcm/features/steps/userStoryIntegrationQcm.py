from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
from django.conf import settings
import os

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
    response = context.client.get(f'/qcm/export-xml/{context.qcm.id}/')
    context.xml = response.content.decode('utf-8')
    assert response.status_code == 200

@then(u'j\'ai un qcm prêt à être importé dans Moodle')
def step_impl(context):    
    with open(os.path.join(context.dirFiles, 'qcm-xml.xml'), 'r', encoding='utf-8') as file:
        contenuFichier = file.readlines()
    assert contenuFichier == context.xml.splitlines()

@when(u'j\'exporte la question au format moodle xml')
def step_impl(context):
    response = context.client.get(f'/question/export-xml/{context.question.id}/')
    context.xml = response.content.decode('utf-8')
    assert response.status_code == 200


@then(u'j\'ai une question prête à être importé dans Moodle')
def step_impl(context):
    with open(os.path.join(context.dirFiles, 'question-xml.xml'), 'r', encoding='utf-8') as file:
        contenuFichier = file.readlines()
    assert contenuFichier == context.xml.splitlines()

@when(u'j\'exporte le qcm au format amc')
def step_impl(context):
    response = context.client.get(f'/qcm/export-latex/{context.qcm.id}/')
    context.latex = response.content.decode('utf-8')
    assert response.status_code == 200


@then(u'j\'ai un qcm au format AMC')
def step_impl(context):
    with open(os.path.join(context.dirFiles, 'qcm-latex.tex'), 'r', encoding='utf-8') as file:
        contenuFichier = file.read()
    assert contenuFichier.splitlines() == context.latex.splitlines()
    


@when(u'j\'exporte le qcm au format amc.txt')
def step_impl(context):
    response = context.client.get(f'/qcm/export-amctxt/{context.qcm.id}/')
    context.amctxt = response.content.decode('utf-8')
    assert response.status_code == 200
    


@then(u'j\'ai un qcm au format AMC.txt')
def step_impl(context):
    with open(os.path.join(context.dirFiles, 'qcm-amctxt.txt'), 'r', encoding='utf-8') as file:
        contenuFichier = file.read()
    assert contenuFichier.splitlines() == context.amctxt.splitlines()
    

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