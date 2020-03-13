import math
from random import randint

def generate_data(n):
	a = '1'
	for i in range(n):
		a += str(randint(0,1))
	return a

def compress(a):
	end = []
	a1 = a.split("1")
	a2 = a.split("0")
	a1 = [i for i in a1 if i]
	a2 = [i for i in a2 if i]
	for	i, j in zip(a2,a1):
		end.append(len(i))
		end.append(len(j))
	end.append(len(a2[-1]))
	return end
def decompres(a):
	pass

if __name__ == "__main__":
	data = bin(randint(100,150))[2:]
	print(data,"\n")
	print(bin(int("".join(str(i) for i in compress(data))))[2:])