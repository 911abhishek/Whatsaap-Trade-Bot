from flask import Flask
from flask import request
from twilio.rest import Client
import os
from tradeBot import stockPrice
app = Flask(__name__)

acc_id ="ACcb847091a1e70b8e360f1de14be38220" 
#ACcb847091a1e70b8e360f1de14be38220
acc_token ='771a225db26f6541bf3a62b92882b141' 
#771a225db26f6541bf3a62b92882b141
twilio_number = "whatsapp:+14155238886"
#+14155238886

def send_msg(msg, recepient):
    cleint.messages.create(
        from_=twilio_number,
        body=msg,
        to=recepient
    )

cleint = Client(acc_id,acc_token)

def process_msg(msg, sender):
    response = ""
    if msg == "Hi":
        response = (f"Hello, Gandu {sender}")
        response +="\nTo get stock value :-\n$tk 'Name of the stock'\nTry: $tk ZOMATO"
    elif "$tk" in msg:
        stock ,name = msg.split(" ")
        stk_price = stockPrice(str(name))

        response = (f"{name} = {stk_price}")
    else:
        response = "Invalid Command Chodu"
    return response

@app.route("/webhook", methods=["POST"])
def webhook():
    # import pdb
    # pdb.set_trace()
    f = request.form
    msg = f['Body']
    sender = f['From']
    name = f['ProfileName']
    response = process_msg(msg, name)
    send_msg(response,sender)
    return "OK", 200
# ticker = str(input())
# exchange = str(input())
# # y = str("Bom")
# s = stockPrice(str(ticker),str(exchange))
# print(s)
# print("abhishek")

