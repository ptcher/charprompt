from nltk.corpus import wordnet as wn
import random


def sampleprint(P,k=5):
    for i in range(5):
        p = random.choice(P)
        print " ".join([";".join([x.name() for x in p.lemmas()]), ":", p.definition()])

def readin(infile):
    return [line.rstrip() for line in open(infile).readlines()]

P = []
for ss in wn.all_synsets("n"): 
    if ss.lexname() == "noun.person" and str(ss.definition).count("inhabit") < 1 and str(ss.definition).count("living") < 1 and len(ss.instance_hypernyms()) < 1:
        P.append(ss)
sampleprint(P)


P = []
for ss in wn.all_synsets("a"):
    P.append(ss)
sampleprint(P)


instincts = readin("instincts.txt")
knacks = readin("knacks.txt")

print "Instinct: " + random.choice(instincts)
print "Knack: " + random.choice(knacks)
