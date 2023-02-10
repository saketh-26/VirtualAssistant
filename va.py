#Sending an automated email
#Create app password check the below link
#https://support.google.com/mail/answer/185833?hl=en

#Create our Virtual Assistant to perform tasks such as
#1)Conversation 2)Time related 3)Opening Desired web pages
#4)Locating Maps 5)Sending emails.....

#we need to install gtts,playsound,SpeechRecognition
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import uuid
import time
import webbrowser


def listen():
    """obtain audio from the microphone"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hey Guy start talking")
        audio = r.listen(source,phrase_time_limit=5)
    data=""
    try:
        data = r.recognize_google(audio,
                                  language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you speak louder")
    except sr.RequestError as e:
        print("Microphone is not working")
    return data
    #tts = gTTS(data)
    #tts.save("Speech.mp3")
    #playsound.playsound("Speech.mp3")
#listen() #dir(__builtins__)

#Respond function to give the response back
def respond(String):
    """Function for responding back"""
    tts = gTTS(text=String)
    tts.save("Speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#Now we will create our assistant to prform actions
def virtual_assistant(data):
    """give your actions"""
    if "how are you" in data:
        listening = True
        respond("I am good thank you")
    elif "time" in data:
        listening = True
        respond(time.ctime())
    elif "You thinking".lower() in data:
        listening = True
        respond("Yes about the weekend plan")
    elif "open google" in data.lower():
        listening = True
        url = "https://www.google.com/"
        webbrowser.open(url)
        respond("Success")
    elif "locate" in data:
        listening = True
        webbrowser.open(
            'https://www.google.com/maps/search/'+
            data.replace("locate",""))
        result = "Located"
        respond("Located {}".format(data.replace(
            "locate","")))
    elif "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen()
        edict = {'hello':'saketh@codegnan.com','new':''} #give mail ids
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject :{}\n\n{}'.format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        #login
        mail.login('','') #enter mailid and app password make sure you enable less secure app access
        mail.sendmail('',toaddr,content) #enter your gmail username
        mail.close()
        respond('Email Sent')
    elif "stop talking" in data:
        listening = False
        respond("Okay take care")
    try:
        return listening
    except:
        print("Stopped")
        
respond("Hey Codegnan this is your assistant")
listening = True
while listening == True:
    data = listen()
    listening = virtual_assistant(data)
    
    
    
  





    
