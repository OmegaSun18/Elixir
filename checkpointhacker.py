import pickle
a=open(".\\loadfile.bin","wb")
b=5
name="Joe"
pn1="his"
pn2="he"
pn3="him"
#above ones are default pronouns, can change

pickle.dump(b,a)
pickle.dump(name,a)
pickle.dump(pn1,a)
pickle.dump(pn2,a)
pickle.dump(pn3,a)

a.close()
