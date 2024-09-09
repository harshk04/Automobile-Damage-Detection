from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as ReportLabImage, Spacer, Table, TableStyle

def generate_pdf(car_details, prediction_json, total_price, price_details, image_path):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add title
    title_style = styles['Title']
    elements.append(Paragraph("Automobile Damage Inspection Report", title_style))

    # Add image
    elements.append(Spacer(1, 20))
    image = ReportLabImage(image_path, width=400, height=200)
    elements.append(image)

    # Add car details
    elements.append(Spacer(1, 20))
    car_info_title = Paragraph("Car Information:", styles['Heading2'])
    elements.append(car_info_title)

    car_info_data = [
        ['Registration No.', car_details['Registration']],
        ['Brand', car_details['Car Brand']],
        ['Model', car_details['Model']],
        ['Body Color', car_details['Colour']],
        ['Body Style', car_details['Type']],
        ['Fuel Type', car_details['Fuel']],
        ['Registration Year', car_details['Year of Manufacture']],
        ['Resell Value', car_details['Car Price']]
    ]
    car_info_table = Table(car_info_data)
    car_info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))
    elements.append(car_info_table)

    # Add damage estimations
    elements.append(Spacer(1, 20))
    damage_title = Paragraph("Damage Estimations:", styles['Heading2'])
    elements.append(damage_title)

    damage_data = [['Damage Type', 'Damage Percent' , 'Estimated Cost']]
    for detail in price_details:
        damage_data.append([ detail[1], f"{detail[0] * 100:.0f}%", f"{detail[2]:.2f}"])

    damage_table = Table(damage_data)
    damage_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))
    elements.append(damage_table)

    # Add total price
    elements.append(Spacer(1, 20))
    total_price_paragraph = Paragraph(f"Total Estimated Cost (INR): {total_price:.2f}", styles['Heading2'])
    elements.append(total_price_paragraph)

    doc.build(elements)
    buffer.seek(0)

    return buffer
