
from gtts import gTTS


import os

mytext = 'lmao on'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("lamao.mp3")

# Playing the converted file
os.system("afplay welcome.mp3")