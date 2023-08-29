import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
import smtplib
import pywhatkit as kit





engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


author=input("enter your name")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good morning{author},")
    elif hour>=12 and hour<15:
        speak(f"Good afternoon{author},")
    elif hour>=15 and hour<18:
        speak(f"good evening{author}")
    else:
         speak(f"good night {author}")
    speak(f"welcome{author},How can I help you????????")


def record_audio():
     #record
     r = sr.Recognizer() #creating recognizer object

     #open the mic and record

     with sr.Microphone() as source:
         print('say somthing!')
         audio = r.listen(source,phrase_time_limit=8)



     #use google speech recognition
     data = ''
     try:
         data = r.recognize_google(audio,language= 'en-in')
         print(f"{author} said: "+data)
     except sr.UnknownValueError:
         print('cant understand the audio !')
     except sr.RequestError as e:
         print('request results from google speech recognition service error '+ e)


     return data

def send_email(subject, message, to):
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your email account
    server.login("your_email-address", "your_password")

    # Create the email
    email_message = f"Subject: {subject}\n\n{message}"

    # Send the email
    server.sendmail("", to, email_message)

    # Close the server
    server.quit()

def send_whatsapp_message(phone_number, message):
    kit.sendwhatmsg_instantly(phone_number, message)






if __name__=="__main__":
    speak(f"welcome {author},I am  tanmoy saha the attitude king")
    wishMe()
    record_audio()
    while True:
        query = record_audio().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results) 

        elif 'news' in query:

            

                speak("news headlines")
                query = query.replace("news", "")
                link = "https://newsapi.org/v2/top-headlines?country=in&apiKey=5bd71c697bb94352bff0048587a1c006"
                news = requests.get(link).text
                news = json.loads(news)
                art = news['articles']

                for article in art:


                    print(article['title'])
                    speak(article['title'])

                    print(article['description'])
                    speak(article['description'])
                    speak("moving on to next news")
        elif 'open gooogle' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'search browser' in query:
            speak("what should I search????....")
            m = record_audio.lower()
            webbrowser.open(f"{m}")
        
        elif 'ip address' in query:
            ip = requests.get('http://api.ipify.org').text
            speak()

        elif 'send email' in query:
            speak("What should the subject be?")
            email_subject = record_audio().lower()
            speak("What message should I send?")
            email_message = record_audio().lower()
            speak("To whom should I send the email?")
            email_to = input("enter the email address whom do you want to send")
            send_email(email_subject, email_message, email_to)
            speak("Email sent successfully!")

        elif 'send whatsapp' in query:
            speak("What message should I send?")
            whatsapp_message = record_audio().lower()
            speak("To whom should I send the WhatsApp message?")
            whatsapp_recipient = input("enter the number whom do you want to send message ")  # Replace with the recipient's phone number
            send_whatsapp_message(whatsapp_recipient, whatsapp_message)
            speak("WhatsApp message sent successfully!")            
            
        
               

               
             
            




