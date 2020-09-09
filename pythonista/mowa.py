'''PyTDM's version for Pythonista'''

import speech
# relative vs non relative import bs
try:
	from translacja import tłumacz
except ModuleNotFoundError:
	from .translacja import tłumacz



# engine = pyttsx3.init()

def say(s):
	speech.say(s)
	# engine.runAndWait()


def mów(s):
	# apple's text to speech doesn't handle all those signs apart from commas too well
	s_corrected = s.replace(".", ",").replace("!", ",").replace(":", ",").replace("?", ",")
	translated = tłumacz(s_corrected.lower())
	print(s)
	say(translated)
