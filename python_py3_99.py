#-*- coding: utf8 -*-
string = ''
for i in range(1,10):
	for j in range(1,10):
			string = str(j)+'乘'+str(i)+'等於'+str(j*i) + '\n'
		
			string = string.replace('1','一')
			string = string.replace('2','二')
			string = string.replace('3','三')
			string = string.replace('4','四')
			string = string.replace('5','五')
			string = string.replace('6','六')
			string = string.replace('7','七')
			string = string.replace('8','八')
			string = string.replace('9','九')

			print(string)