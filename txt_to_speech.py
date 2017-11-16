
from gtts import gTTS

import os
 
# The text that you want to convert to audio
mytext = 'Wannna Suck your boobs'

language = 'en'
 
a = gTTS(text=mytext, lang=language, slow=False)
a.save("welcome.mp3")
os.system("mpg321 welcome.mp3")