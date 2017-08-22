from nltk.corpus import wordnet as wn
import random


def sampleprint(P,k=5):
    for _ in range(k):
        p = random.choice(P)
        print " ".join([";".join([x.name() for x in p.lemmas()]), ":", p.definition()])

def readin(infile):
    return [line.rstrip() for line in open(infile).readlines()]

professions = []
for ss in wn.all_synsets("n"): 
    if ss.lexname() == "noun.person" and str(ss.definition).count("inhabit") < 1 and str(ss.definition).count("living") < 1 and len(ss.instance_hypernyms()) < 1:
        professions.append(ss)
sampleprint(professions, 1)


adjectives = []
for ss in wn.all_synsets("a"):
    adjectives.append(ss)
sampleprint(adjectives, 3)


instincts = readin("instincts.txt")
knacks = readin("knacks.txt")

print "Instinct: " + random.choice(instincts)
print "Knack: " + random.choice(knacks)
