word1 = "downdraft"
word2 = "downdraft "
word3 = "down" + "draft"

print("word1==word2?", word1==word2)
print("word1==word3?", word1==word3)

sent1 = "oMg hAxOrs HACKED MY COMPUTER!"
sent2 = "OMG Haxors hacked my computer!"
sent3 = "Omg haxors hacked my computer!"

print("sent1.lower()==sent2.lower()?",
       sent1.lower()==sent2.lower())
print("sent1.lower()==sent3.lower()?",
       sent1.lower()==sent3.lower())

print("4/2==2?", 4/2==2)
print(".1+.1+.1==.3?",.1+.1+.1==.3)
print(format(.1,".30g")) #30 digits
#Approximation is good to 16 digits
print(format(.1+.1+.1,".30g"))
print(format(.3,".30g"))

print(".1+.1+.1>.3?",.1+.1+.1>.3)
print(format(.1*3,".30g"))
print(".1*3>.1+.1+.1?",.1*3>.1+.1+.1)
print(".1*3<.1+.1+.1?",.1*3<.1+.1+.1)

#and, or, in, not in

li = []
print("len(li)==1 and 'a' in li?",
    len(li)==1 and 'a' in li)
print("len(li)==1 or 'a' in li?",
    len(li)==1 or 'a' in li)

print("len(li)==1 and li[0]=='a'?",
    len(li)==1 and li[0]=='a')
try:
    print("len(li)==1 or li[0]=='a'?",
        len(li)==1 or li[0]=='a')
except Exception as E:
    print(E)

print("len(li)==1 and 'a' not in li?",
    len(li)==1 and 'a' not in li)
print("len(li)==1 or 'a' not in li?",
    len(li)==1 or 'a' not in li)