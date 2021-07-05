import ctypes

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

i = bool()

while i == False:
    print("Ready to see a MessageBox? Input R if you're ready ou N if you're not")
    m = input()

    if m == "R" or m == "r":
        Mbox("Hello!", "Just testing things", 0)
        i = True

    elif m == "N" or m == "n":
        print("Ok then...")
        i = True
    else:
        Mbox("Input not available", "Please, choose only between N and R", 0)
        i = False
