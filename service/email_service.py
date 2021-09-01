from typing import Optional

import python_http_client.client
import sendgrid

from db.order import Order
key_name: Optional[str] = None
api_key: Optional[str] = None

def send_cake_order_receipt(order: Order):
    client = sendgrid.SendGridAPIClient(api_key)
    # gather email details: name, email and so on.
    from_email = sendgrid.From('jason@localmarketingtakeover.com', 'Jason Derr')
    to_email = sendgrid.To(order.user.email, order.user.name)
    subject = sendgrid.Subject("Your order receipt from Cake Time")
    html = "<h1> Your Receipt</h1>\n<br>\n<br> Thanks for ordering your " \
            f"{order.size} {order.flavour} cake."
    text =  "Your Receipt\n\nThanks for ordering your " \
            f"{order.size} {order.flavour} cake."
    message = sendgrid.Mail(from_email, to_email,subject, text, html)
    # TODO: build pdf invoice
    # TODO: generate HTML content
    # TODO: attach the invoice to the email
    # Send the email
    response = python_http_client.client.Response = client.send(message)

    if response.satus_code not in {200, 201, 202}:
        raise Exception(f"Error sending email: {response.satus_code}")
    print(f"Sent email successfully: Order {order.id} to {order.user.name} at {order.user.email}")


    message= sendgrid.Mail()
    print(f"Will send email confirmation about {order} to {order.user.name} ")