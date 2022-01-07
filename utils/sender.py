from twilio.rest import Client

def smsSend():
    client = Client("AC666143db39bcd40ab05659a005731f28","151deb9b50a893ba3501d8cb73304d1a")
    client.messages.create(to = ["+261347231032"] , from_ = "+12242434814" , body = "ALERT INTRUSION!!!")

def telegramSend():
    pass

