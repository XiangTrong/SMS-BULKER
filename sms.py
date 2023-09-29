import re
import conf
import requests

class SendSMS:
    def __init__(self):
        self.api_key      = conf.VONAGE_API_KEY
        self.api_secret   = conf.VONAGE_API_SECRET
        self.from_number  = conf.FROM_NUMBER
        self.base_url     = r"https://rest.nexmo.com/sms/json"
    
    def sanitize_mobile_number(self, mobile):
        mobile1 = None
        try:          
            mobile1 = re.sub('\D', '', mobile)            
        except Exception as e:
            print(str(e))        
        return mobile1

    def send_sms_message(self, message, to_number):        
        ret = {}
        ret['success'] = False
        try:  
         
            param = {}
            param['api_key']    = self.api_key
            param['api_secret'] = self.api_secret
            param['from']       = self.from_number
            param['text']       = message
            param['to']         = self.sanitize_mobile_number(to_number)           

            response = requests.get(self.base_url, params=param)   #{'messages': [{'to': '917829713845', 'message-id': 'b7b9383-ffff-409e-a7c5-1744ced3000e', 
                                                                   #    'status': '0', 
                                                                   #    'remaining-balance': '1.95860000', 'message-price': '0.04140000', 'network': '405862'}], 
                                                                   #   'message-count': '1'}

            print(response)
            print(response.status_code)
            if response.status_code == 200:
                json_response = response.json()

                if 'messages' in json_response:
                    ret['message_id'] = json_response[0]['message-id']
                    ret['success'] = True          

        except Exception as e:
            print(str(e))

        return ret

def main():
    
    otp_code = 123456
    message = f"Nigga test: {otp_code}"
    
    to_number = '+639702458106'
    to_number = '+639185857866'
    obj = SendSMS()
    ret = obj.send_sms_message(message, to_number)
    print(ret)
    
if __name__ == '__main__':
    main()
    print("Done")