from behave import given, when, then
from django.core.files.uploadedfile import SimpleUploadedFile
from behave.api.pending_step import StepNotImplementedError
from django.conf import settings
from app.models import Question
import os

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
    with open(os.path.join(os.path.join(settings.BASE_DIR, '..', 'features', 'steps', 'fichiersIntegration'), 'qcm-amctxt.txt'), 'r', encoding='utf-8') as file:
        contenuFichier = file.read()
    assert contenuFichier.splitlines() == context.amctxt.splitlines()
    
@given(u'j\'ai des questions Moodle XML à importer')
def step_impl(context):
    with open(os.path.join(settings.BASE_DIR, '..', 'features', 'steps', 'fichiersIntegration', 'qcm-xml.xml'), 'r', encoding='utf-8') as file:
        contenuFichier = file.read()
    context.xml = contenuFichier

@given(u'j\'ai des questions AMC à importer')
def step_impl(context):
    with open(os.path.join(settings.BASE_DIR, '..', 'features', 'steps', 'fichiersIntegration', 'qcm-latex.tex'), 'r', encoding='utf-8') as file:
        contenuFichier = file.read()
    context.latex = contenuFichier

@given(u'j\'ai des questions AMC.txt à importer')
def step_impl(context):
    with open(os.path.join(settings.BASE_DIR, '..', 'features', 'steps', 'fichiersIntegration', 'qcm-amctxt.txt'), 'r', encoding='utf-8') as file:
        contenuFichier = file.read()
    context.amctxt = contenuFichier


@when(u'j\'importe les questions au format moodle xml')
def step_impl(context):
    uploaded_file = SimpleUploadedFile('importfile.xml', context.xml.encode(), content_type='text/xml')
    question_data = {
        'import_type': 'moodle_xml',
        'file': uploaded_file
    }
    reponse = context.client.post('/question/import/', question_data)

    assert reponse.status_code == 200

@when(u'j\'importe les questions au format amc')
def step_impl(context):
    uploaded_file = SimpleUploadedFile('importfile.tex', context.latex.encode(), content_type='text/x-tex')
    question_data = {
        'import_type': 'latex_amc',
        'file': uploaded_file
    }
    reponse = context.client.post('/question/import/', question_data)

    assert reponse.status_code == 200


@when(u'j\'importe les questions au format amc.txt')
def step_impl(context):
    uploaded_file = SimpleUploadedFile('importfile.txt', context.amctxt.encode(), content_type='text/plain')
    question_data = {
        'import_type': 'amc_txt',
        'file': uploaded_file
    }
    reponse = context.client.post('/question/import/', question_data)

    assert reponse.status_code == 200


@then(u'j\'ai des questions importées de Moodle XML en base de données')
def step_impl(context):
    question = Question.objects.get(nom="Question1")

    assert question is not None
    assert question.texte == "<p dir=\"ltr\" style=\"text-align: left;\">Texte<br></p>"

@then(u'j\'ai des questions importées de AMC en base de données')
def step_impl(context):
    question = Question.objects.get(nom="Question1")

    assert question is not None
    print(question.texte)
    assert question.texte.strip() == "Texte"

@then(u'j\'ai des questions importées de AMC Txt en base de données')
def step_impl(context):
    question = Question.objects.get(nom="Texte :")

    assert question is not None
    assert question.texte == "Texte :"