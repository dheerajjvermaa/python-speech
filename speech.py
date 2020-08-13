
# importing the pyttsx library 
import pyttsx3 
  
# initialisation 
engine = pyttsx3.init() 
newVoiceRate = 90
engine.setProperty('rate',newVoiceRate)
# testing 
engine.say("I am a High-functioning Sociopath") 

engine.runAndWait() 

#notification #notification #notification #notification #notification
#notification #notification #notification #notification #notification

print("SEE NOTIFICATION")

from plyer import notification
def notify(title, message):
     notification.notify(
          message = message,
          title = title,
          app_icon = None,
          timeout = 3
     )
if __name__ == "__main__":
    notify("Dheeraj Verma", "High-functioning Sociopath")
