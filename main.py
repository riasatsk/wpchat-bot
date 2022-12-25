import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)
position1 = pt.locateOnScreen("whatsapp/smile_clip.png", confidence=.8)
x = position1[0]
y = position1[1]

#Get Message
def get_message():
  global x,y

  position = pt.locateOnScreen("whatsapp/smile_clip.png", confidence=.8)
  x=position[0]
  y=position[1]
  pt.moveTo(x,y, duration=.5)
  pt.moveTo(x+50, y-65, duration=.5)
  pt.rightClick()
  pt.moveTo(x+80, y-305,)
  pt.doubleClick()
  whatsapp_message= pyperclip.paste()
  pt.click()
  print("Message Recived:"+whatsapp_message)
  return whatsapp_message

#posts
def post_response(message):
    global x, y

    position = pt.locateOnScreen("whatsapp/smile_clip.png", confidence=.8)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y +10, duration=.05)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n", interval=.01)


#process response
def process_response(message):
    random_no = random.randrange(3)
    
    if "?" in str(message).lower():
        return "Don't ask me any question!"

    else:
        if random_no == 0:
         return "That's Cool!"
        elif random_no==1:
            return "Hi I am AI"

        else:
           return "Save Water Save Tress" 




# check for new message
def check_for_new_message():
    pt.moveTo(x+50,y-50, duration=.01)

    while True:
      #continously checks for new messages
       try:
          positon= pt.locateOnScreen("whatsapp/active_dot.png", confidence=.8)

          if positon is not None:
              pt.moveTo(positon)
              pt.moveRel(-100, 0)
              pt.click()
              sleep(.5)
       except(Exception):  
             print("No New Messages")
       if pt.pixelMatchesColor(int(x+50), int (y-50), (255, 255, 255), tolerance = 10):
          print("is_white")
          processed_message = process_response(get_message())
          post_response(processed_message)

       else:
        print("No new messages")
        sleep(5)

check_for_new_message()
