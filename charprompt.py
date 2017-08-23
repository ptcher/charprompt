from nltk.corpus import wordnet as wn
import random
from timeit import timeit


def sampleprint(P,k=5):
    for _ in range(k):
        p = random.choice(P)
        print "%s: %s " % (";".join([x.name() for x in p.lemmas()]), p.definition())

def readin(infile):
    return [line.rstrip() for line in open(infile).readlines()]

professions = [ss for ss in wn.all_synsets("n") if 
        ss.lexname() == "noun.person" and str(ss.definition).count("inhabit") < 1 and 
        str(ss.definition).count("living") < 1 and 
        len(ss.instance_hypernyms()) < 1]

adjectives = list(wn.all_synsets("a"))

instincts = readin("instincts.txt")
knacks = readin("knacks.txt")

sampleprint(professions, 1)
sampleprint(adjectives, 3)
print "Instinct: %s" % random.choice(instincts)
print "Knack: %s" % random.choice(knacks)
