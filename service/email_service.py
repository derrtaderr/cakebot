import base64
import uuid
from pathlib import Path
from typing import Optional

import html2text
import jinja2
import python_http_client.client
import sendgrid
from pdfkit import pdfkit

from db.order import Order
key_name: Optional[str] = None
api_key: Optional[str] = None

def send_cake_order_receipt(order: Order):
    client = sendgrid.SendGridAPIClient(api_key)
    # gather email details: name, email and so on.
    from_email = sendgrid.From('jason@localmarketingtakeover.com', 'Jason Derr')
    to_email = sendgrid.To(order.user.email, order.user.name)
    subject = sendgrid.Subject("Your order receipt from Cake Time")

    html = build_html('email/receipt.html', {'order': order})
    text = html2text.html2text(html)

    invoice_html = build_html("email/invoice.html", {'order': order})

    message = sendgrid.Mail(from_email, to_email,subject, text, html)
    # TODO: build pdf invoice
    # TODO: generate HTML content
    # TODO: attach the invoice to the email
    attachment = sendgrid.Attachment()
    attachment.file_content = pdf
    attachment.disposition = "attachment"
    attachment.file_type = "application/pdf"
    attachment.file_name = f"cake-city-invoice-{order.id}.pdf"


    # Send the email
    message = sendgrid.Mail(from_email, to_email, subject, text, html)
    message.add_attachment(attachment)
    response = python_http_client.client.Response = client.send(message)

    if response.satus_code not in {200, 201, 202}:
        raise Exception(f"Error sending email: {response.satus_code}")
    print(f"Sent email successfully: Order {order.id} to {order.user.name} at {order.user.email}")

def build_pdf(html: str) -> str:
    # Requires install from https://wkhtmltopdf.org/ in addition to pdfkit.
    temp_file = Path(__file__).parent.parent / (str(uuid.uuid4()) + ".pdf")

    pdfkit.from_string(html, str(temp_file))
    pdf_bytes = temp_file.read_bytes()

    temp_file.unlink()

    encoded_pdf = base64.b64encode(pdf_bytes).decode('ascii')
    return encoded_pdf


def build_html(template_file: str, data: dict) -> str:
    template_folder = str(Path(__file__).parent.parent / "templates")
    loader = jinja2.FileSystemLoader(template_folder)
    env = jinja2.Environment(loader=loader)

    template: jinja2.Template = loader.load(env, template_file, None)
    html = template.render(**data)

    return html