#Замыкание для отслеживания количества HP героя - HP не может 
#подниматься больше 100 и опускаться ниже 0, герой может лечиться 
#или получать урон.

def hero():
    hp = 100

    def heal(x):
        nonlocal hp 
        hp = hp + x
        return hp
    
    def damage(x):
        nonlocal hp
        hp = hp - x
        return hp
    
    return heal, damage

heal, damage = hero()
print(damage(30))
print(heal(10))
