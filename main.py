import pyttsx3

if __name__ == '__main__':
    print("Welcome To RoboSpeaker Created By Ritisha")
    while True:
        x = input("Enter what you want me to say: ")
        engine = pyttsx3.init()
        if x=="Q":
            break
       
        engine.say(x)
        engine.runAndWait()

    