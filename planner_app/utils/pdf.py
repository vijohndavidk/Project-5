from django.http import HttpResponse

from reportlab.pdfgen import canvas

def export_pdf(text):


    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = (
        'attachment; filename="timetable.pdf"'
    )

    p = canvas.Canvas(
        response
    )

    y = 800

    p.setFont(
        "Helvetica",
        14
    )

    p.drawString(
        100,
        y,
        "AI Study Timetable"
    )

    y -= 50

    for line in text.split("\n"):

        p.drawString(
            80,
            y,
            line
        )

        y -= 25

    p.save()

    return response

