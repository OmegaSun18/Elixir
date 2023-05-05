#Import statements+mysql connector

import mysql.connector
from time import sleep
import pickle
import textwrap
from tkinter import *
from PIL import ImageTk, Image
import os
import sys

mycon=mysql.connector.connect(host="localhost",user="root",passwd="1805530343")
cursor=mycon.cursor()
cursor.execute("DROP database IF EXISTS project")
st="CREATE database project;"
cursor.execute(st)
mycon.commit()
mycon.close()

mycon=mysql.connector.connect(host="localhost",user="root",passwd="1805530343",database="project")
cursor=mycon.cursor()

#User Defined functions

def numchoice(pointer):
    """getting the number of choices available"""
    
    st="SELECT * FROM coutline WHERE sp=%s"%(pointer,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter+4]
    return c

def cfile(pointer):
    """to get the name of the choice file, depending on the number of choices two or three values will be returned"""
    global filecounter
    
    a=numchoice(pointer)
    st="SELECT choice1 FROM coutline WHERE sp=%s"%(pointer,)
    cursor.execute(st)
    b=cursor.fetchall()
    c=b[filecounter]
    d=c[filecounter]
    st="SELECT choice2 FROM coutline WHERE sp=%s"%(pointer,)
    cursor.execute(st)
    e=cursor.fetchall()
    f=e[filecounter]
    g=f[filecounter]

    if a==3:
        st="SELECT choice3 FROM coutline WHERE sp=%s"%(pointer,)
        cursor.execute(st)
        h=cursor.fetchall()
        i=h[filecounter]
        j=i[filecounter]
        return d,g,j
    else:
        return d,g

def deadend(name):
    """to find out if the choice is a deadend"""
    
    st="SELECT deadend FROM choices WHERE cname='%s'"%(name,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter]
    return c

def cstatement(name):
    """Stuff on button"""
    
    st="SELECT st FROM choices WHERE cname='%s'"%(name,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter]
    return c

def cloadno(name):
    """loadno for choices"""
    
    st="SELECT loadno FROM choices WHERE cname='%s'"%(name,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter]
    return c

def floadno(pointer):
    """To get the load number for main story"""
    
    st="SELECT loadno FROM choutline WHERE sp=%s"%(pointer,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter]
    return c

def file(pointer):
    """to get the story from the file"""
    
    st="SELECT filehandle FROM choutline WHERE sp=%s"%(pointer,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter]
    d=".\\Story\\"+c+".bin"
    fin=open(d,"rb")
    e=[]
    f=floadno(pointer)
    for i in range(0,f):
        g=pickle.load(fin)
        e.append(g)
    fin.close()
    return e

def cstory(name):
    """To get the choice story"""
    
    a=".\\Choices\\"+name+".bin"
    fin=open(a,"rb")
    b=[]
    c=cloadno(name)
    for i in range(0,c):
        d=pickle.load(fin)
        b.append(d)
    fin.close()
    return b

def nextsp(currentsp):
    """to get the next story pointer"""
    global storypointer,filecounter,ch

    try:
        st="SELECT nsp FROM coutline WHERE sp=%s"
        cursor.execute(st,(currentsp,))
        a=cursor.fetchall()
        b=a[filecounter]
        c=b[filecounter]
        if c==' ':
            st="SELECT nsp FROM choices WHERE cname=%s"
            cursor.execute(st,(ch,))
            d=cursor.fetchall()
            e=d[filecounter]
            f=e[filecounter]
            f=int(f)
            sp=f
            return sp
        else:
            c=int(c)
            sp=c
            return sp

    except:
        st="SELECT nsp FROM choices WHERE cname=%s"
        cursor.execute(st,(ch,))
        a=cursor.fetchall()
        b=a[filecounter]
        c=b[filecounter]
        if c==' ':
            pass
        else:
            c=int(c)
            sp=c
            return sp

def chpt(pointer):
    """"Seeing if there is a checkpoint or not at this file pointer"""
    
    st="SELECT chpt FROM coutline WHERE sp=%s"%(pointer,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter]
    return c

def chptsno(currentsp):
    """Getting the checkpoint number from the currentsp"""
    
    st="SELECT cno FROM checkpoint WHERE currentsp=%s"%(currentsp,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter]
    return c

def chptnxtsp(cno):
    """Getting the currentsp from the checkpoint no"""
    
    st="SELECT currentsp FROM checkpoint WHERE cno=%s"%(cno,)
    cursor.execute(st)
    a=cursor.fetchall()
    b=a[filecounter]
    c=b[filecounter]
    return c

def replace(string):
    """Replacing the code names"""
    global pn1,pn2,pn3,name
    
    string=string.replace('Jf*De*','Jeff')
    string=string.replace('Jf*An*','Jeff')
    string=string.replace('Jf*Cg*','Jeff')
    string=string.replace('Jf*Cn*','Jeff')
    string=string.replace('Jf*Cr*','Jeff')
    string=string.replace('Jf*Sa*','Jeff')
    string=string.replace('Jf*Sh*','Jeff')
    string=string.replace('Jf*Sm*','Jeff')
    
    string=string.replace('Jn*De*','Jennifer')
    string=string.replace('Jn*An*','Jennifer')
    string=string.replace('Jn*Ao*','Jennifer')
    string=string.replace('Jn*Cr*','Jennifer')
    string=string.replace('Jn*Df*','Jennifer')
    string=string.replace('Jn*Sh*','Jennifer')
    string=string.replace('Jn*Sk*','Jennifer')
    string=string.replace('Jn*Wf*','Jennifer')
    string=string.replace('Jn*Wo*','Jennifer')
    
    string=string.replace('Li*De*','Lily')
    string=string.replace('Li*Cd*','Lily')
    string=string.replace('Li*Dy*','Lily')
    string=string.replace('Li*Ss*','Lily')
    string=string.replace('Li*Wo*','Lily')
    
    string=string.replace('Lu*De*','Luna')
    string=string.replace('Lu*An*','Luna')
    string=string.replace('Lu*Cr*','Luna')
    string=string.replace('Lu*Dr*','Luna')
    string=string.replace('Lu*Sm*','Luna')
    
    string=string.replace('Tr*De*','Trey')
    string=string.replace('Tr*An*','Trey')
    string=string.replace('Tr*Co*','Trey')
    string=string.replace('Tr*Cr*','Trey')
    string=string.replace('Tr*Sa*','Trey')
    string=string.replace('Tr*Sm*','Trey')
    
    string=string.replace('Wa*De*','Wally')
    string=string.replace('Wa*An*','Wally')
    string=string.replace('Wa*Cr*','Wally')
    string=string.replace('Wa*Sa*','Wally')
    string=string.replace('Wa*Wh*','Wally')
    string=string.replace('Wa*Wo*','Wally')
    
    string=string.replace('_____*',name)
    string=string.replace('____*',pn1)
    string=string.replace('___*',pn2)
    string=string.replace('__*',pn3)
    return string

def avatar(string):
    """Getting which avatar to display"""
    global Joe,Joelene,Jf11,Tr11,Jn11,Lu11,Li11,Wa11,Jf21,Jf31,Jf41,Jf51,Jf61,Jf71,Jf81,Tr21,Tr31,Tr41,Tr51,Tr61,Jn21,Jn31,Jn41,Jn51,Jn61,Jn71,Jn81,Jn91,Lu21,Lu31,Lu41,Lu51,Li21,Li31,Li41,Li51,Wa21,Wa31,Wa41,Wa51,Wa61
    
    a=string[:6]
    if a=="Jf*De*":
        Jf11 = C.create_image(300,515,anchor="s", image=Jf1)
    elif a=="Jf*An*":
        Jf21 = C.create_image(300,515,anchor="s", image=Jf2)
    elif a=="Jf*Cg*":
        Jf31 = C.create_image(300,515,anchor="s", image=Jf3)
    elif a=="Jf*Cn*":
        Jf41 = C.create_image(300,515,anchor="s", image=Jf4)
    elif a=="Jf*Cr*":
        Jf51 = C.create_image(300,515,anchor="s", image=Jf5)
    elif a=="Jf*Sa*":
        Jf61 = C.create_image(300,515,anchor="s", image=Jf6)
    elif a=="Jf*Sh*":
        Jf71 = C.create_image(300,515,anchor="s", image=Jf7)
    elif a=="Jf*Sm*":
        Jf81 = C.create_image(300,515,anchor="s", image=Jf8)
    
    elif a=="Tr*De*":
        Tr11 = C.create_image(300,515,anchor="s", image=Tr1)
    elif a=="Tr*An*":
        Tr21 = C.create_image(300,515,anchor="s", image=Tr2)
    elif a=="Tr*Co*":
        Tr31 = C.create_image(300,515,anchor="s", image=Tr3)
    elif a=="Tr*Cr*":
        Tr41 = C.create_image(300,515,anchor="s", image=Tr4)
    elif a=="Tr*Sa*":
        Tr51 = C.create_image(300,515,anchor="s", image=Tr5)
    elif a=="Tr*Sm*":
        Tr61 = C.create_image(300,515,anchor="s", image=Tr6)

    
    elif a=="Jn*De*":
        Jn11 = C.create_image(300,515,anchor="s", image=Jn1)
    elif a=="Jn*An*":
        Jn21 = C.create_image(300,515,anchor="s", image=Jn2)
    elif a=="Jn*Ao*":
        Jn31 = C.create_image(300,515,anchor="s", image=Jn3)
    elif a=="Jn*Cr*":
        Jn41 = C.create_image(300,515,anchor="s", image=Jn4)
    elif a=="Jn*Df*":
        Jn51 = C.create_image(300,515,anchor="s", image=Jn5)
    elif a=="Jn*Sh*":
        Jn61 = C.create_image(300,515,anchor="s", image=Jn6)
    elif a=="Jn*Sk*":
        Jn71 = C.create_image(300,515,anchor="s", image=Jn7)
    elif a=="Jn*Wf*":
        Jn81 = C.create_image(300,515,anchor="s", image=Jn8)
    elif a=="Jn*Wo*":
        Jn91 = C.create_image(300,515,anchor="s", image=Jn9)
    
    elif a=="Lu*De*":
        Lu11 = C.create_image(300,515,anchor="s", image=Lu1)
    elif a=="Lu*An*":
        Lu21 = C.create_image(300,515,anchor="s", image=Lu2)
    elif a=="Lu*Cr*":
        Lu31 = C.create_image(300,515,anchor="s", image=Lu3)
    elif a=="Lu*Dr*":
        Lu41 = C.create_image(300,515,anchor="s", image=Lu4)
    elif a=="Lu*Sm*":
        Lu51 = C.create_image(300,515,anchor="s", image=Lu5)
    
    elif a=="Li*De*":
        Li11 = C.create_image(300,515,anchor="s", image=Li1)
    elif a=="Li*Cd*":
        Li21 = C.create_image(300,515,anchor="s", image=Li2)
    elif a=="Li*Dy*":
        Li31 = C.create_image(300,515,anchor="s", image=Li3)
    elif a=="Li*Ss*":
        Li41 = C.create_image(300,515,anchor="s", image=Li4)
    elif a=="Li*Wo*":
        Li51 = C.create_image(300,515,anchor="s", image=Li5)
    
    elif a=="Wa*De*":
        Wa11 = C.create_image(300,515,anchor="s", image=Wa1)
    elif a=="Wa*An*":
        Wa21 = C.create_image(300,515,anchor="s", image=Wa2)
    elif a=="Wa*Cr*":
        Wa31 = C.create_image(300,515,anchor="s", image=Wa3)
    elif a=="Wa*Sa*":
        Wa41 = C.create_image(300,515,anchor="s", image=Wa4)
    elif a=="Wa*Wh*":
        Wa51 = C.create_image(300,515,anchor="s", image=Wa5)
    elif a=="Wa*Wo*":
        Wa61 = C.create_image(300,515,anchor="s", image=Wa6)

    elif a=="_____*":
        if name=='Joe':
            Joe= C.create_image(300,515,anchor="s", image=man1)
        elif name=='Joelene':
            Joelene= C.create_image(300,515,anchor="s", image=women1)
        else:
            pass
        
    else:
        pass

def delavatar():
    """Deletes the avatars from the screen"""
    """Trey"""
    try:
        C.delete(Tr11)
    except:
        pass
    try:
        C.delete(Tr21)
    except:
        pass
    try:
        C.delete(Tr31)
    except:
        pass
    try:
        C.delete(Tr41)
    except:
        pass
    try:
        C.delete(Tr51)
    except:
        pass
    try:
        C.delete(Tr61)
    except:
        pass
    
    """Jennifer"""
    try:
        C.delete(Jn11)
    except:
        pass
    try:
        C.delete(Jn21)
    except:
        pass
    try:
        C.delete(Jn31)
    except:
        pass
    try:
        C.delete(Jn41)
    except:
        pass
    try:
        C.delete(Jn51)
    except:
        pass
    try:
        C.delete(Jn61)
    except:
        pass
    try:
        C.delete(Jn71)
    except:
        pass
    try:
        C.delete(Jn81)
    except:
        pass
    try:
        C.delete(Jn91)
    except:
        pass
    
    """Jeff"""
    try:
        C.delete(Jf11)
    except:
        pass
    try:
        C.delete(Jf21)
    except:
        pass
    try:
        C.delete(Jf31)
    except:
        pass
    try:
        C.delete(Jf41)
    except:
        pass
    try:
        C.delete(Jf51)
    except:
        pass
    try:
        C.delete(Jf61)
    except:
        pass
    try:
        C.delete(Jf71)
    except:
        pass
    try:
        C.delete(Jf81)
    except:
        pass
    
    """Luna"""
    try:
        C.delete(Lu11)
    except:
        pass
    try:
        C.delete(Lu21)
    except:
        pass
    try:
        C.delete(Lu31)
    except:
        pass
    try:
        C.delete(Lu41)
    except:
        pass
    try:
        C.delete(Lu51)
    except:
        pass
    
    """Lily"""
    try:
        C.delete(Li11)
    except:
        pass
    try:
        C.delete(Li21)
    except:
        pass
    try:
        C.delete(Li31)
    except:
        pass
    try:
        C.delete(Li41)
    except:
        pass
    try:
        C.delete(Li51)
    except:
        pass
    
    """Wally"""
    try:
        C.delete(Wa11)
    except:
        pass
    try:
        C.delete(Wa21)
    except:
        pass
    try:
        C.delete(Wa31)
    except:
        pass
    try:
        C.delete(Wa41)
    except:
        pass
    try:
        C.delete(Wa51)
    except:
        pass
    try:
        C.delete(Wa61)
    except:
        pass

    """Protagonist"""
    try:
        C.delete(Joe)
    except:
        pass
    try:
        C.delete(Joelene)
    except:
        pass
    

def nextstory():
    """Brain of the whole operation"""
    global storypointer, dg, dc, colour

    try:
        C.delete('all')
    except:
        pass
    
    storypointer=nextsp(storypointer)  
    dg=file(storypointer)
    dc=0
    
    if storypointer>100 and storypointer<118:

        colour='black'
        bgdd = C.create_image(0,0,anchor="nw", image=bgd1)
        db1d = C.create_image(60,515,anchor="nw", image=db1)
        nxtbut1= Button(root, image=nxt1, borderwidth=0, command=display, cursor='hand2', bg="#c0f7f9")
        nxtbut11 = C.create_window(1290, 2, anchor="nw", window=nxtbut1)
        
    elif storypointer>=118 and storypointer<200:

        colour='black'
        bgdd0 = C.create_image(0,0,anchor="nw", image=bgd10)
        tb100 = C.create_image(60,515,anchor="nw", image=tb10)
        nxtbut0 = Button(root, image=nxt10, borderwidth=0, command=display, cursor='hand2', bg="#341F1B")
        nxtbut10 = C.create_window(1290, 2, anchor="nw", window=nxtbut0)

    elif storypointer>200 and storypointer<300:

        colour='white'
        bgdd2 = C.create_image(0,0,anchor="nw", image=bgd12)
        tb122 = C.create_image(60,515,anchor="nw", image=tb12)
        nxtbut2 = Button(root, image=nxt12, borderwidth=0, command=display, cursor='hand2', bg='#C8E690')
        nxtbut12 = C.create_window(1290, 2, anchor="nw", window=nxtbut2)

    elif storypointer>300 and storypointer<400:

        colour='white'
        bgdd3 = C.create_image(0,0,anchor="nw", image=bgd13)
        tb133 = C.create_image(60,515,anchor="nw", image=tb13)
        nxtbut3 = Button(root, image=nxt13, borderwidth=0, command=display, cursor='hand2', bg='black')
        nxtbut13 = C.create_window(1290, 2, anchor="nw", window=nxtbut3)

    else:
        pass

def display():
    """Will actually shove stuff onto the screen"""
    global dc, dg, canvas_text, storypointer, colour

    try:
        C.delete(canvas_text)
        root.update()
        delavatar()
        root.update()
    except:
        pass

    if dc==len(dg):
        if chpt(storypointer)=='yes':
            checkpoint()
        else:
            if numchoice(storypointer)==0:
                nextstory()
            elif numchoice(storypointer)==2:
                cnxt2()
            elif numchoice(storypointer)==3:
                cnxt3()
            else:
                pass
        
    else:
        a=dg[dc]
        avatar(a)
        typing(dnd=a,fc=colour)
        root.update()
        dc+=1

def cdisplay():
    """Will actually shove stuff onto the screen"""
    global dc, dg, canvas_text, storypointer, ch, colour
    
    try:
        C.delete(canvas_text)
        root.update()
        delavatar()
        root.update()
    except:
        pass

    if dc==len(dg):
        if deadend(ch)=='yes':
            game_over()
        elif deadend(ch)=='GE':
            endgame()
        else:
            nextstory()
        
    else:
        a=dg[dc]
        avatar(a)
        typing(dnd=a, fc=colour)
        root.update()
        dc+=1
        
def cnextstory1():
    """function to display story from the choice files onto the screen, for ch1"""
    global storypointer, ch1, ch2, ch3, dg, dc, ch, colour
    
    try:
        C.delete('all')
    except:
        pass

    ch=ch1
    dg=cstory(ch1)
    dc=0

    if storypointer>100 and storypointer<118:

        colour='black'
        bgdd = C.create_image(0,0,anchor="nw", image=bgd1)
        db1d = C.create_image(60,515,anchor="nw", image=db1)
        nxtbut1= Button(root, image=nxt1, borderwidth=0, command=cdisplay, cursor='hand2', bg="#c0f7f9")
        nxtbut11 = C.create_window(1290, 2, anchor="nw", window=nxtbut1)
        
    elif storypointer>=118 and storypointer<200:

        colour='black'
        bgdd0 = C.create_image(0,0,anchor="nw", image=bgd10)
        tb100 = C.create_image(60,515,anchor="nw", image=tb10)
        nxtbut0 = Button(root, image=nxt10, borderwidth=0, command=cdisplay, cursor='hand2', bg="#341F1B")
        nxtbut10 = C.create_window(1290, 2, anchor="nw", window=nxtbut0)

    elif storypointer>200 and storypointer<300:

        colour='white'
        bgdd2 = C.create_image(0,0,anchor="nw", image=bgd12)
        tb122 = C.create_image(60,515,anchor="nw", image=tb12)
        nxtbut2 = Button(root, image=nxt12, borderwidth=0, command=cdisplay, cursor='hand2', bg='#C8E690')
        nxtbut12 = C.create_window(1290, 2, anchor="nw", window=nxtbut2)

    elif storypointer>300 and storypointer<400:

        colour='white'
        bgdd3 = C.create_image(0,0,anchor="nw", image=bgd13)
        tb133 = C.create_image(60,515,anchor="nw", image=tb13)
        nxtbut3 = Button(root, image=nxt13, borderwidth=0, command=cdisplay, cursor='hand2', bg='black')
        nxtbut13 = C.create_window(1290, 2, anchor="nw", window=nxtbut3)

    else:
        pass

def cnextstory2():
    """function to display story from the choice files onto the screen, for ch2"""
    global storypointer, ch1, ch2, ch3, dg, dc, ch
    
    try:
        C.delete('all')
    except:
        pass

    ch=ch2
    dg=cstory(ch2)
    dc=0

    if storypointer>100 and storypointer<118:

        colour='black'
        bgdd = C.create_image(0,0,anchor="nw", image=bgd1)
        db1d = C.create_image(60,515,anchor="nw", image=db1)
        nxtbut1= Button(root, image=nxt1, borderwidth=0, command=cdisplay, cursor='hand2', bg="#c0f7f9")
        nxtbut11 = C.create_window(1290, 2, anchor="nw", window=nxtbut1)
        
    elif storypointer>=118 and storypointer<200:

        colour='black'
        bgdd0 = C.create_image(0,0,anchor="nw", image=bgd10)
        tb100 = C.create_image(60,515,anchor="nw", image=tb10)
        nxtbut0 = Button(root, image=nxt10, borderwidth=0, command=cdisplay, cursor='hand2', bg="#341F1B")
        nxtbut10 = C.create_window(1290, 2, anchor="nw", window=nxtbut0)

    elif storypointer>200 and storypointer<300:

        colour='white'
        bgdd2 = C.create_image(0,0,anchor="nw", image=bgd12)
        tb122 = C.create_image(60,515,anchor="nw", image=tb12)
        nxtbut2 = Button(root, image=nxt12, borderwidth=0, command=cdisplay, cursor='hand2', bg='#C8E690')
        nxtbut12 = C.create_window(1290, 2, anchor="nw", window=nxtbut2)

    elif storypointer>300 and storypointer<400:

        colour='white'
        bgdd3 = C.create_image(0,0,anchor="nw", image=bgd13)
        tb133 = C.create_image(60,515,anchor="nw", image=tb13)
        nxtbut3 = Button(root, image=nxt13, borderwidth=0, command=cdisplay, cursor='hand2', bg='black')
        nxtbut13 = C.create_window(1290, 2, anchor="nw", window=nxtbut3)

    else:
        pass

def cnextstory3():
    """function to display story from the choice files onto the screen, for ch3"""
    global storypointer, ch1, ch2, ch3, dg, dc, ch
    
    try:
        C.delete('all')
    except:
        pass

    ch=ch3
    dg=cstory(ch3)
    dc=0

    if storypointer>100 and storypointer<118:

        colour='black'
        bgdd = C.create_image(0,0,anchor="nw", image=bgd1)
        db1d = C.create_image(60,515,anchor="nw", image=db1)
        nxtbut1= Button(root, image=nxt1, borderwidth=0, command=cdisplay, cursor='hand2', bg="#c0f7f9")
        nxtbut11 = C.create_window(1290, 2, anchor="nw", window=nxtbut1)
        
    elif storypointer>=118 and storypointer<200:

        colour='black'
        bgdd0 = C.create_image(0,0,anchor="nw", image=bgd10)
        tb100 = C.create_image(60,515,anchor="nw", image=tb10)
        nxtbut0 = Button(root, image=nxt10, borderwidth=0, command=cdisplay, cursor='hand2', bg="#341F1B")
        nxtbut10 = C.create_window(1290, 2, anchor="nw", window=nxtbut0)

    elif storypointer>200 and storypointer<300:

        colour='white'
        bgdd2 = C.create_image(0,0,anchor="nw", image=bgd12)
        tb122 = C.create_image(60,515,anchor="nw", image=tb12)
        nxtbut2 = Button(root, image=nxt12, borderwidth=0, command=cdisplay, cursor='hand2', bg='#C8E690')
        nxtbut12 = C.create_window(1290, 2, anchor="nw", window=nxtbut2)

    elif storypointer>300 and storypointer<400:

        colour='white'
        bgdd3 = C.create_image(0,0,anchor="nw", image=bgd13)
        tb133 = C.create_image(60,515,anchor="nw", image=tb13)
        nxtbut3 = Button(root, image=nxt13, borderwidth=0, command=cdisplay, cursor='hand2', bg='black')
        nxtbut13 = C.create_window(1290, 2, anchor="nw", window=nxtbut3)

    else:
        pass

def cnxt2():
    """function is called to make the choice screen for 2 choices"""
    global storypointer, ch1, ch2, ch3
    
    try:
        C.delete('all')
    except:
        pass

    choicebg=C.create_image(0,0,anchor="nw", image=chbg1)

    choice1= Button(root,image=ch11, borderwidth=0, command=cnextstory1, cursor='hand2', bg="black")
    choice11 = C.create_window(637, 375, anchor="w", window=choice1)

    choice2= Button(root,image=ch21, borderwidth=0, command=cnextstory2, cursor='hand2', bg="black")
    choice21 = C.create_window(637, 525, anchor="w", window=choice2)

    ch1,ch2=cfile(storypointer)
    b=cstatement(ch1)
    c=cstatement(ch2)
    d="Choice 1 - "+b
    e="Choice 2 - "+c
    c_typing1(dnd=d,fc='white',xaxis=600,yaxis=130)
    c_typing2(dnd=e,fc='white',xaxis=600,yaxis=190)

def cnxt3():
    """function is called to make the choice screen for 3 choices"""
    global storypointer, ch1, ch2, ch3
    
    try:
        C.delete('all')
    except:
        pass

    choicebg=C.create_image(0,0,anchor="nw", image=chbg1)

    choice1= Button(root,image=ch11, borderwidth=0, command=cnextstory1, cursor='hand2', bg="black")
    choice11 = C.create_window(637, 325, anchor="w", window=choice1)

    choice2= Button(root,image=ch21, borderwidth=0, command=cnextstory2, cursor='hand2', bg="black")
    choice21 = C.create_window(637, 450, anchor="w", window=choice2)

    choice3= Button(root,image=ch31, borderwidth=0, command=cnextstory3, cursor='hand2', bg="black")
    choice31 = C.create_window(637, 575, anchor="w", window=choice3)

    ch1,ch2,ch3=cfile(storypointer)
    b=cstatement(ch1)
    c=cstatement(ch2)
    d=cstatement(ch3)
    e="Choice 1 - "+b
    f="Choice 2 - "+c
    g="Choice 3 - "+d
    c_typing1(dnd=e,fc='white',xaxis=200,yaxis=50)
    c_typing2(dnd=f,fc='white',xaxis=200,yaxis=100)
    c_typing3(dnd=g,fc='white',xaxis=200,yaxis=150)
    
def title():
    """Title screen"""
    global load_button1,new_button1,exit_button1,set_button1
    
    C.delete('all')

    my_bg = C.create_image(0,0,anchor="nw", image=mbg)
    display1 = C.create_image(675,170,anchor="c", image=title1_1)

    load_button = Button(root, image=load_btn1, borderwidth=0, command=(load_game),cursor='hand2', bg='black')
    load_button1 = C.create_window(675, 500, anchor="c", window=load_button)

    f=open(".\\loadfile.bin",'rb')
    a=pickle.load(f)
    f.close()
    
    if a==0:
        load_button['state'] = "disabled"
        startg.config(state="normal")
    else:
        pass

    new_button = Button(root, image=new_btn1, command=(new_game), borderwidth=0, cursor='hand2', bg='black')
    new_button1 = C.create_window(675, 350, anchor="c", window=new_button)

    exit_button = Button(root, image=exit_btn1,command=game_exit, borderwidth=0, cursor='hand2', bg='black')
    exit_button1 = C.create_window(675, 650, anchor="c", window=exit_button)

    set_button = Button(root, image=set_btn1, command=settings, borderwidth=0, cursor='hand2', bg='black')
    set_button1 = C.create_window(1325, 60, anchor="c", window=set_button)

def game_exit():
    """Exiting the game"""
    
    while(0<1):
        root.destroy()
        sys.exit()

def settings():
    """Settings screen"""
    global my_bg1,display2,ins_button1,gb_button1,lc_button1,ts_button1

    C.itemconfigure(load_button1, state='hidden')
    C.itemconfigure(new_button1, state='hidden')
    C.itemconfigure(set_button1, state='hidden')
    C.itemconfigure(exit_button1, state='hidden')
    
    my_bg1 = C.create_image(0,0,anchor="nw", image=mbg1)
    display2 = C.create_image(675,120,anchor="c", image=title2_1)
     
    ins_button= Button(root,image=ins_btn1, borderwidth=0, command=instructions, cursor='hand2', bg="black")
    ins_button1 = C.create_window(675, 360, anchor="c", window=ins_button)

    gb_button= Button(root,image=gb_btn1, borderwidth=0, command=back, cursor='hand2', bg="black")
    gb_button1 = C.create_window(675, 520, anchor="c", window=gb_button)

def back():
    """Goes back to the title screen"""
    
    C.itemconfigure(load_button1, state='normal')
    C.itemconfigure(new_button1, state='normal')
    C.itemconfigure(set_button1, state='normal')
    C.itemconfigure(exit_button1, state='normal')
    
    C.delete(my_bg1)
    C.delete(display2)
    C.delete(ins_button1)
    C.delete(gb_button1)
    C.delete(lc_button1)
    C.delete(ts_button1)

def back1():
    """Goes back to the settings screen"""
    
    C.itemconfigure(ins_button1, state='normal')
    C.itemconfigure(gb_button1, state='normal')
    
    C.delete(insbag)
    C.delete(back2_window)

def instructions():
    """Creates the instructions screen"""
    global insbag, back2_window
    C.itemconfigure(ins_button1, state='hidden')
    C.itemconfigure(gb_button1, state='hidden')
    
    insbag = C.create_image(0,0,anchor="nw", image=insbg1)

    back2 = Button(root, image=insback1, borderwidth=0, command=back1, cursor='hand2', bg="#25231F")
    back2_window = C.create_window(617, 700, anchor="w", window=back2)
    

def new_game():
    """Starts a new game"""
    global startg,ts_window,startg_window,bimage,storypointer,proimg,chckpnt,ts_button
    
    C.delete('all')
    
    chckpnt=0
    a=265
    storypointer=100

    proimg=C.create_image(0,0,anchor="nw", image=text1)
    bimage=C.create_image(0,0,anchor="nw", image=bdrop1)

    startg = Button(root,image=start1, borderwidth=0, command=move, cursor='hand2', bg="black")
    startg_window = C.create_window(100, 75, anchor="w", window=startg)

    ts_button= Button(root,image=ts_btn1, command=title, borderwidth=0, cursor='hand2', bg="black")
    ts_window = C.create_window(1000, 75, anchor="w", window=ts_button)
    startg['state'] = "disabled"

    typing(dnd="Choose your character", xaxis=525, yaxis=250,ft='EB Garamond', fc="white", sz=20)
    c_typing1(dnd="Joe",xaxis=360, yaxis=700,ft='EB Garamond', fc="white", sz=20)
    c_typing2(dnd="Joelene",xaxis=930, yaxis=700,ft='EB Garamond', fc="white", sz=20)

    avchoice()

def load_game():
    """Loads the game to the last saved checkpoint"""
    global name,pn1,pn2,pn3,chckpnt,storypointer
    
    a=open(".\\loadfile.bin","rb")
    b=pickle.load(a)
    c=pickle.load(a)
    d=pickle.load(a)
    e=pickle.load(a)
    f=pickle.load(a)
    a.close()

    chckpnt=b
    name=c
    pn1=d
    pn2=e
    pn3=f
    g=chptnxtsp(chckpnt)
    storypointer=g
    nextstory()

def avchoice():
    """Selection for Male or Female"""
    global man_btn, women_btn,man_btn1, women_btn1

    man_btn = Button(root, image=man1_, borderwidth=0, command=male, cursor='hand2', bg="black")
    man_btn1 = C.create_window(368, 484, anchor="c", window=man_btn)

    women_btn = Button(root,image=women1_, borderwidth=0, command=female, cursor='hand2', bg="black")
    women_btn1 = C.create_window(968, 484, anchor="c", window=women_btn)

def male():
    """Male choice"""
    global name,pn1,pn2,pn3,chckpnt
    
    chckpnt=0
    name="Joe"
    pn1="his"
    pn2="he"
    pn3="him"
    women_btn['state'] = "disabled"
    startg.config(state="normal")
    ts_button['state'] = "disabled"

    f=open(".\\loadfile.bin",'wb')
    pickle.dump(chckpnt,f)
    pickle.dump(name,f)
    pickle.dump(pn1,f)
    pickle.dump(pn2,f)
    pickle.dump(pn3,f)
    f.close()
    
def female():
    """Female choice"""
    global name,pn1,pn2,pn3,chckpnt
    
    chckpnt=0
    name="Joelene"
    pn1="her"
    pn2="she"
    pn3="her"
    man_btn['state'] = "disabled"
    startg.config(state="normal")
    ts_button['state'] = "disabled"

    f=open(".\\loadfile.bin",'wb')
    pickle.dump(chckpnt,f)
    pickle.dump(name,f)
    pickle.dump(pn1,f)
    pickle.dump(pn2,f)
    pickle.dump(pn3,f)
    f.close()

def move():
    """Animation for Prologue"""
    global count,bx,by, nextbut, next_window
    
    d=open(".\\loadfile.bin","wb")
    a=0
    pickle.dump(a,d)
    d.close()
    
    C.delete(ts_window)
    C.delete(startg_window)
    C.delete(man_btn1)
    C.delete(women_btn1)
    C.delete(choice_text2)
    C.delete(choice_text1)
    C.delete(canvas_text)
    
    
    while count < 100:
        by=by+0.3
        count += 1
        C.move(bimage, bx, by)
        root.update_idletasks()
        sleep(0.03)

    C.delete(bimage)
    c=file(storypointer)
    
    for i in c:
        typing(dnd=i,xaxis=150,yaxis=290,tw=115,sz=16)

    nextbut= Button(root,image=nextb1, borderwidth=0, command=nexti, cursor='hand2', bg='#4b0082')
    next_window = C.create_window(1184, 723, anchor="w", window=nextbut)

def typing(dnd,xaxis=110,yaxis=560,tw=133,ft='EB Garamond',sz=15,fc="black"):
    """Regular typing animation"""
    global canvas_text
    
    dnd=replace(dnd)
    canvas_text = C.create_text(xaxis, yaxis, text='', anchor="nw", font=(ft, sz), fill=fc)
    wrapper=textwrap.TextWrapper(width=tw)
    word=wrapper.fill(text=dnd)
    d = ''.join(word)
    delta = 10
    delay = 0
    
    for j in range (0,len(d)+1):
        s = d[:j]
        update_text = lambda s=s: C.itemconfigure(canvas_text, text=s)
        C.after(delay, update_text)
        delay += delta

def c_typing1(dnd,xaxis=110,yaxis=560,tw=133,ft='EB Garamond',sz=15,fc="black"):
    """Typing animation for displaying choice statement 1"""
    global choice_text1

    choice_text1 = C.create_text(xaxis, yaxis, text='', anchor="nw", font=(ft, sz), fill=fc)
    wrapper=textwrap.TextWrapper(width=tw)
    word=wrapper.fill(text=dnd)
    d = ''.join(word)
    delta = 10
    delay = 0

    for j in range (0,len(d)+1):
        s = d[:j]
        update_text = lambda s=s: C.itemconfigure(choice_text1, text=s)
        C.after(delay, update_text)
        delay += delta

def c_typing2(dnd,xaxis=110,yaxis=560,tw=133,ft='EB Garamond',sz=15,fc="black"):
    """Typing animation for displaying choice statement 2"""
    global choice_text2

    choice_text2 = C.create_text(xaxis, yaxis, text='', anchor="nw", font=(ft, sz), fill=fc)
    wrapper=textwrap.TextWrapper(width=tw)
    word=wrapper.fill(text=dnd)
    d = ''.join(word)
    delta = 10
    delay = 0

    for j in range (0,len(d)+1):
        s = d[:j]
        update_text = lambda s=s: C.itemconfigure(choice_text2, text=s)
        C.after(delay, update_text)
        delay += delta

def c_typing3(dnd,xaxis=110,yaxis=560,tw=133,ft='EB Garamond',sz=15,fc="black"):
    """Typing animation for displaying choice statement 3"""
    global choice_text3

    choice_text3 = C.create_text(xaxis, yaxis, text='', anchor="nw", font=(ft, sz), fill=fc)
    wrapper=textwrap.TextWrapper(width=tw)
    word=wrapper.fill(text=dnd)
    d = ''.join(word)
    delta = 10
    delay = 0

    for j in range (0,len(d)+1):
        s = d[:j]
        update_text = lambda s=s: C.itemconfigure(choice_text3, text=s)
        C.after(delay, update_text)
        delay += delta

def nexti():
    """Leads to the story starting"""
    global storypointer
    
    C.delete(canvas_text)
    C.delete(next_window)
    C.delete(proimg)
    nextstory()

def checkpoint_fade(dnd, yaxis):
    """Fade effect of checkpoint screen"""
    
    zx2bg=C.create_image(0,0,anchor="nw", image=zx12)
    root.update_idletasks()
    sleep(0.08)
    
    zx3bg=C.create_image(0,0,anchor="nw", image=zx13)
    root.update_idletasks()
    sleep(0.08)
    
    zx4bg=C.create_image(0,0,anchor="nw", image=zx14)
    root.update_idletasks()
    sleep(0.08)
    
    zx5bg=C.create_image(0,0,anchor="nw", image=zx15)
    root.update_idletasks()
    sleep(0.08)
    
    zx6bg=C.create_image(0,0,anchor="nw", image=zx16)
    root.update_idletasks()
    sleep(0.08)
    
    zx7bg=C.create_image(0,0,anchor="nw", image=zx17)
    root.update_idletasks()
    sleep(0.08)
    
    zx8bg=C.create_image(0,0,anchor="nw", image=zx18)
    root.update_idletasks()
    sleep(0.08)
    
    zx9bg=C.create_image(0,0,anchor="nw", image=zx19)
    root.update_idletasks()
    sleep(0.08)
    
    zx10bg=C.create_image(0,0,anchor="nw", image=zx110)
    root.update_idletasks()
    sleep(0.08)

    canvas_text = C.create_text(400, yaxis, text='', anchor="nw", font=("Times New Roman", 50), fill="white")

    wrapper=textwrap.TextWrapper(width=150)
    word=wrapper.fill(text=dnd)
    d = ''.join(word)
    delta = 10
    delay = 0

    for j in range (0,len(d)+1):
        s = d[:j]
        update_text = lambda s=s: C.itemconfigure(canvas_text, text=s)
        C.after(delay, update_text)
        delay += delta

    next_check= Button(root,image=next_chck1, borderwidth=0, command=nextstory, cursor='hand2', bg="black")
    next_check1 = C.create_window(1290, 40, anchor="w", window=next_check)

def checkpoint():
    """checkpoint screeen"""
    global name,pn1,pn2,pn3,chckpnt,storypointer
    
    try:
        C.delete('all')
    except:
        pass
    
    chckpnt=chptsno(storypointer)
    c=str(chckpnt)
    b="Checkpoint"+c
    zx1bg=C.create_image(0,0,anchor="nw", image=zx11)
    root.update()
    sleep(0.08)
    checkpoint_fade(b,100)
    a=open(".\\loadfile.bin","wb")
    pickle.dump(chckpnt,a)
    pickle.dump(name,a)
    pickle.dump(pn1,a)
    pickle.dump(pn2,a)
    pickle.dump(pn3,a)
    a.close()
    
def game_over():
    """Game over screen"""
    
    try:
        C.delete('all')
    except:
        pass
    
    gobgbg=C.create_image(0,0,anchor="nw", image=gobg1)
    gooimg=C.create_image(425,100,anchor="nw", image=goo1)

    golc_btn= Button(root,image=golc1, command=lastcheckpoint, borderwidth=0, cursor='hand2', bg="black")
    golc_btn1 = C.create_window(470, 375, anchor="w", window=golc_btn)

    gots_btn= Button(root,image=gots1, command=title, borderwidth=0, cursor='hand2', bg="black")
    gots_btn1 = C.create_window(470, 595, anchor="w", window=gots_btn)

def lastcheckpoint():
    """Warps to last checkpoint"""
    global chckpnt,storypointer
    
    a=open(".\\loadfile.bin",'rb')
    b=pickle.load(a)
    chckpnt=b
    a.close()
    c=chptnxtsp(chckpnt)
    storypointer=c
    nextstory()

def endgame():
    """End screen"""
    
    try:
        C.delete('all')
    except:
        pass
    
    endbg11=C.create_image(0,0,anchor="nw", image=endbg1)
    endts_btn= Button(root,image=endts1, borderwidth=0, command=title, cursor='hand2', bg="#FCECA7")
    endts_btn1 = C.create_window(670, 400, anchor="c", window=endts_btn)
    
    typing("Thank You For Playing!", 400, 95)

#setting up databases

try:
    cursor.execute("DROP TABLE choutline")
    cursor.execute("CREATE TABLE choutline(sp int, primary key(sp), filehandle varchar(20), loadno int)")
    mycon.commit()
except:
    cursor.execute("CREATE TABLE choutline(sp int, primary key(sp), filehandle varchar(20), loadno int)")
    mycon.commit()
    
cursor.execute("INSERT INTO choutline values(100,'prologue',1)")
cursor.execute("INSERT INTO choutline values(101,'cp1',5)")
cursor.execute("INSERT INTO choutline values(102,'cp2',5)")
cursor.execute("INSERT INTO choutline values(103,'cp3',11)")
cursor.execute("INSERT INTO choutline values(104,'cp4',16)")
cursor.execute("INSERT INTO choutline values(106,'cp5',8)")
cursor.execute("INSERT INTO choutline values(109,'cp6',2)")
cursor.execute("INSERT INTO choutline values(113,'cp7',12)")
cursor.execute("INSERT INTO choutline values(114,'cp8',9)")
cursor.execute("INSERT INTO choutline values(115,'cp9',8)")
cursor.execute("INSERT INTO choutline values(116,'cp10',8)")
cursor.execute("INSERT INTO choutline values(117,'cp11',5)")
cursor.execute("INSERT INTO choutline values(118,'cp12',5)")
cursor.execute("INSERT INTO choutline values(119,'cp13',11)")
cursor.execute("INSERT INTO choutline values(120,'cp14',8)")
cursor.execute("INSERT INTO choutline values(121,'cp15',18)")
cursor.execute("INSERT INTO choutline values(125,'cp16',11)")
cursor.execute("INSERT INTO choutline values(126,'cp17',9)")
cursor.execute("INSERT INTO choutline values(127,'cp18',12)")
cursor.execute("INSERT INTO choutline values(128,'cp19',10)")
cursor.execute("INSERT INTO choutline values(129,'cp20',9)")
cursor.execute("INSERT INTO choutline values(130,'cp21',8)")
mycon.commit()

cursor.execute("INSERT INTO choutline values(201,'cp22',15)")
cursor.execute("INSERT INTO choutline values(204,'cp23',11)")
cursor.execute("INSERT INTO choutline values(207,'cp24',4)")
cursor.execute("INSERT INTO choutline values(208,'cp25',11)")
cursor.execute("INSERT INTO choutline values(209,'cp26',10)")
cursor.execute("INSERT INTO choutline values(212,'cp27',12)")
cursor.execute("INSERT INTO choutline values(213,'cp28',6)")
cursor.execute("INSERT INTO choutline values(214,'cp29',5)")
mycon.commit()

cursor.execute("INSERT INTO choutline values(301,'cp30',7)")
cursor.execute("INSERT INTO choutline values(302,'cp31',10)")
cursor.execute("INSERT INTO choutline values(303,'cp32',14)")
cursor.execute("INSERT INTO choutline values(304,'cp33',10)")
cursor.execute("INSERT INTO choutline values(305,'cp34',14)")
cursor.execute("INSERT INTO choutline values(308,'cp35',14)")
cursor.execute("INSERT INTO choutline values(309,'cp36',9)")
cursor.execute("INSERT INTO choutline values(312,'cp37',9)")
cursor.execute("INSERT INTO choutline values(313,'cp38',13)")
cursor.execute("INSERT INTO choutline values(316,'cp39',14)")
cursor.execute("INSERT INTO choutline values(317,'cp40',10)")
cursor.execute("INSERT INTO choutline values(318,'cp41',16)")
cursor.execute("INSERT INTO choutline values(319,'cp42',11)")
cursor.execute("INSERT INTO choutline values(320,'cp43',7)")
mycon.commit()

try:
    cursor.execute("DROP TABLE coutline")
    cursor.execute("CREATE TABLE coutline(sp int, primary key(sp), choice1 varchar(20), choice2 varchar(20), choice3 varchar(20), numchoice int, nsp varchar(20), chpt varchar(20))")
    mycon.commit()
except:
    cursor.execute("CREATE TABLE coutline(sp int, primary key(sp), choice1 varchar(20), choice2 varchar(20), choice3 varchar(20), numchoice int, nsp varchar(20), chpt varchar(20))")
    mycon.commit()

cursor.execute("INSERT INTO coutline values(100,' ',' ',' ',0, '101', 'no')")
cursor.execute("INSERT INTO coutline values(101,' ',' ',' ',0, '102', 'no')")
cursor.execute("INSERT INTO coutline values(102,' ',' ',' ',0, '103', 'no')")
cursor.execute("INSERT INTO coutline values(103,' ',' ',' ',0, '104', 'yes')")
cursor.execute("INSERT INTO coutline values(104, 'CIa', 'CIb',' ', 2, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(106, 'CIIa', 'CIIb',' ', 2, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(109, 'CIIIa', 'CIIIb', 'CIIIc',3,' ', 'no')")
cursor.execute("INSERT INTO coutline values(113,' ',' ',' ',0, '114', 'no')")
cursor.execute("INSERT INTO coutline values(114,' ',' ',' ',0, '115', 'no')")
cursor.execute("INSERT INTO coutline values(115,' ',' ',' ',0, '116', 'no')")
cursor.execute("INSERT INTO coutline values(116,' ',' ',' ',0, '117', 'no')")
cursor.execute("INSERT INTO coutline values(117, 'CIIIa', 'CIIIb', 'CIIIc',3, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(118,' ',' ',' ',0, '119', 'no')")
cursor.execute("INSERT INTO coutline values(119,' ',' ',' ',0, '120', 'yes')")
cursor.execute("INSERT INTO coutline values(120,' ',' ',' ',0, '121', 'no')")
cursor.execute("INSERT INTO coutline values(121, 'CIVa', 'CIVb', 'CIVc',3, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(125,' ',' ',' ',0, '126', 'no')")
cursor.execute("INSERT INTO coutline values(126,' ',' ',' ',0, '127', 'no')")
cursor.execute("INSERT INTO coutline values(127,' ',' ',' ',0, '128', 'no')")
cursor.execute("INSERT INTO coutline values(128,' ',' ',' ',0, '129', 'no')")
cursor.execute("INSERT INTO coutline values(129,' ',' ',' ',0, '130', 'no')")
cursor.execute("INSERT INTO coutline values(130,' ',' ',' ',0, '201', 'yes')")
mycon.commit()

cursor.execute("INSERT INTO coutline values(201, 'CVa', 'CVb', ' ', 2, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(204, 'CVIa', 'CVIb', ' ', 2, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(207, ' ', ' ', ' ',0, '208', 'yes')")
cursor.execute("INSERT INTO coutline values(208, ' ', ' ', ' ',0, '209', 'no')")
cursor.execute("INSERT INTO coutline values(209, 'CVIIa', 'CVIIb',' ',2, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(212, ' ', ' ', ' ',0, '213', 'no')")
cursor.execute("INSERT INTO coutline values(213, ' ', ' ', ' ',0, '214', 'no')")
cursor.execute("INSERT INTO coutline values(214, ' ', ' ', ' ',0, '301', 'yes')")
mycon.commit()

cursor.execute("INSERT INTO coutline values(301,' ',' ',' ',0, '302', 'no')")
cursor.execute("INSERT INTO coutline values(302,' ',' ',' ',0, '303', 'no')")
cursor.execute("INSERT INTO coutline values(303,' ',' ',' ',0, '304', 'no')")
cursor.execute("INSERT INTO coutline values(304,' ',' ',' ',0, '305', 'yes')")
cursor.execute("INSERT INTO coutline values(305,'CVIIIa','CVIIIb',' ',2, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(308,' ',' ',' ',0, '309', 'no')")
cursor.execute("INSERT INTO coutline values(309,'CIXa','CIXb',' ',2, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(312,' ',' ',' ',0, '313', 'yes')")
cursor.execute("INSERT INTO coutline values(313,'CXa','CXb',' ',2, ' ', 'no')")
cursor.execute("INSERT INTO coutline values(316,' ',' ',' ',0, '317', 'no')")
cursor.execute("INSERT INTO coutline values(317,' ',' ',' ',0, '318', 'no')")
cursor.execute("INSERT INTO coutline values(318,' ',' ',' ',0, '319', 'no')")
cursor.execute("INSERT INTO coutline values(319,' ',' ',' ',0, '320', 'no')")
cursor.execute("INSERT INTO coutline values(320,'CXIa','CXIb',' ',2, ' ', 'no')")
mycon.commit()

try:
    cursor.execute("DROP TABLE choices")
    cursor.execute("CREATE TABLE choices(sp int, primary key(sp), cname varchar(10), st varchar(1000), deadend varchar(10), loadno int, nsp varchar(20))")
    mycon.commit()
except:
    cursor.execute("CREATE TABLE choices(sp int, primary key(sp), cname varchar(10), st varchar(1000), deadend varchar(10), loadno int, nsp varchar(20))")
    mycon.commit()

cursor.execute("INSERT INTO choices values(105, 'CIa', 'NO', 'no', 4,'106')")
cursor.execute("INSERT INTO choices values(167, 'CIb', 'YES', 'no', 10,'113')")
cursor.execute("INSERT INTO choices values(107, 'CIIa', 'Inject more Elixir', 'yes', 7,' ')")
cursor.execute("INSERT INTO choices values(108, 'CIIb', 'Get a Stabilizer', 'no', 7,'109')")
cursor.execute("INSERT INTO choices values(110, 'CIIIa', 'Grab a fire extinguisher and spray the monster with it.', 'yes', 1,' ')")
cursor.execute("INSERT INTO choices values(111, 'CIIIb', 'Find your way into the control room and lock yourself with the SuPeR sEcUrE sYsTeM and try to contact help.', 'yes', 9,' ')")
cursor.execute("INSERT INTO choices values(112, 'CIIIc', 'Turn on the fire alarm and try to escape the ensuing confusion', 'no', 2,'118')")
cursor.execute("INSERT INTO choices values(122, 'CIVa', 'Freeze Chandler at Absolute 0.', 'yes', 1,' ')")
cursor.execute("INSERT INTO choices values(123, 'CIVb', 'Poison Chandler with some lethal poison', 'yes', 1,' ')")
cursor.execute("INSERT INTO choices values(124, 'CIVc', 'Open a time rift and throw Chandler into the time stream.', 'no', 1,'125')")
cursor.execute("INSERT INTO choices values(202, 'CVa', 'Start searching their surroundings', 'no', 1,'204')")
cursor.execute("INSERT INTO choices values(203, 'CVb', 'Start searching the time machine', 'yes', 1,' ')")
cursor.execute("INSERT INTO choices values(205, 'CVIa', 'Going along the river', 'no', 1,'207')")
cursor.execute("INSERT INTO choices values(206, 'CVIb', 'Going through the forest', 'no', 1,'207')")
cursor.execute("INSERT INTO choices values(210, 'CVIIa', 'They find blankets and use them as mattress', 'no', 2,'212')")
cursor.execute("INSERT INTO choices values(211, 'CVIIb', 'They find materials to make a makeshift bed', 'no', 2,'212')")
cursor.execute("INSERT INTO choices values(306, 'CVIIIa', 'Clue', 'no', 4,'308')")
cursor.execute("INSERT INTO choices values(307, 'CVIIIb', 'Riddle', 'no', 8,'308')")
cursor.execute("INSERT INTO choices values(310, 'CIXa', 'Clue', 'no', 5,'312')")
cursor.execute("INSERT INTO choices values(311, 'CIXb', 'Riddle', 'no', 11,'312')")
cursor.execute("INSERT INTO choices values(314, 'CXa', 'Clue', 'no', 4,'316')")
cursor.execute("INSERT INTO choices values(315, 'CXb', 'Riddle', 'no', 11,'316')")
cursor.execute("INSERT INTO choices values(321, 'CXIa', 'Protagonist wins', 'GE', 6,' ')")
cursor.execute("INSERT INTO choices values(322, 'CXIb', 'Antagonist wins', 'GE', 1,' ')")
mycon.commit()

try:
    cursor.execute("DROP TABLE checkpoint")
    cursor.execute("CREATE TABLE checkpoint(cno int, currentsp int)")
    mycon.commit()
except:
    cursor.execute("CREATE TABLE checkpoint(cno int, currentsp int)")
    mycon.commit()

cursor.execute("INSERT INTO checkpoint values(1,103)")
cursor.execute("INSERT INTO checkpoint values(2,119)")
cursor.execute("INSERT INTO checkpoint values(3,130)")
cursor.execute("INSERT INTO checkpoint values(4,207)")
cursor.execute("INSERT INTO checkpoint values(5,214)")
cursor.execute("INSERT INTO checkpoint values(6,304)")
cursor.execute("INSERT INTO checkpoint values(7,312)")
mycon.commit()

#create the tKinter inteface

root=Tk()
root.geometry("1366x768")
root.attributes('-fullscreen', True)

#---------------Useful Variables-------------------------#

filecounter=0
storypointer=100#Storypointer
dg=[]#display guide
dc=0#display counter
colour=''#colour of text
ch1=ch2=ch3=ch=''#choicehelper
chckpnt=0#checkpointno
canvas_text=choice_text1=choice_text2=choice_text3=''#Used in typing animations
name=pn1=pn2=pn3=''#protagonistreplacement
Joe=Joelene=Jf11=Tr11=Jn11=Lu11=Li11=Wa11=Jf21=Jf31=Jf41=Jf51=Jf61=Jf71=Jf81=Tr21=Tr31=Tr41=Tr51=Tr61=Jn21=Jn31=Jn41=Jn51=Jn61=Jn71=Jn81=Jn91=Lu21=Lu31=Lu41=Lu51=Li21=Li31=Li41=Li51=Wa21=Wa31=Wa41=Wa51=Wa61=0
my_bg1=display2=ins_button1=gb_button1=lc_button1=ts_button1=0
insbag=back2_window=0
w=1366
h=768
z=0
by=0
bx=0
count=0

C = Canvas(root, height=h, width=w)
C.pack(fill="both",expand=True)

#-----------Image location of Protagonist-----------------------#

man = Image.open(".\\Layout\\PROJECT\\Pr\\Joe.png")
man1 = ImageTk.PhotoImage(man)

man_ = Image.open(".\\Layout\\PROJECT\\Pr\\Joe_.png")
man1_ = ImageTk.PhotoImage(man_)

women = Image.open(".\\Layout\\PROJECT\\Pr\\Joelene.png")
women1 = ImageTk.PhotoImage(women)

women_ = Image.open(".\\Layout\\PROJECT\\Pr\\Joelene_.png")
women1_ = ImageTk.PhotoImage(women_)

#--------Image location of Jeff-------------------#

Jf = Image.open(".\\Layout\\PROJECT\\Jf\\De.png")
Jf1 = ImageTk.PhotoImage(Jf)

Jfa = Image.open(".\\Layout\\PROJECT\\Jf\\An.png")
Jf2 = ImageTk.PhotoImage(Jfa)

Jfb = Image.open(".\\Layout\\PROJECT\\Jf\\Cg.png")
Jf3 = ImageTk.PhotoImage(Jfb)

Jfc = Image.open(".\\Layout\\PROJECT\\Jf\\Cn.png")
Jf4 = ImageTk.PhotoImage(Jfc)

Jfd = Image.open(".\\Layout\\PROJECT\\Jf\\Cr.png")
Jf5 = ImageTk.PhotoImage(Jfd)

Jfe = Image.open(".\\Layout\\PROJECT\\Jf\\Sa.png")
Jf6 = ImageTk.PhotoImage(Jfe)

Jff = Image.open(".\\Layout\\PROJECT\\Jf\\Sh.png")
Jf7 = ImageTk.PhotoImage(Jff)

Jfg = Image.open(".\\Layout\\PROJECT\\Jf\\Sm.png")
Jf8 = ImageTk.PhotoImage(Jfg)

#----------Image location of Jennifer------------#

Jn = Image.open(".\\Layout\\PROJECT\\Jn\\De.png")
Jn1 = ImageTk.PhotoImage(Jn)

Jna = Image.open(".\\Layout\\PROJECT\\Jn\\An.png")
Jn2 = ImageTk.PhotoImage(Jna)

Jnb = Image.open(".\\Layout\\PROJECT\\Jn\\Ao.png")
Jn3 = ImageTk.PhotoImage(Jnb)

Jnc = Image.open(".\\Layout\\PROJECT\\Jn\\Cr.png")
Jn4 = ImageTk.PhotoImage(Jnc)

Jnd = Image.open(".\\Layout\\PROJECT\\Jn\\Df.png")
Jn5 = ImageTk.PhotoImage(Jnd)

Jne = Image.open(".\\Layout\\PROJECT\\Jn\\Sh.png")
Jn6 = ImageTk.PhotoImage(Jne)

Jnf = Image.open(".\\Layout\\PROJECT\\Jn\\Sk.png")
Jn7 = ImageTk.PhotoImage(Jnf)

Jng = Image.open(".\\Layout\\PROJECT\\Jn\\Wf.png")
Jn8 = ImageTk.PhotoImage(Jng)

Jnh = Image.open(".\\Layout\\PROJECT\\Jn\\Wo.png")
Jn9 = ImageTk.PhotoImage(Jnh)

#----------Image location of Lily------------#

Li = Image.open(".\\Layout\\PROJECT\\Li\\De.png")
Li1 = ImageTk.PhotoImage(Li)

Lia = Image.open(".\\Layout\\PROJECT\\Li\\Cd.png")
Li2 = ImageTk.PhotoImage(Lia)

Lib = Image.open(".\\Layout\\PROJECT\\Li\\Dy.png")
Li3 = ImageTk.PhotoImage(Lib)

Lic = Image.open(".\\Layout\\PROJECT\\Li\\Ss.png")
Li4 = ImageTk.PhotoImage(Lic)

Lid = Image.open(".\\Layout\\PROJECT\\Li\\Wo.png")
Li5 = ImageTk.PhotoImage(Lid)

#----------Image location of Luna------------#

Lu = Image.open(".\\Layout\\PROJECT\\Lu\\De.png")
Lu1 = ImageTk.PhotoImage(Lu)

Lua = Image.open(".\\Layout\\PROJECT\\Lu\\An.png")
Lu2 = ImageTk.PhotoImage(Lua)

Lub = Image.open(".\\Layout\\PROJECT\\Lu\\Cr.png")
Lu3 = ImageTk.PhotoImage(Lub)

Luc = Image.open(".\\Layout\\PROJECT\\Lu\\Dr.png")
Lu4 = ImageTk.PhotoImage(Luc)

Lud = Image.open(".\\Layout\\PROJECT\\Lu\\Sm.png")
Lu5 = ImageTk.PhotoImage(Lud)

#----------Image location of Trey------------#

Tr = Image.open(".\\Layout\\PROJECT\\Tr\\De.png")
Tr1 = ImageTk.PhotoImage(Tr)

Tra = Image.open(".\\Layout\\PROJECT\\Tr\\An.png")
Tr2 = ImageTk.PhotoImage(Tra)

Trb = Image.open(".\\Layout\\PROJECT\\Tr\\Co.png")
Tr3 = ImageTk.PhotoImage(Trb)

Trc = Image.open(".\\Layout\\PROJECT\\Tr\\Cr.png")
Tr4 = ImageTk.PhotoImage(Trc)

Trd = Image.open(".\\Layout\\PROJECT\\Tr\\Sa.png")
Tr5 = ImageTk.PhotoImage(Trd)

Tre = Image.open(".\\Layout\\PROJECT\\Tr\\Sm.png")
Tr6 = ImageTk.PhotoImage(Tre)

#----------Image location of Wally------------#

Wa = Image.open(".\\Layout\\PROJECT\\Wa\\De.png")
Wa1 = ImageTk.PhotoImage(Wa)

Waa = Image.open(".\\Layout\\PROJECT\\Wa\\An.png")
Wa2 = ImageTk.PhotoImage(Waa)

Wab = Image.open(".\\Layout\\PROJECT\\Wa\\Cr.png")
Wa3 = ImageTk.PhotoImage(Wab)

Wac = Image.open(".\\Layout\\PROJECT\\Wa\\Sa.png")
Wa4 = ImageTk.PhotoImage(Wac)

Wad = Image.open(".\\Layout\\PROJECT\\Wa\\Wh.png")
Wa5 = ImageTk.PhotoImage(Wad)

Wae = Image.open(".\\Layout\\PROJECT\\Wa\\Wo.png")
Wa6 = ImageTk.PhotoImage(Wae)

#------------Image Location Of Layout 1----------#

bg = Image.open(".\\Layout\Layout1\\Background-Intro.png")
mbg = ImageTk.PhotoImage(bg)

title1=Image.open(".\\Layout\Layout1\\Title-1.png")
title1_1=ImageTk.PhotoImage(title1)

load_btn=Image.open(".\\Layout\Layout1\\Load_Game-1.png")
load_btn1=ImageTk.PhotoImage(load_btn)

new_btn=Image.open(".\\Layout\Layout1\\New_Game-1.png")
new_btn1=ImageTk.PhotoImage(new_btn)

exit_btn=Image.open(".\\Layout\Layout1\\Exit-1.png")
exit_btn1=ImageTk.PhotoImage(exit_btn)

set_btn=Image.open(".\\Layout\Layout1\\Settings-1.png")
set_btn1=ImageTk.PhotoImage(set_btn)

#-------------Settings Layout Location---------------#

bg1 = Image.open(".\\Layout\Layout1\\Background-Settings.png")
mbg1 = ImageTk.PhotoImage(bg1)

title2=Image.open(".\\Layout\Layout1\\Title-2.png")
title2_1=ImageTk.PhotoImage(title2)

ins_btn=Image.open(".\\Layout\Layout1\\Instructions-1.png")
ins_btn1=ImageTk.PhotoImage(ins_btn)

gb_btn=Image.open(".\\Layout\Layout1\\Back-1.png")
gb_btn1=ImageTk.PhotoImage(gb_btn)

ts_btn=Image.open(".\\Layout\Layout1\\Title_Screen.png")
ts_btn1=ImageTk.PhotoImage(ts_btn)

#--------------Image Location Of Instructions-----------#

insbg=Image.open(".\\Layout\\Instructions\\Instructions.png")
insbg1=ImageTk.PhotoImage(insbg)

insback=Image.open(".\\Layout\\Instructions\\BackButton2.png")
insback1=ImageTk.PhotoImage(insback)

#---------------Image Location Of Prologue--------------#

text=Image.open(".\\Layout\\Prologue\\Text1.png")
text1=ImageTk.PhotoImage(text)

bdrop=Image.open(".\\Layout\\Prologue\\Backdrop.jpg")
bdrop1=ImageTk.PhotoImage(bdrop)

start=Image.open(".\\Layout\\Prologue\\StartG.png")
start1=ImageTk.PhotoImage(start)

nextb=Image.open(".\\Layout\\Prologue\\next.png")
nextb1=ImageTk.PhotoImage(nextb)

startg= Button(root,image=start1, borderwidth=0, command=move, cursor='hand2', bg="black")
ts_button= Button(root,image=ts_btn1, command=title, borderwidth=0, cursor='hand2', bg="black")

#-------------------Image location of layout 2------------------#

bgd=Image.open(".\\Layout\\Layout2\\bgd.png")
bgd1=ImageTk.PhotoImage(bgd)

db=Image.open(".\\Layout\\Layout2\\Dialogue_box1.png")
db1=ImageTk.PhotoImage(db)

nxt=Image.open(".\\Layout\\Layout2\\Nxt.png")
nxt1=ImageTk.PhotoImage(nxt)

#------------------Image location layout 3-------------------------#

bgd2=Image.open(".\\Layout\\Layout3\\wood_land.png")
bgd12=ImageTk.PhotoImage(bgd2)

tb2=Image.open(".\\Layout\\Layout3\\Text_box2.png")
tb12=ImageTk.PhotoImage(tb2)

nxt2=Image.open(".\\Layout\\Layout3\\Nxt2.png")
nxt12=ImageTk.PhotoImage(nxt2)

#------------------Image location layout 4----------------------#

bgd3=Image.open(".\\Layout\\Layout4\\dead_land.png")
bgd13=ImageTk.PhotoImage(bgd3)

tb3=Image.open(".\\Layout\\Layout4\\text_box3.png")
tb13=ImageTk.PhotoImage(tb3)

nxt3=Image.open(".\\Layout\\Layout4\\Nxt3.png")
nxt13=ImageTk.PhotoImage(nxt3)

#-------------------Image location layout 5----------------------#

bgd0=Image.open(".\\Layout\\Layout5\\blood_land.png")
bgd10=ImageTk.PhotoImage(bgd0)

tb0=Image.open(".\\Layout\\Layout5\\dialogue_blood.png")
tb10=ImageTk.PhotoImage(tb0)

nxt0=Image.open(".\\Layout\\Layout5\\next_blood.png")
nxt10=ImageTk.PhotoImage(nxt0)

#----------------------Choices Location-------------------#

chbg=Image.open(".\\Layout\\Choices\\Choicesbg.png")
chbg1=ImageTk.PhotoImage(chbg)

ch1=Image.open(".\\Layout\\Choices\\Choice1.png")
ch11=ImageTk.PhotoImage(ch1)

ch2=Image.open(".\\Layout\\Choices\\Choice2.png")
ch21=ImageTk.PhotoImage(ch2)

ch3=Image.open(".\\Layout\\Choices\\Choice3.png")
ch31=ImageTk.PhotoImage(ch3)

#----------------------Chekpoint--------------------------#

zx1=Image.open(".\\Layout\\Checkpoint\\zx1.png")
zx11=ImageTk.PhotoImage(zx1)

zx2=Image.open(".\\Layout\\Checkpoint\\zx2.png")
zx12=ImageTk.PhotoImage(zx2)

zx3=Image.open(".\\Layout\\Checkpoint\\zx3.png")
zx13=ImageTk.PhotoImage(zx3)

zx4=Image.open(".\\Layout\\Checkpoint\\zx4.png")
zx14=ImageTk.PhotoImage(zx4)

zx5=Image.open(".\\Layout\\Checkpoint\\zx5.png")
zx15=ImageTk.PhotoImage(zx5)

zx6=Image.open(".\\Layout\\Checkpoint\\zx6.png")
zx16=ImageTk.PhotoImage(zx6)

zx7=Image.open(".\\Layout\\Checkpoint\\zx7.png")
zx17=ImageTk.PhotoImage(zx7)

zx8=Image.open(".\\Layout\\Checkpoint\\zx8.png")
zx18=ImageTk.PhotoImage(zx8)

zx9=Image.open(".\\Layout\\Checkpoint\\zx9.png")
zx19=ImageTk.PhotoImage(zx9)

zx10=Image.open(".\\Layout\\Checkpoint\\zx10.png")
zx110=ImageTk.PhotoImage(zx10)

next_chck=Image.open(".\\Layout\\Checkpoint\\Next_chck.png")
next_chck1=ImageTk.PhotoImage(next_chck)

#-----------------------Game Over-------------------------#

gobg=Image.open(".\Layout\Game_Over\gobg.png")
gobg1=ImageTk.PhotoImage(gobg)

goo=Image.open(".\Layout\Game_Over\GameOver.png")
goo1=ImageTk.PhotoImage(goo)

golc=Image.open(".\Layout\Game_Over\golc.png")
golc1=ImageTk.PhotoImage(golc)

gots=Image.open(".\Layout\Game_Over\gots.png")
gots1=ImageTk.PhotoImage(gots)

#------------------------End Game------------------------#

endbg=Image.open(".\\Layout\\End_Screen\\ENDBG.png")
endbg1=ImageTk.PhotoImage(endbg)

endts=Image.open(".\\Layout\\End_Screen\\LIA.png")
endts1=ImageTk.PhotoImage(endts)

#---------------------Start of the program-------------------#

title()
root.mainloop()
