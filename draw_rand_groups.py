import random

class Person:
    def __init__(self, name, gruppe):
        self.name = name
        self.gruppe = gruppe
        self.partner = None

class Topf:
    def __init__(self):
        self.init_w = {
        'person1  ' : 1,
        'person2  ' : 2,
        'person3  ' : 2,
        'person4  ' : 3,
        'person5  ' : 3,
        'person6  ' : 4,
        'person7  ' : 4 }

        self.persons = {name : Person(name,gruppe) for name, gruppe in self.init_w.items()}
        self.all_taker = [name for name in self.init_w]
        self.all_picks = [name for name in self.init_w]

    def neu(self):
        self.__init__()

def print_solution(person):
    print("\n=============================")
    for n,w in person.items():
        print(n + " hat " + (w.partner or "___ERROR___") + " gezogen")
    print("=============================\n")

def main():
    debug = False
    random.seed()
    t = Topf()
    c=0
    alle_ziehungen_ok = False
    # Schleife bis alle Ziehungen valide sind
    while(not alle_ziehungen_ok):
        # Schleife einer Ziehung (evtl. nicht fehlerfrei möglich)
        while(not len(t.all_taker) == 0
                and c < len(t.persons)*2 ):
            i = random.randrange(len(t.all_taker))
            taker = t.all_taker[i]

            j = random.randrange(len(t.all_picks))
            pick = t.all_picks[j]

            # ziehung OK?
            if( not taker == pick
                    and not t.persons[taker].gruppe == t.persons[pick].gruppe):
                t.persons[taker].partner = pick
                t.all_taker.pop(i)
                t.all_picks.pop(j)
            else: # Abbruchbedingung
                c = c + 1
                if debug:
                    print(f'c: {c}')
                    if c == len(t.persons)*2: print_solution(t.persons)
        if(len(t.all_taker) == 0):
            alle_ziehungen_ok = True
        else: # neue Runde initialisieren
            t = Topf()
            c=0
            if debug: print("neuer Topf")

    print_solution(t.persons)

main()
