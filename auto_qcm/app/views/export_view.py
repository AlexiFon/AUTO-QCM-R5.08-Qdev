from app.decorators import teacher_required
from app.models import QCM, Question
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


@login_required(login_url="login")
@teacher_required
def export_question_xml(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    xml_content = question.convertToXmlSingle()

    response = HttpResponse(xml_content, content_type="application/xml")

    response[
        "Content-Disposition"
    ] = f'attachment; filename="question_{question_id}.xml"'

    return response


@login_required(login_url="login")
@teacher_required
def export_qcm_xml(request, qcm_id):
    qcm = get_object_or_404(QCM, id=qcm_id)

    xml_content = qcm.convertToXml()

    response = HttpResponse(xml_content, content_type="application/xml")

    response["Content-Disposition"] = f'attachment; filename="qcm_{qcm_id}.xml"'

    return response


@login_required(login_url="login")
@teacher_required
def export_qcm_latex(request, qcm_id):
    qcm = get_object_or_404(QCM, id=qcm_id)

    latex_content = qcm.convert_to_latex()

    response = HttpResponse(latex_content, content_type="application/x-latex")

    response["Content-Disposition"] = f'attachment; filename="qcm_{qcm_id}.tex"'

    return response


@login_required(login_url="login")
@teacher_required
def export_qcm_amctxt(request, qcm_id):
    qcm = get_object_or_404(QCM, id=qcm_id)
    amc_content = qcm.convertToAmcTxt()
    response = HttpResponse(amc_content, content_type="application/x-amc")
    response["Content-Disposition"] = f'attachment; filename="qcm_{qcm_id}.txt"'
    return response
