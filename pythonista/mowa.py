"""PyTDM's version for Pythonista ie. iOS"""

import speech

# relative vs non relative import bs
try:
    from translacja import tłumacz
except ModuleNotFoundError:
    from .translacja import tłumacz


def say(s, lang=None):
    if lang:
        speech.say(s, lang)
    else:
        speech.say(s)


def mów(s, lang="en", show=True):
    # apple's text to speech doesn't handle all those signs apart from commas too well
    s_corrected = (
        s.replace(".", ",").replace("!", ",").replace(
            ":", ",").replace("?", ",")
    )
    langs = {"en": "en_US", "fr": "fr_FR"}
    if show:
        print(s)
    if lang in langs:
        translated = tłumacz(s_corrected.lower(), lang)
        say(translated, langs[lang])
    else:
        print("%s not among avalaible languages, using the default" % lang)
        translated = tłumacz(s_corrected.lower())
        say(translated)


# english keyboardz
mow = mów
tlumacz = tłumacz
