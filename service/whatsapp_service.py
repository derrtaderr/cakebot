from db.order import Order
from infrastructure import app_secrets
from twilio.rest import Client

def send_cake_ready(order: Order):
    client = Client(username=app_secrets.twilio_sid, password=app_secrets.twilio_key)

    from_number = "whatsapp:+14155238886 "
    to_number = order.user.phone
    # Note: Message must confirm to a couple of template options:
    # check out: https://www.twilio.com/console/sms/whatsapp/sandbox
    message_body = f"Your cake order's status code is ready for pickup"

    resp = client.messages.create(to=to_number, from_=from_number, body=message_body)
    if resp.error_message:
        raise Exception(f"Cannot send whatsapp message: {resp.error_message}.")