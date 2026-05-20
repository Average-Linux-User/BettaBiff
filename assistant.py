import os
import random
print("<o)))))><")
print("Biff Assistant Ver:1.0")
phrases = [
"glub",
"why do you look hungry",
"another satisfied request",
"I think I lost my fins",
"I am a fish",
"100% more fish",
"why is the water always so warm when you are nearby",
"Now 2% bug free",
"why is the water always so warm when you are nearby",
]
clean = [
"You clean the tank and the fish thanks you",
"you make the tank more dirty and the fish hates you <@)))))><",
"you trip and fall try again",
]
kill = [
"why",
"are we serious",
"come on",
"we can talk about this",
"...",
"sound of keyboard slamming on wall",
"sound of controller slamming aginst wall",
"Frustrated sounds",
]
game = [
"status=hungry",
"status=dirty",
"status=good",
]
print(random.choice(phrases))
while True:
    user= input("Fish:")

    if user == "hello":
        print("Glub")
        print("""
      o
       o
        <o)))))><""")
    elif user == "swim":
        print("I don't know how to swim.")
    elif user == "sudo":
        print("Not the terminal! You pingus")
    elif user == "notepad":
        print("One moment...")
        print("""
            .--.
            |__| .-------.
            |=.| |.-----.|
            |--| ||     ||
            |  | |'-----'| <o)))))><
            |__|~')_____('
              """)
        os.system("notepad.exe")
        print("One moment...")
    elif user == "sudo fish":
        print("Activating super user fish")
        print("""
               $
              <o)))))><""")
        print("Sudoooooooooooooo powers activate!!!!!!!")
    elif user == "explorer":
        print("One moment...")
        print("""
            .--.
            |__| .-------.
            |=.| |.-----.|
            |--| ||     ||
            |  | |'-----'| <o)))))><
            |__|~')_____('
              """)
        os.system("explorer.exe")
    elif user == "I am a fish":
        print("password")
        password = input("secretfish:")
        if password == "biff":
            print("Calling all fish to aisle four. Let's turn the world into a giant lake for all the fish of the world to swim in.")
        else:
            print("Invalid Password")
    elif user == "what":
        print("Um I said nothing about taking over the world?!")
    elif user == "future":
        print("I will add a fish img in the future")
    elif user == "cat":
        print("This is not linux nor a cat, stop saying that dreaded word!")
    elif user == "ask biff":
        print("One moment...")
        print("""
            .--.
            |__| .-------.
            |=.| |.-----.|
            |--| ||     ||
            |  | |'-----'| <o)))))><
            |__|~')_____('
              """)
        os.system (r'python "E:\coding\biffasistant\biff.py"')
    elif user == "question":
        print("One moment...")
        print("""
            .--.
            |__| .-------.
            |=.| |.-----.|
            |--| ||     ||
            |  | |'-----'| <o)))))><
            |__|~')_____('
              """)
        os.system (r'python "E:\coding\biffasistant\biff.py"')
    elif user == "search":
        print("One moment...")
        print("""
            .--.
            |__| .-------.
            |=.| |.-----.|
            |--| ||     ||
            |  | |'-----'| <o)))))><
            |__|~')_____('
              """)
        os.system ("python biff.py")
    elif user == "help":
        print("This is a digital Fish assistant. Ask biff will open up a custom 2B Ollama AI agent built of of Gemma4:2B You will need to install ollama in order to use this. Also eat exits the program. I will update this as necassary, but the rest of the commands are really just for entertainment so far. Try to type sudo,what,swim,sudo fish,I am a fish,feed,clean,view,I will return,profile . All of these are just for entertainment.")
    elif user == "2 fish":
        print("<o)))))><")
    elif user == "feed":
        print("Thanks for the food")
        print("<o)))))><")
    elif user == "eat":
        print("No please don't do that!")
        print("""
<x)))))><
              """)
        input("...")
        break
    elif user == "kill":
        print(random.choice(kill))
        print("""
<x)))))><
              """)
        print("R.I.P")
    elif user == "clean":
        print(random.choice(clean))
    elif user == "biff":
        print("""
        <@)))))><""")
        print("Yes sir, reporting for duty")
    elif user == "fish":
        print("""
        <@)))))><""")
        print("Yes sir, reporting for duty")
    elif user == "summon":
        print("Coming")
        print("""
        <o)))))><""")
    elif user == "view":
            print("""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                    
        <o)))))><
                  
                  <o)))))><
                <o)))))><
                                        <x)))))><

                  <o)))))><
            <o)))))><
                  

                    Biff
                  <o)))))><
                                    <x)))))><
        <x)))))><               <x)))))><
                  """)
    elif user =="I will return":
        print("I will be waiting! Don't take forever in the bathroom")
        print("<o)))))><")
        print("><(((((o>")
        print("When will this guy get back?!")
    elif user =="profile":
        print("My github profile link is https://github.com/Average-Linux-User ")
    elif user =="version":
        print("<o))))><")
        print("Betta Biff Version 1.0 2% bug free")
    else:
        print("Not a valid fish command. Type help")