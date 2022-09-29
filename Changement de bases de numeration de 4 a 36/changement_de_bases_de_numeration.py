# Il est possible de passer de n'importe quelle base à
# une autre directement, mais utiliser la base 10,
# comme pivot, est ce qu'il y a de plus facile 
# à coder
class convertisseur_de_bases:
	def __init__(self, base):
		if (base>36):
			print("Erreur : La base est suppérieure à 36 : le convertisseur ne peut pas fonctionner.")
			return
		symboles_complets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.symboles = symboles_complets[0:int(base)]
		self.sym2val = {l: i for i, l in enumerate(self.symboles)}
		self.val2sym = dict(enumerate(self.symboles))
 
	def to_base_10(self, nombre):
		i = 0
		string = str(nombre)
		base = len(self.sym2val)
		# On part de la gauche vers la droite,
		# donc on commence avec les valeurs les plus
		# grosses.
		# Pour chaque symbole, on ajoute la valeur
		# de celui-ci (donnée par la table) et
		# avec facteur lié à sa position.
		for c in string:
			i *= base
			i += self.sym2val[c]
		return i
 
	def from_base_10(self, nombre):
		""" Convert from a base 10 to the custom base"""
		number = int(nombre)
		array = []
		base = len(self.val2sym)
		# Division euclidienne en boucle jusqu'à ce que le
		# reste soit égal à zero.
		while number:
			number, value = divmod(number, base)
			# Le résultat est l'index du symbole.
			# On le place le plus à gauche, chaque
			# symbole ayant une valeur plus grande
			# que le précédent.
			array.insert(0, self.val2sym[value])
 
		# Ne pas oublier le zéro
		return ''.join(array) or self.symboles[0]

###########################################################################

################### Fonctions utilitaires ####################

def is_number(a):
	chiffres = [".", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	nombre_de_points = 0
	a_tmp = (str)(a)

	if (a==""):
		return False
	j = 0
	for i in a_tmp:
		if (i=="-" and j>0):
			return False
		if (i=="."):
			nombre_de_points+=1
		if (nombre_de_points>1):
			return False
		if i not in chiffres:
			return False
		j+=1
	return True

def is_number_base(nombre, base):
	chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	if (not is_number(nombre)):
		return False

	nombre_str = str(nombre)
	for i in nombre:
		if (i in chiffres):
			if (int(i)>=base):
				return False

	return True	

def is_integer(a):
	if (is_number(a)):
		return ("." not in str(a))
	else:
		return False

def entre_nombre(phrase):
	cmp = 0
	res = ""
	while (not is_number(res)):
		if (cmp>0):
			print("\nVeuiller entrer un nombre")
		res = input(phrase)
		cmp+=1
	if (is_integer(res)):
		return int(res)
	else:
		return float(res)

def entre_nombre_base(base, phrase):
	cmp = 0
	res = ""
	while (not is_number_base(res, base)):
		if (cmp>0):
			print("\nVeuiller entrer un nombre en base "+str(base)+" : ")
		res = input(phrase)
		cmp+=1
	if (is_integer(res)):
		return int(res)
	else:
		return float(res)

def entre_entier(phrase):
	cmp = 0
	res = ""
	while (not is_integer(res)):
		if (cmp>0):
			print("\nVeuiller entrer un entier")
		res = input(phrase)
		cmp+=1
	return int(res)

############# Fonctions utilitiares importantes ################

def entre_base(max, phrase):
	base = -1
	while (base<2 or base>max):
		print("La base doit être suppérieure ou égale à 2 et inférieure à "+str(max)+" : ")
		base = entre_entier(phrase)
	return base

#################### Fonctions principales #####################

'''
	L'opération se fait dans ce sens :
		n1<opérateur>n2

	Valeurs possibles de operation :
		'+', '-', '*', '/', '%', '//', '**'
'''
def operation (n1, n2, base, operation):
	operations_possibles = ['+', '-', '*', '/', '%', '//', '**']
	if (operation not in operations_possibles):
		print("operation : "+str(operation)+" n'est pas une opération possible")
		return -1
	conv = convertisseur_de_bases(base)
	n1_b = conv.to_base_10(n1)
	n2_b = conv.to_base_10(n2)

	if (operation=='+'):
		res_b = n1_b+n2_b
	if (operation=='-'):
		res_b = n1_b-n2_b
	if (operation=='*'):
		res_b = n1_b*n2_b
	if (operation=='/'):
		res_b = n1_b/n2_b
	if (operation=='%'):
		res_b = n1_b%n2_b
	if (operation=='//'):
		res_b = n1_b//n2_b
	if (operation=='**'):
		res_b = n1_b**n2_b

	res = conv.from_base_10(res_b)
	return res

'''
	Renvoie n1 en base2
'''
def change_base(n1, base1, base2):
	conv_b1 = convertisseur_de_bases(base1)
	conv_b2 = convertisseur_de_bases(base2)

	res1 = conv_b1.to_base_10(n1)
	res2 = conv_b2.from_base_10(res1)

	return res2	

def tests():
	base = 12
	conv = convertisseur_de_bases(base)

	'''
	for i in range(base):
		print(conv.from_base_10(i))

	for i in range(10):
		print(i, "=", calcul_numerologie(conv.from_base_10(i), base))

	for i in range(100):
		print(multiplie_base(2, conv.from_base_10(i), base))

	doublage(base)
	'''
	tmp = addition_base(conv.from_base_10(99), conv.from_base_10(99), base)
	print("("+str(tmp)+")(12)")
	print("("+str(conv.to_base_10(tmp))+")(10)")

##################### Menu #####################

def menu ():
	q = 0
	while (q<1 or q>2):
		print("\nMenu :\n")
		print("1 : Changer un nombre de base")
		print("2 : Changer plusieurs nombres de base")
		q = entre_entier("? = ")
	return q

##################### Main #####################	

def execution_principale():
	max_base = 36
	bool = True
	q = menu()
	if (q==1 or q==2):
		base1 = entre_base(max_base, "\nBase initiale = ")
		base2 = entre_base(max_base, "Base finale = ")
		while (bool):

			nombre = entre_nombre_base(base1, "\nNombre = ")
			res = change_base(nombre, base1, base2)
			print("\nres =", res)

			if (q==2):
				bool = True
			else:
				bool = False

def main():
	while (True):
		execution_principale()

#tests()
main()