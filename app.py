from flask import Flask, jsonify, request
import os
import requests
import config
app = Flask(__name__)


@app.route('/')
def main_page():
    ''' This is the main page of the site
    '''
    return 'Hello!'

@app.route('/v1/process',methods=['POST'])
def process():
    """ This is a call back from KaveNegar . will get sender and message and will check if it is valid 
    ,then answers back 
    """
    import pdb;pdb.set_trace()         #4 debug receive data from BTS <<data form is 'form' 4 access to data use request.form
    #data=request.json
    data = request.form
    sender = data ["form"]
    message = data["message"]
    print('received {message} from {sender}')
    send_sms(sender, 'Hi'+message)
    ret = { "message" : "processed"}
    return jsonify(ret), 200

def send_sms(receptor, message):
    """This function will get a MSISDN and a message, then uses KaveNegar to send sms.
    """
    url = f'https://api.kavenegar.com/v1/{config.API_KEY}/sms/send.json'
    data={"message":message,
            "receptor":receptor}
    res = requests.post(url,data)
    print(f"message <<{message}>> send. status code is {res.status_code}}")
def check_serial():
    pass

if __name__ == "__main__":
    send_sms('09212196193', 'Hi babe')
    app.run("0.0.0.0", 5000)


