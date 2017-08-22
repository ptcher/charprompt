from nltk.corpus import wordnet as wn
import random


def sampleprint(P,k=5):
    for i in range(5):
        p = random.choice(P)
        print(";".join([x.name() for x in p.lemmas()]), ":", p.definition())

def readin(infile):
    words = set()
    for l in open(infile).readlines():
        words.add(l.strip().split(" ")[0])
    return sorted(words)

P = []
for ss in wn.all_synsets("n"): 
    if ss.lexname() == "noun.person" and str(ss.definition).count("inhabit") < 1 and str(ss.definition).count("living") < 1 and len(ss.instance_hypernyms()) < 1:
        P.append(ss)
sampleprint(P)


P = []
for ss in wn.all_synsets("a"):
    P.append(ss)
sampleprint(P)



female = readin("female.txt")
male = readin("male.txt")
surname = readin("surname.txt")

print(random.choice(surname),"{", random.choice(female),",",random.choice(male),"}")
