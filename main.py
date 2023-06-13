import os
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

if __name__ == '__main__':
    print("Welcome!")
    while True:
        x = input("Enter the sentence: ")
        # say is command for only mac os
        command = f"say {x}"
        if x == "q":
            break
        speak.Speak(command)
