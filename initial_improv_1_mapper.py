hypsep = False
octave = 1
octmap = 1
maxletter = 97

def ltrmapper(ltrnum):
    ltrnum = ltrnum - 97
    ltroct = int(int(int(ltrnum)/7)/octmap)
    if (ltrnum % 7) >= 2:
        ltroct = ltroct + 1 #remapping over to be based off c instead of a
    ltrval = unichr((ltrnum % 7) + 97)
    ltrstr = str(ltrval) + str(ltroct)
    return ltrstr
    
    

def nameconvert(name):
    retstr = ""
    for ltr in name:
        ltrnum = ord(ltr)
        if ltrnum < 123 and ltrnum >= 97:
            retstr = retstr + " " + ltrmapper(ltrnum)
        else:
            retstr = retstr + " " + ltr
    return retstr
            

person = raw_input("Enter your name: ").strip().lower()
for ltr in person:
    ltrnum = ord(ltr)
    if ltrnum < 123: #is a letter
        maxletter = max(ltrnum, maxletter)
        
names = person.split(" ")
hypsepstr = raw_input("Hyphenated name as separate? (yes or no): ").strip().lower()
if hypsepstr[0] == "y":
    hypsep = True
octavestr = raw_input("Octaves available: ").strip().lower()
octave = max(1, min(4, ord(octavestr[0])))
maxletter = maxletter - 97 #a
octneeded = round(float(maxletter)/7.0 + 0.5)
octmap = int(octave/int(octneeded)) + 1

overallstr = ""
for name in names:
    if hypsep:
        for subname in name.split("-"):
            overallstr = overallstr + " || " + nameconvert(subname)
    else:
        overallstr = overallstr + " || " + nameconvert(name)

overallstr = overallstr + " || "
overallstr = overallstr.strip()

print(overallstr)
            
