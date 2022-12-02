import webbrowser
from appscript import app
import time

encodedMessage = ""
number = []#list of phone numbers
print(len(number))
for no in number:

    if len(no) == 13:
        webbrowser.open("https://wa.me/"+no[1:]+"?text="+encodedMessage )
    elif len(no) == 12:
        webbrowser.open("https://wa.me/"+no+"?text="+encodedMessage )
    elif len(no) == 11:
        webbrowser.open("https://wa.me/91"+no[1:]+"?text="+encodedMessage )
    elif len(no) == 10:
        webbrowser.open("https://wa.me/91"+no+"?text="+encodedMessage )
    #set the delay time
    time.sleep(7)
    #default for mac , change for windows by changing keystroke
    app('System Events').keystroke('\r')
