# Inlezen ledenlijst zoals aangeleverd

with open('klas_a.txt') as a:
    ledenlijst = a.read().splitlines()

with open('certified secure.txt') as b:
    ledenlijst_website = b.read().splitlines()


for lid in ledenlijst:
    if lid not in ledenlijst_website:
        print lid + " Heeft CS nog niet gehaald."
