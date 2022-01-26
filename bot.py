from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route('/mybot' , methods=['POST'])
def mybot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message
    responded = False
    
    if 'hi' in incoming_msg:
        # return msg ('hello' or 'welcome') to sender
        msg.body("Hello , i'm your bot")
        responded = True
    
    if 'quote' in incoming_msg:
        r = request.get('http://api.quotable.io/random')
        
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} , ({data["author"]})'
        
        else:
            quote = 'sorry iam unable to retrieve quote at this time, please try later'
        
        msg.body(quote)
        responded= True
    
    if 'who are you' in incoming_msg:
        msg.body('hi iam whatsapp bot')
        responded = True
    
    if not responded :
        msg.body('hi i can tell only about quotes and my identity')
        
    return str(response)


if __name__ == '__main__':
    app.run(debug=True)