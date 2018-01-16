class kalusfighter(object):
    def __init__(Person, ATK, HP, MP, name, job):
        Person.HP = HP
        Person.MP = MP
        Person.name = name
        Person.job = job
        Person.ATK = ATK

    def attack(Person, afterattack):
        afterattack.HP -= Person.ATK

        if afterattack.HP <= 0:
            message = '{} dead'.format(afterattack.name)
            aftermagic_fire.HP = 0
        
        elif afterattack.HP > 0:
            message = '{} has {} point remaining'.format(afterattack.name, afterattack.HP)
        print (message)


    def magic_fire(Person, aftermagic_fire):
        aftermagic_fire.HP -= 90

        if aftermagic_fire.HP <= 0:
            message = '{} dead'.format(aftermagic_fire.name)
            aftermagic_fire.HP = 0
        
        elif aftermagic_fire.HP > 0:
            message = '{} has {} point remaining'.format(aftermagic_fire.name, aftermagic_fire.HP)
        print（'BOOMMMMM!!!!!'）
        print (message)


    def magic_heal(Person, aftermagic_heal):
        if Person.HP > 0:
            aftermagic_heal.HP += 100

            if aftermagic_heal.HP >= Person.HP + 100:
                message = "{} don't need any heal".format(aftermagic_heal.name)
                aftermagic_heal.HP = Person.HP

            elif aftermagic_heal.HP > 0 and aftermagic_heal.HP < Person.HP + 100:
                aftermagic_heal.HP = Person.HP
                message = '{} has {} point remaining'.format(aftermagic_heal.name, aftermagic_heal.HP)
            
            elif aftermagic_heal.HP > 0:
                message = '{} has {} point remaining'.format(aftermagic_heal.name, aftermagic_heal.HP)
                
        elif Person.HP == 0:
            message = "it's impossible."
        print (message)
            

def status(Person):
    if Person.HP <= 0:
        print('dead.')
    elif Person.HP > 0:
        print ('{} is a {}, ATK:{}, HP:{}, MP:{} '.format(Person.name, Person.job, Person.ATK, Person.HP, Person.MP))

alex = kalusfighter(ATK=20, HP=100, MP=50, name='alex', job='saber')
bob = kalusfighter(ATK=30, HP=200, MP=200, name='bob', job='archer')

print（'Welcome!'）
print ('{} is a {}, ATK:{}, HP:{}, MP:{} '.format(alex.name, alex.job, alex.ATK, alex.HP, alex.MP))
print ('{} is a {}, ATK:{}, HP:{}, MP:{} '.format(bob.name, bob.job, bob.ATK, bob.HP, bob.MP))