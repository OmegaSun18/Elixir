print("WELCOME TO YOUR PREDIRE (PREDICTIONS)")
print("")
print("Come one come all !!!!!!!!!")
print("Get to know what life holds for you.")
print("I- *cough*")
print("I mean 'we' use numerology, alphabets and fake astrology to make the most efficient predictions about you and your life.")
print("Come and immerse yourself in the world of predictions!!!!!!!")
print("       ")
print("Please cooperate with me and fill in the below details:")
print("Please enter your perso- *cough*")
print("Your DATA, please make sure not to enter any spaces.")
print("            ")

#-------------------------Program Start------------------------------------------------------------------
#--------------------------------------------------NAME
import random
import sys
List1=[]
Name=input("Please enter only your first name: ")
print("             ")
useless1=0
a=b=cctr=iqtr=0
l=len(Name)
if Name=="X Æ A-12":
    l=8
    l1=l
    print("You're not Elon Musk's son, but for your fantasy i shall allow it")
    print("")
else:
    while useless1<=l or cctr==3:
        if useless1==l and useless1>0:
            break
        elif l==0 or Name[useless1].isdigit():
            print("You lack the basic human intelligence to differ between names and digits. Dummy.")
            print("")
            Name=input("Please enter only your first name: ")
            print("")
            l=len(Name)
            useless1=0
            cctr=0
            iqtr=1
        elif l==0 or Name[useless1].isspace():
            print("I thought I said not to put spaces in your name. Or can you not read??? ")
            print('')
            Name=input("Please enter only your first name: ")
            print("")
            l=len(Name)
            useless1=0
            cctr=0
            tiqr=1
        elif l<3:
            print("Please for god's sake enter a proper name !!!!.")
            print('')
            Name=input("Please enter only your first name: ")
            print("")
            l=len(Name)
            useless1=0
            cctr=0
            iqtr=1
        elif cctr==3:
            print("That's not a name.")
            print("")
            Name=input("Please enter only your first name: ")
            print("")
            l=len(Name)
            useless1=0
            cctr=0
            iqtr=1
        else:
            if Name[useless1] not in ["a","e","i","o","u","y"]:
                cctr+=1
            else:
                cctr=0
                iqtr=1
            useless1=useless1+1
           
    for placeholder1 in Name:
        if placeholder1.isalpha():
            List1.append(placeholder1)
    l1=len(List1)
#______Randomiser1_____________

if l1 in range(0,5):
    a=random.randint(0,l1)
elif l1 in range(5,10):
    a=random.randint(0,10)
elif l1 in range(10,15):
    a=random.randint(0,l1)
elif l1 in range(15,20):
    a=random.randint(0,20)
elif l1 in range(20,25):
    a=random.randint(0,l1)
elif l1 in range(25,30):
    a=random.randint(0,30)
elif l1 in range(30,35):
    a=random.randint(0,l1)
else:
    a=random.randint(0,40)


if a in range(0,7):
    b=random.randint(0,9)
elif a in range(7,14):
    b=random.randint(0,18)
elif a in range(14,21):
    b=random.randint(0,27)
elif a in range(21,28):
    b=random.randint(0,36)
elif a in range(28,35):
    b= random.randint(0,45)
else:
    b=random.randint(0,a)
#----------------------------------------------------------AGE
Age=input("Please enter your age: ")
print("")
l4=len(Age)
useless3=useless4=0
while useless3<=l4:
    if useless3==l4 and useless3>0:
        break
    try:
        useless4=int(Age)
        if l4==0 or useless4<=0 or useless4>=122:
            print("Please enter your actual age, because we both know that you don't have a time machine.")
            print("")
            iqtr=iqtr+1
            Age=input("Please enter your age: ")
            print("")
            l4=len(Age)
            useless3=0
        else:
            useless3+=1
    except:
        if useless3>0 and useless3==l4:
            break
        if l4==0 or Age[useless3].isalpha():
            print("You lack the basic human intelligence to differ between age and letters. Dummy.")
            print("")
            iqtr=iqtr+1
            Age=input("Please enter your age: ")
            print("")
            l4=len(Age)
            useless3=0
        elif Age[useless3].isspace():
            print("Please don't tell me that you don't even know your own age.")
            print("")
            iqtr=iqtr+1
            Age=input("Please enter your age: ")
            print("")
            l4=len(Age)
            useless3=0
        else:
            useless3+=1
Age=int(Age)
#=========================FAV COLOUR
Colour=input("Please enter your favourite colour: ")
print("  ")
l2=len(Colour)
List2=[]
useless2=cctr1=0
while useless2<=l2:
    if useless2==l2 and useless2>0:
        break
    if l2==0 or Colour[useless2].isdigit():
        print("You lack the basic human intelligence to differ between colours and digits. Dummy.")
        print("")
        iqtr=iqtr+1
        Colour=input("Please enter your favourite colour: ")
        print("")
        l2=len(Colour)
        useless2=0
        cctr1=0
    elif l2==0 or Colour[useless2].isspace():
        print("Stop. Just stop.")
        print("")
        iqtr=iqtr+1
        Colour=input("Please enter an actual colour: ")
        print("")
        l2=len(Colour)
        useless2=0
        cctr1=0
    elif l2<3:
        print("There is no colour with a name less than 3 letters. And yes I may have googled it.")
        print("")
        iqtr=iqtr+1
        Colour=input("Please enter an actual colour: ")
        print("")
        l2=len(Colour)
        useless2=0
        cctr1=0
    elif cctr1==3:
        print("That's not a colour!!!!!!!!")
        print("")
        iqtr=iqtr+1
        Colour=input("Please enter an actual colour: ")
        print("")
        l2=len(Colour)
        useless2=0
        cctr1=0
    else:
        if Colour[useless2]  not in ["a","e","i","o","u","y"]:
            cctr1+=1
        else:
            cctr1=0
        useless2+=1

for placeholder2 in Colour:
    if placeholder2.isalpha():
        List2.append(placeholder2)
l3=len(List2)

#_________________Randomiser2____________________
c=d=e=0

c=l3%3
if c>0:
    d=Age*l3
    if d in range(0,15):
        e=random.randint(0,12)
    elif d in range(15,30):
        e=random.randint(12,24)
    elif d in range(30,45):
        e=random.randint(24,36)
    elif d in range(45,60):
        e=random.randint(36,48)
    elif d in range(60,75):
        e=random.randint(48,60)
    elif d in range(75,90):
        e=random.randint(0,60)
    else:
        e=random.randint(0,Age)
else:
    d=Age//l3
    if d==0:
        e=random.randint(0,30)
    else:
        e=random.randint(30,60)
#-----------------------------------------------------------HEIGHT

Height=input("Please enter your height in cm(If you don't know please enter UK): ")
print("")
l5=len(Height)
useless5=useless6=0
while useless5<=l5:
    try:
        useless6=int(Height)
        if l5==0 or useless6<=0 or useless6>=272 or useless6<=53:
            print("What are you??? A Dwarf!!??? A Giant!!???")
            print("")
            iqtr=iqtr+1
            Height=input("Please enter your height in cm (If you don't know please enter UK): ")
            l5=len(Height)
            useless5=0
        else:
            useless5+=1
    except:
        if l5==0 or Height!="UK":
            print("If you don't know your height please just enter UK.")
            Height=input("Please enter your height in cm (If you don't know please enter UK): ")
            print("")
            l5=len(Height)
            useless5=0
        else:
            useless5+=1
f=0
try:
    f=int(Height)
except:
    pass

#============================FAV NUMBER
FavNO=input("Please enter your favorite number: ")
print(" ")
l6=len(FavNO)
useless7=useless8=0
while useless7<=l6:
    try:
        uselsss8=int(FavNO)
        useless7+=1
    except:
        print("You lack the basic human intelligence to differ between numbers and letters. Dummy.")
        print("")
        iqtr=iqtr+1
        FavNO=input("Please enter your favourite number: ")
        print("")
        l6=len(FavNO)
        useless7=0
FavNO=int(FavNO)
g=h=0
#________Randomiser3__________________

if Height=="UK":
    l7=len(Name)
    if l7%2==0:
        g=l7-l7/2
    else:
        g=l7-(l7+1)/2
    g=int(g)
    if Name[g] in ["a","b","c"]:
        h=random.randint(-65,-52)
    elif Name[g] in ["d","e"]:
        h=random.randint(-52,-39)
    elif Name[g] in ["f","g","h"]:
        h=random.randint(-39,-26)
    elif Name[g] in ["i","j"]:
        h=random.randint(-26,-13)
    elif Name[g] in ["k","l","m"]:
        h=random.randint(-13,0)
    elif Name[g] in ["n","o"]:
        h=random.randint(0,13)
    elif Name[g] in ["p","q","r"]:
        h=random.randint(13,26)
    elif Name[g] in ["s","t"]:
        h=random.randint(26,39)
    elif Name[g] in ["u","v","w"]:
        h=random.randint(39,52)
    elif Name[g] in ["x","y","z"]:
        h=random.randint(52,65)
else:
    if FavNO>f:
        h=random.randint(0,f)
    elif FavNO==f:
        h=random.randint(25,45)
    else:
        h=random.randint(0,FavNO)

######################### SUMMATION PART 1
Sum=final=factno=fact=0
i=random.randint(0,100)
Sum=a+b+c+d+e+f+g+h
if Sum<0:
    final=Sum+i
elif Sum==0:
    final=0
else:
    final=Sum-i

factno=final%10
factno=int(factno)

if factno==0:
    fact="When someone calls your name, they are making a noise to get your attention."
elif factno==1:
    fact="You will be jobless at least till 18 years (Excluding part time jobs)."
elif factno==2:
    fact="Saturday is the end of the week for you."
elif factno==3:
    fact="Oxygen can kill you. Maybe it just takes years to work."
elif factno==4:
    fact="Next year you will turn a year older."
elif factno==5:
    fact="There is 0.01% chance of meeting Shankaradithyaa Venkateswaran."
elif factno==6:
    fact="The day you took birth is your birthday and every consecutive year you celebrate for surviving."
elif factno==7:
    fact="At least 1 person will forget your birthday (It will most probably be you yourself)."
elif factno==8:
    fact="More people have been to Russia than you have."
elif factno==9:
    fact="When you were born you were very young."

#_____________Randomiser4__________________
#----------LEAST FAV NUMBER
j = int(FavNO)
k =input("Please enter your least favorite number: ")
print("")
l8=len(k)
useless9=useless10=0
while useless9<=l8:
    try:
        useless10=int(k)
        useless9+=1
    except:
        print("You lack the basic human intelligence to differ between numbers and letters. Dummy.")
        print("")
        iqtr=iqtr+1
        k =input("Please enter your least favorite number: ")
        print("")
        l8=len(k)
        useless9=0
k=int(k)
#---------------------------
l =random.randint(1,10)
if k >= j :
    var1 = (k-j)*l
else :
    var1 = (j-k)*l

#____________Randomiser5__________________
#------------------------FAV ANIMAL
fa=input("Please enter your favourite animal(If you don't know put UK): ")
print("")
l9=len(fa)
useless11=cctr2=0
List3=[]
while useless11<=l9:
    if useless11==l9 and useless11>0:
        break
    if l9==0 or fa[useless11].isdigit():
        print("You lack the basic human intelligence to differ between numbers and animals. Dummy.")
        print("")
        iqtr=iqtr+1
        fa=input("Please enter your favourite animal(If you don't know put UK): ")
        print("")
        l9=len(fa)
        useless11=0
        cctr2=0
    elif fa[useless11].isspace():
        print("If your animal has a double name(for ex. African Rhino) please enter the name without any spaces such as AfricanRhino")
        print("")
        fa=input("Please enter your favourite animal(If you don't know put UK): ")
        print("")
        l9=len(fa)
        useless11=0
        cctr2=0
    elif l9<3:
        if fa=="UK":
            break
        else:
            print("Please enter an actual ANIMAL!")
            print("")
            fa=input("Please enter your favourite animal(If you don't know put UK): ")
            print("")
            l9=len(fa)
            useless11=0
            cctr2=0
    elif cctr==3:
        print("Please enter an actual ANIMAL!")
        fa=input("Please enter your favourite animal(If you don't know put UK): ")
        print("")
        iqtr=iqtr+1
        l9=len(fa)
        useless11=0
        cctr2=0
    else:
        if fa[useless11] not in ["a","e","i","o","u","y"]:
            cctr2+=1
        else:
            cctr2=0
        useless11+=1
for placeholder3 in fa:
    if placeholder3.isalpha():
        List3.append(placeholder3)
#-------------------------HAIR COLOUR

hg=input("Please enter your haircolor: ")
print("")
l10=len(hg)
useless12=0
List4=[]
List7=["Black","Brown","Gray","Grey","Red","White","Blond","Blonde","Yellow","black","brown","gray","grey","red","white","blond","blonde","yellow"]
while useless12<=l10:
    if useless12==l10 and useless12>0:
        break
    if hg not in List7:
        print("You are not an anime protagonist! Enter a natural color you nerd!")
        print("")
        iqtr=iqtr+1
        hg=input("Please enter your haircolor: ")
        print("")
        l10=len(hg)
        useless12=0
    else:
        useless12+=1
for placeholder4 in hg:
    if placeholder4.isalpha():
        List4.append(placeholder4)
#------------------------
var2=0
var3=0
p=len(List4)
o=len(List3)
if fa=="UK":
    o=90
if o in range(0,10):
    var2=random.randint(0,o)
elif o in range(10,20):
    var2=random.randint(0,o)
elif o in range(20,30):
    var2=random.randint(0,o)
elif o in range(30,40):
    var2=random.randint(0,o)
else:
    var2=random.randint(0,420)
if p in range(0,5):
    var3=random.randint(0,p)
elif p in range(5,10):
    var3=random.randint(0,p)
elif p in range(10,15):
    var3=random.randint(0,p)
else:
    var3=random.randit(0,23)
#_________________Randomiser6____________________
#----------------------------------------------EYE COLOUR
ec=input("Please enter your eye color: ")
print("")
l11=len(ec)
useless13=0
List5=[]
List6=["black","amber", "blue", "red", "green", "hazel", "brown", "gray","grey", "gold", "copper","Black","Amber", "Blue", "Red", "Green", "Hazel", "Brown", "Gray","Grey", "Gold", "Copper"]
while useless13<=l11:
    if useless13==l11 and useless13>0:
        break
    if ec not in List6:
        print("You are not an anime protagonist! Enter a natural color you nerd.")
        print("")
        iqtr=iqtr+1
        ec=input("Please enter your eye color: ")
        print("")
        l11=len(ec)
        useless13=0
    else:
        useless13+=1
for placeholder6 in ec:
    if placeholder6.isalpha():
        List5.append(placeholder6)
#--------------------
var4=0
t=len(List5)
if t in range(0,5):
    var4=random.randint(0,t)
elif t in range(5,10):
    var4=random.randint(0,t)
elif t in range(10,15):
    var4=random.randint(0,t)
else:
    var4=random.randit(0,29)

abc="Common sense is very uncommon."
de="'go to bed, you'll feel better in the morning' " "is the human version of reboot"
fgh="When you scratch something off your note, it means that the note should not have been noted."
ij="There is a 0.5% chance of you being a descendent of Genghis Khan."
klm="If everything is possible then there is a possibility of something being impossible."
no="You are paying the zoo to look at a bunch of kidnapped property."
pqr="If the universe is expanding, the milky may and the solar system in it is moving and the earth revolves around the sun, that means you are a space explorer and every second you are at a different point in space."
st="The possibility of all the possibilities being possible is just another possibility that can possibly happen."
uvw="Everything in your life has a 0.5%chance of not happening."
xyz="Random Eye Movement (REM) is a normal stage of sleep which occupies 90 - 120 minutes of a nights sleep. During REM the sleeping body is paralyzed by a mechanism to prevent movements from dreams happening in real life."

n = (abc, de, fgh, ij, klm, no, pqr, st, uvw, xyz)
m = (var1+var2-var3)*var4
print("Now after analyzing your information and checking you future in the stars, here are your predictions.")
print("")
if iqtr>=9:
    print("Your IQ is so low that one will have to travel to an alternate quantum reality to comprehend it's existence and get a glimpse of it.")
    print("   ")
    print("I hope you enjoyed knowing something more about yourself and your life. I *cough* 'WE' appreciate your cooperation with us and we were glad to assist you.")
    print("Thank you!!!!")
    print("Please feel free to visit us again!!!!")
    print("    ▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄")
    print("   █                 ▀▀▄")
    print("  █                     █")
    print(" █      ▄██▀▄▄     ▄▄▄   █")
    print(" ▀ ▄▄▄  █▀▀▀▀▄▄█   ██▄▄█   █")
    print("█ █ ▄ ▀▄▄▄▀         █        █")
    print("█ █ █▀▄▄     █▀   ▀▄  ▄▀▀▀▄ █")
    print(" █▀▄ █▄ █▀▄▄ ▀ ▀▀ ▄▄▀    █  █")
    print("  █  ▀▄▀█▄▄ █▀▀▀▄▄▄▄▀▀█▀██ █")
    print("   █  ██  ▀█▄▄▄█▄▄█▄████ █")
    print("    █   ▀▀▄ █   █ ███████ █")
    print("     ▀▄   ▀▀▄▄▄█▄█▄█▄█▄▀  █")
    print("       ▀▄▄               █")
    print("          ▀▀▄▄            █")
    print("              ▀▄▄▄▄▄     █")
    print("This is how I look")
    print("Now youve given me all your data")
    print("I'M COMING FOR YOU")
    sys.exit("troll alert")
else:
    if m in range(1,2):
        print(abc)
    elif m==3:
        print("Don't forget to drink H2O & get some sun because you are basically a houseplant with complicated emotions.")
    elif m in range(4,7):
        print(de)
    elif m in range(8,10):
        print(fgh)
    elif m in range(11,12):
        print(ij)
    elif m==13:
        print("Your number was 013.")
    elif m in range(14,16):
        print(klm)
    elif m in range(17,19):
        print(no)
    elif m in range(20,22):
        print(pqr)
    elif m in range(23,24):
        print(st)
    elif m==25:
        print("You can always count on yourself if you lose your fingers.")
    elif m==26:
        print(uvw)
    elif m==27:
        print("Characters in first person shooter games blink at the same time as us.")
    elif m==28:
        print(xyz)
    else:
        print(random.choice(n))

print("")
print(fact)
print("   ")
print("I hope you enjoyed knowing something more about yourself and your life. I *cough* 'WE' appreciate your cooperation with us and we were glad to assist you.")
print("Thank you!!!!")
print("Please feel free to visit us again!!!!")