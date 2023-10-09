# Aufgabe: Schreibe eine Funktion, welche Dominosteine bis zu einer gewissen
# Grenze erzeugt. Die Dominosteine können z.B. so aussehen:
# (1|1), (1|2), (1|3), (2|2), (2|3), (3|3) ...
# Es dürfen dabei jedoch KEINE Duplikate auftreten! Ist bspw. (1|2) schon erzeugt,
# darf (2|1) nicht nochmals erzeugt werden, usw.

list = []
def dominoSteine(x):
    for i in range(1, 4):
        for j in range(1, 4):
            domiTuple = "({}|{})".format(i, j)
            reversedDomiTuple = "({}|{})".format(j, i)
            if domiTuple in list:
                print("Fuck off")
            elif reversedDomiTuple in list:
                print("Fuck off²")
            else:
                list.append(domiTuple)
    print(list)

dominoSteine(3)