from twilio.rest  import Client
import speech_recognition as sr 
import pyaudio
import webbrowser




TWILIO_PHONE_NUMBER = "+xx xx xxxxx"


DIAL_NUMBERS = ["+91 xxxxx xxxxx"]

text = ["None"]
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"



client = Client("use twilio credentials", "auth token")


def dial_numbers(numbers_list):
    
    for number in numbers_list:
        print("Dialing " + number)
        
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    
  
    init_rec = sr.Recognizer()
    print("Attendance Checker is online you can go sleep")
    while True:

     with sr.Microphone() as source:
        try:
         audio_data = init_rec.record(source,duration=5)
         print("............")
         text = init_rec.recognize_google(audio_data)
         text = text.split(' ')
        except NameError:
            None
        except AttributeError:
            None
        except sr.UnknownValueError:
            None
        print(text)
        for i in text:
                if(i == '650'or i == '651'or i == '652'or i == '653'or i == '654'or i == '655'or i == '656'or i == '657'or i == '658'or i == '659'or i == '660'or i == '661'or i == '662'or i == '663'or i == '664'or i == '665'or i == '666'or i == '667'or i == '668'or i == '669'or i == '670'or i == '671'or i == '672'or i == '673'or i == '674'or i == '675'or i == '676'or i == '677'or i == '678'or i == '679'or i == '680'or i == '681'or i == '682'or i == '683'or i == '684' or i =='present sir' or i == 'present'):
                    print("Attendance is being taken")
                    dial_numbers(DIAL_NUMBERS)
                    print(text)
                    
