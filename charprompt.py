from nltk.corpus import wordnet as wn
import random

# TODO maybe write large sample sets to files (if reading from file is faster than getting them out of wordnet)

def sampleprint(P,k=5):
    for _ in range(k):
        p = random.choice(P)
        print "%s: %s " % (";".join([x.name() for x in p.lemmas()]), p.definition())

def readin(infile):
    return [line.rstrip() for line in open(infile).readlines()]

professions = [ss for ss in wn.all_synsets("n") if 
        ss.lexname() == "noun.person" and 
        str(ss.definition).count("inhabit") < 1 and 
        str(ss.definition).count("living") < 1 and 
        str(ss.definition).count("native") < 1 and
        len(ss.instance_hypernyms()) < 1
        ]

adjectives = list(wn.all_synsets("a"))

instincts = readin("instincts.txt")
knacks = readin("knacks.txt")

while True:
    try:
        raw_input('Push button receive prompt')
        print ""
        sampleprint(professions, 1)
        sampleprint(adjectives, 3)
        print "Instinct: %s" % random.choice(instincts) 
        print "Knack: %s" % random.choice(knacks) 
        print ""
    except:
        print "\nBye!"
        break
