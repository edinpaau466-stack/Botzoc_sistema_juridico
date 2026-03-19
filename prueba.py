from twilio.rest import Client

account_sid = 'AC4bbaabd025c76815329024eda570fcf7'
auth_token = '8391a5a29470b35cef02fe0ce9504b8a'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="PRUEBA WHATSAPP 🔥",
    from_='whatsapp:+14155238886',
    to='whatsapp:+50258253400'
)

print(message.sid)
