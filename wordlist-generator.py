#!/usr/bin/python
#encoding: utf-8

import sys as S
import datetime as D
import string

argv_acceptable = ('-t1','-t2','-t3','-t9')

class WordListGenerator:
	def __init__(self, max_wordsize = 0):
		self.max_wordsize = max_wordsize
		self.number_lowchars = string.printable[:35]  #62 #!@#$%&*
		self.numbers = string.printable[:10]
		self.lowchars = string.printable[10:35]
		self.upperchars = string.printable[36:62]
		self.word = ['0']*max_wordsize
	
		
	def t9_implementation(self):
		strDateTime = str(D.datetime.today().strftime('%Y-%m-%d %H-%M-%S'))
		self.file_generated = open('./'+strDateTime+'_generated-wlist.txt','a')
		self.t9_recursive_for()
		self.file_generated.close()
	

	def t9_recursive_for(self,layer=0):	
		for char in self.number_lowchars:
			if layer == self.max_wordsize:
				print("".join(self.word))
				self.file_generated.write("".join(self.word)+'\n')
				break
			else:
				self.word[layer] = str(char)
				self.t9_implementation(layer+1)
		

	def t1_implementation(self, name):
		self.file_generated = open(name+'_t1_combinations.txt','a')
		combinations_counter = 0
		years = [ y for y in range(1960,2021) ]
		
		for y in years:
			self.file_generated.write(name+str(y)+'\n')
			self.file_generated.write(str(y)+name+'\n')
			self.file_generated.write(name.title()+str(y)+'\n')
			self.file_generated.write(str(y)+name+'\n')
			
			self.file_generated.write(name+'_'+str(y)+'\n')
			self.file_generated.write(str(y)+'_'+name+'\n')
			self.file_generated.write(name.title()+'_'+str(y)+'\n')
			self.file_generated.write(str(y)+'_'+name+'\n')
			
			combinations_counter+=8
			
		for y in years:
			for m in range(1,13):
				self.file_generated.write(name+str(y)+str(m).zfill(2)+'\n')
				self.file_generated.write(name+str(m).zfill(2)+str(y)+'\n')
				self.file_generated.write(name.title()+str(y)+str(m).zfill(2)+'\n')
				self.file_generated.write(name.title()+str(m).zfill(2)+str(y)+'\n')
				
				self.file_generated.write(name+'_'+str(y)+str(m).zfill(2)+'\n')
				self.file_generated.write(name+'_'+str(m).zfill(2)+str(y)+'\n')
				self.file_generated.write(name.title()+'_'+str(y)+str(m).zfill(2)+'\n')
				self.file_generated.write(name.title()+'_'+str(m).zfill(2)+str(y)+'\n')
				
				combinations_counter+=8
				
		for y in years:
			for m in range(1,13):
				for d in range(1,32):
					self.file_generated.write(name+str(y)+str(m).zfill(2)+str(d).zfill(2)+'\n')
					self.file_generated.write(name+str(d).zfill(2)+str(m).zfill(2)+str(y)+'\n')
					self.file_generated.write(name.title()+str(y)+str(m).zfill(2)+str(d).zfill(2)+'\n')
					self.file_generated.write(name.title()+str(d).zfill(2)+str(m).zfill(2)+str(y)+'\n')
					
					self.file_generated.write(name+'_'+str(y)+str(m).zfill(2)+str(d).zfill(2)+'\n')
					self.file_generated.write(name+'_'+str(d).zfill(2)+str(m).zfill(2)+str(y)+'\n')
					self.file_generated.write(name.title()+'_'+str(y)+str(m).zfill(2)+str(d).zfill(2)+'\n')
					self.file_generated.write(name.title()+'_'+str(d).zfill(2)+str(m).zfill(2)+str(y)+'\n')
					
					combinations_counter+=8
		print(str(combinations_counter) + ' combinations generated! ')
		self.file_generated.close()
		

	def _recursive_numbers(self, max_size, layer=0):
		for num in self.numbers:
			if layer == max_size:
				self.numbers_combination.append("".join(self.word))
				break	
			else:
				self.word[layer] = str(num)
				self._recursive_numbers(max_size,layer+1)


	def _recursive_chars(self, max_size, layer=0):
		for char in self.lowchars:
			if layer == max_size:
				self.chars_combination.append("".join(self.word))
				break
			else:
				self.word[layer] = char
				self._recursive_chars(max_size,layer+1)


	def t2_implementation(self, ssid):
		self.file_generated = open(ssid+'_t2_combinations.txt','a')
		combinations_counter = 0

		ssid = ssid.lower
		ssid = str(ssid).replace('fibra-victory-','')
		
		self.word = ['']*2
		self.chars_combination = []
		self._recursive_chars(max_size=2)
		
		
		self.word = ['']*4
		self.numbers_combination = []
		self._recursive_numbers(max_size=4)
		
		for l1 in self.chars_combination:
			for n1 in [2020,2019,2018]:
				for n2 in self.numbers_combination:
					_word = l1+str(n1)+'s'+n2
					print(_word)
					self.file_generated.write(_word+'\n') 
					combinations_counter+=1

		print(str(combinations_counter) + ' combinations generated! ')
		self.file_generated.close()
		

	def t3_implementation(self, name, years):
		self.file_generated = open(name+'_t3_combinations.txt','w')
		combinations_counter=0
		year_list = years.split(',')

		for d in range(1,31):
			for m in range(1,12):
				for y in year_list:
					if '-' in y:
						date_range = y.split('-')
						for d in range(int(date_range[0]), int(date_range[1])):
							print(name+str(d).zfill(2)+str(m).zfill(2)+str(d))
							self.file_generated.write(name+str(d).zfill(2)+str(m).zfill(2)+str(d)+'\n')
							if d > 50:
								self.file_generated.write(name+str(d).zfill(2)+str(m).zfill(2)+'19'+str(d)+'\n')
							else:
								self.file_generated.write(name+str(d).zfill(2)+str(m).zfill(2)+'20'+str(d)+'\n')
							combinations_counter +=2
					else:
						print(name+str(d)+str(m)+str(y))
						self.file_generated.write(name+str(d).zfill(2)+str(m).zfill(2)+str(y)+'\n')
						if d > 50:
							self.file_generated.write(name+str(d).zfill(2)+str(m).zfill(2)+'19'+str(y)+'\n')
						else:
							self.file_generated.write(name+str(d).zfill(2)+str(m).zfill(2)+'20'+str(y)+'\n')
						combinations_counter+=2
		
		for d in range(1,31):
			for m in range(1,12):
				print(name+str(d)+str(m))
				self.file_generated.write(name+str(d).zfill(2)+str(m).zfill(2)+'\n')
				combinations_counter+=1

		for m in range(1,12):					
			for y in year_list:
				if '-' in y:
					date_range = y.split('-')
					for d in range(int(date_range[0]), int(date_range[1])):
						print(name+str(m).zfill(2)+str(d).zfill(2))
						self.file_generated.write(name+str(m).zfill(2)+str(d)+'\n')
						if d > 50:
							print(name+str(m).zfill(2)+'19'+str(d)+'\n')
							self.file_generated.write(name+str(m).zfill(2)+'19'+str(d)+'\n')
						else:	
							print(name+str(m).zfill(2)+'20'+str(d)+'\n')
							self.file_generated.write(name+str(m).zfill(2)+'20'+str(d)+'\n')
						combinations_counter+=2
				else:
					print(name+str(m).zfill(2)+str(y))
					self.file_generated.write(name+str(m).zfill(2)+str(y)+'\n')
					if int(y) > 50:
						print(name+str(m).zfill(2)+'19'+str(y)+'\n')
						self.file_generated.write(name+str(m).zfill(2)+'19'+str(y)+'\n')
					else:
						print(name+str(m).zfill(2)+'20'+str(y)+'\n')
						self.file_generated.write(name+str(m).zfill(2)+'20'+str(y)+'\n')

					combinations_counter+=2

		for y in year_list:
			if '-' in y:
				date_range = y.split('-')
				for d in range(int(date_range[0]), int(date_range[1])):
					print(name+str(d))
					self.file_generated.write(name+str(d)+'\n')
					combinations_counter+=1
					if int(d) > 50:
						print(name+'19'+str(d))
						self.file_generated.write(name+'19'+str(d)+'\n')
						combinations_counter+=1
					else:
						print(name+'20'+str(d))
						self.file_generated.write(name+'20'+str(d)+'\n')
						combinations_counter+=1
			else:
				print(name+str(y))
				self.file_generated.write(name+str(y)+'\n')
				if int(y) > 50:
					print(name+'19'+str(y))
					self.file_generated.write(name+'19'+str(y)+'\n')
				else:
					print(name+'20'+str(y))
					self.file_generated.write(name+'20'+str(y)+'\n')
				combinations_counter+=2

		print(str(combinations_counter) + ' combinations generated! ')
		self.file_generated.close()
				


if __name__ == "__main__":
			
	if S.argv[1] == '-t9': 
		print('This mode is more heavy combination and word bigger as 8 digit \n with all number and low case letters can generate 5.642.219.814.912 combinations, aprox 5Tb.')
		instance = WordListGenerator(int(S.argv[2]))
		instance.t9_implementation()
	
	elif S.argv[1] == '-t1':
		print('This mode combinate some name with, date numbers')
		name = input('Type some name or press [Enter] to generate random:  ')
		instance = WordListGenerator()
		instance.t1_implementation(name)

	elif S.argv[1] == '-t2':
		print('This mode generate some pattern to FIBRA-VICTORY- default\'s password. ')
		network_name = input('Insert the SSID of the network: ')
		instance = WordListGenerator()
		#instance.t2_implementation('fibra-victory-s271')
		instance.t2_implementation(network_name)

	elif S.argv[1] == '-t3':
		print('This mode generate some pattern like name + some date ')
		_name = input('Insert the name: ')
		print('The date list could be one single year or numbers between \'-\'  ')
		_date_list = input('Insert the date list pattern: ')
		instance = WordListGenerator()
		instance.t3_implementation(_name, _date_list)		