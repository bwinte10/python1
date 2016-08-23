#naive exact match algorithm
# 
def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


# return a reverse compliement
def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t


# parse a DNA reference genome from a file in FASTA format.
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

# parse the read and quality strings from a FASTQ file with reads
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def BaseContent(aBase,str):
    return str.count(aBase) 
   


### main routine
filen=input("Enter the filename")
filen="lambda_virus.fa"

geno=readGenome(filen)

print(geno)

seqLen=len(geno)
print("Sequence is ",seqLen," long.");

Acnt=0
Tcnt=0
Gcnt=0
Ccnt=0

Acnt=BaseContent('A',geno)
print("Check A content . . .",Acnt/seqLen)


Tcnt=BaseContent('T',geno)
print("Check T content . . .",Tcnt/seqLen)

Gcnt=BaseContent('G',geno)
print("Check G content . . . ",Gcnt/seqLen)

Ccnt=BaseContent('C',geno)
print("Check C content . . .",Ccnt/seqLen)

print("To check for percent ", Acnt+Tcnt+Gcnt+Ccnt) 


print("Check for reverse compliement");
instring="TCACTTTACGGGTCCTTTCCGGTGATCCGACAGGTTACG"
print(" Try ",instring)

outstring=reverseComplement(instring)
print("Results in",outstring)

print("Search for substring position")
jj=naive("GATATCCGTCAGGCAATCGACCGTT",geno)
print(jj)
print("Done")
