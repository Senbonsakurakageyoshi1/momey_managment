
class Aa:
                id=11
class Bb:
                id=22
class Cc:
                id=33
class Xx(Cc,Bb,Aa):
                pass
print(Xx.id)
