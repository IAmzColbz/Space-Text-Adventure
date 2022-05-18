#Colby & Connor
#Text Based Adventure
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

def cont():
    gotonext = "stay"
    while gotonext == "stay":
        print("Press 'Enter' to continue...")
        ans = input()
        if ans == "":
            gotonext = "continue"
            cls()

def introduction():
    print("""Welcome traveler! You're about to set forth on a grand adventure!
    But first, we must learn your name. Who are you?""")
    introduction.name = input("\t>>>")
    cls()
    print(f"Good, {introduction.name}. That name will do nicely.")
    cont()

def backstory():
    print(f"""My name is {introduction.name}. I am an 'indentured servant' aboard the Galactic Zorda.
    I have always considered myself a slave, but the ship owners call me 'servant' to avoid
    being prosecuted under intergalactic law, which prohibits slavery. The Zorda was built in 
    year 3388 when Jefferson Davis commissioned the ship to transport his, 'assets.'
    Jefferson was also a well known and feared politician of the galactic empire, who dabbled in slave trade
    and commandeering 'unlicenced' peasant trade ships.""")
    cont()
    print("""The ship is now owned by his son, Robert E. Davis III, almost 50 years later. I was imprisoned
    8 years ago today and spent 6 of those years on a empire sanctioned prison planet named ConV71.
    However 6 years into my 20 year prison sentence, I was misplaced by the warden. I found myself tied and
    gagged in the back of a windowless transport van with 5 others. I only knew this after they opened the 
    van doors to show off the slavers newest subjects. They pulled us out of the back of the van by the 
    backs of our tattered prison rags, letting us hit the ground with little regard or care.""")
    cont()
    print("""After exchanging a few plasteele cards that worked as a form of underground currency, they dragged 
    us into their hulking transport ship. It's thrusters alone  where larger than my old home. This was the
    start of the next 2 years of my life where beatings were common, food was scarce, death was common, and hope
    was lost. I spent my fair share of time sitting on the steel flooring of the cell I was thrown into wonder what
    life could have been. If I didn't speak out against Jefferson and his underhanded practices. My article was 
    evaporated from the newstream before it the eyes of a single person, and thus my arrest was swift yet quiet.""")
    cont()

def escape_decide():
    print("""That Brings me to today, sitting on cold steel grating, half starving, half beaten. I am going to die
    in here. I'll starve. I'll disappear when the slavers don't think I'm productive enough. I'll be dropped into
    the void of space with no more than my brittle bones and searing hatred.""")
    cont()
    print("I need out")
    cont()
    print("""But... if I try to escape... Ill probably get caught, and they torture deserters... I can stick out my
    sentence. I Know I can survive, but it'll be hard...""")
    cont()

    ans = True

    while ans == True:
        c1 = input("Should I 'Escape' or should I 'Stay?'\n\t>>>")
        if c1.lower() == "escape" or c1.lower() == "leave":
            escape_decide.bgc = "escape"
            cls()
            ans = False
        elif c1.lower() == "stay":
            escape_decide.bgc = 'stay'
            cls()
            ans = False
        else:
            cls()
            print("This is important, I need to say it. 'Escape' or 'Stay'?")

def escaping():
    print("""Its decided then. Its time to escape. I pull my decrepid body to its feet and nearly double over 
    with nausia, but stood straight and managed to keep what little bile I had down. I looked around me for 
    something that may provide usefull to my ventures, deciding the vastness of nothing wouldn't help much.
    I pressed my body to the cell bars, basking in the cool dark air outside in the block. It's probably around
    midnight judging by the guard rotation""")



introduction()
backstory()
escape_decide()
if escape_decide.bgc == 'escape':
    escaping()
elif escape_decide.bgc == 'stay':
    print('you stay and die debug')