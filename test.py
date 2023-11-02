import pyttsx3

engine = pyttsx3.init("sapi5")

# Get a list of all available voices
voices = engine.getProperty('voices')

# Set the voice to use
engine.setProperty('voice', voices[2].id)
for voice in voices:
    print(voice.name)
# Speak the text
engine.say('أعلن البيت الأبيض عن ما وصفها')

# Wait for the text to be spoken
engine.runAndWait()