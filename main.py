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
		
		elif afterattack.HP > 0:
			message = '{} has {} point remaining'.format(afterattack.name, afterattack.HP)
		print (message)

alex = kalusfighter(ATK=20, HP=100, MP=50, name='alex', job='saber')
bob = kalusfighter(ATK=30, HP=200, MP=200, name='bob', job='archer')

print ('{} is a {}, ATK:{}, HP:{}, MP:{} '.format(alex.name, alex.job, alex.ATK, alex.HP, alex.MP))
print ('{} is a {}, ATK:{}, HP:{}, MP:{} '.format(bob.name, bob.job, bob.ATK, bob.HP, bob.MP))