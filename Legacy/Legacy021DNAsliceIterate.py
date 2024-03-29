#Take input sequence, cut into random sequences of X length.
#Iterate: Do X times
#Using preset base sequence instead of randomly generated one so as to be able to compare slices from multiple iterations.

#Convention: dnaXSeq = ternary, dnaXNuc = nucleotides, baseline assumption = ternary.
#Add handling for if is ternary or nucleotides.


import random

nucDict = {
    "0": "A",
    "1": "T",
    "2": "C",
    "3": "G"
}

def convDNA(y):
    nuclist = nucDict[c] for c in y
 
    return(''.join(nuclist))

#Can implement using map, list comprehension, or lambda?

#map implementation - working
def convDNAlistMap(y):
    xSeq = list(map(convDNA, y))

    return(xSeq)

#lambda impementation - working
def convDNAlistLambda(y):
    xSeq = []
    for z in y:
        xSeq.append(convDNA(z))

    return(xSeq)

#list comprehension - working   
def convDNAlistlc(y):
    xSeq = [convDNA(y) for y in y]

    return(xSeq)

def randDNA(p):
    dnaTemp = ""
    for i in range(p):
        temp = str(random.randint(0, 3))
        dnaTemp += temp

    return(dnaTemp)

def sliceDNA25(y):
    basel = 25 #number of bases to grab for slice
    randStart = random.randint(0, (len(y)))
    lst = [c for c in y]
    if basel + randStart >= len(y):
        basel = (len(y) - randStart)
    dnaSliceSeq = [lst[i] for i in range(randStart, randStart + basel)]

    return(''.join(dnaSliceSeq))



#150 bp sequence, issue with leading 0s "SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers"
dnaSeq = '103021302212310123102231322112221323123310232002211332213012211231121112223210101103033200012301011013232013221120010022111031320030100000001321023023'

dnaNuc = convDNA(dnaSeq)
#dnaSeq_sliced = sliceDNA25(dnaSeq)
#dnaNuc_sliced = convDNA(dnaSeq_sliced) 

print("Original sequence of 150 bases is:", dnaSeq, "or in nucleotides:", ''.join(dnaNuc))
#print("Sliced sequence is:", dnaSeq_sliced, "or in nucleotides:", ''.join(dnaNuc_sliced))

print("How many random 25 base slices should we generate?")

#n = int(input())
#commenting out and adding below time to avoid needing input
n = 5

dnaSeqSlices = [sliceDNA25(dnaSeq) for i in range(n)] 
print("Slices are: ", dnaSeqSlices)

dnaNucSlices = convDNAlistLambda(dnaSeqSlices) #convDNA canot ingest lists. Create function that can?
print(dnaNucSlices)