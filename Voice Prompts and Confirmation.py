import pyttsx3

engine = pyttsx3.init()

# Example prompts
engine.say("Please confirm your purchase:")
engine.say("Total amount: {}".format(total_amount))
engine.runAndWait()
