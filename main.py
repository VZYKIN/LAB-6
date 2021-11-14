
      
num=int(input('Введите число, состоящее только из 6 и 9'))
def rot(num):
	num = str(num)
	num = num.replace('6', '9', 1)
	return int(num)

print(rot(num))
