import string
import pyttsx
from gtts import gTTS
import os
from pygame import mixer 
import time 

i = 0
ureg = []
w = len(ureg)
uregcontent = []
def userreg(temp,o):
	#o =w
	if o > 0:
		for t in range(0,w):
			if temp == ureg[t]:
				return uregcontent[t]
			
			else :

				print "I cannot find the content.But if u know plz write it down"
				ureg[t] = raw_input("reg name")
				uregcontent[t] = raw_input("enter the despription")
				return "thanks"


	else:
		print "I cannot find the content.But if u know plz write it down"
		regtemp = raw_input("reg name")
		ureg.append(regtemp)
		print ureg
		uregcontenttemp = raw_input("enter the despription")
		uregcontent.append(uregcontenttemp)
		return "thanks"

 

def comasplt(sply):
	b = []
	b = sply.split(',')
	print b
	g = len(b)
	#print g
	for q in range(0,g):
		text = comparereg(b[q])
		explain(text)
	
def explain(str):
	tts = gTTS(text= str, lang='en')
	tts.save("temp.mp3")
	mixer.init()
	mixer.music.load('temp.mp3')
	mixer.music.play()
	time.sleep(15)

def compareinst(insta):
	if insta =='MOV':
		explain("This moves the content of source to destination")
		#print "insta done"
		comasplt(a[i+1])
	elif insta =="int":
		explain("int 21 h . THIS IS AN interrupt INSTRUCTION WHICH CHECKS THE VALUE STORED IN A H REGISTER ")

	elif  insta == ".model":
		explain("dot model is an assmebler directive.small represents size of program. that is it contain  one data segment and one code segment")
		i = i+1

def comparereg(reg):
	if reg == 'AX':
		accumulator ='A X is the primary accumulator. it is used in input/output and most arithmetic instructions.'
		
		return accumulator
	elif reg == 'BX':
		base = 'B X is known as the base register, as it could be used in indexed addressing.'
		return base
	elif reg == 'CX':
		count = 'C X is known as the count register, as the E C X, C X registers store the loop count in iterative operations.'
		return count
	elif reg ==	'DX':
		data == 'D X is known as the data register. It is also used in input/output operations. It is also used with A X register along with D X for multiply and divide operations involving large values'

		return data
	
	else :
		print "wait"
		temp2 = userreg(reg,w)
		return temp2
		'''print "I cannot find the content.But if u know plz write it down"
		v = raw_input()
		return "Thanks"'''



print "welcome"
explain("are you new to assembly language.")
want = raw_input("1.yes   2.no \n")
if int (want) == 1:
	tts = gTTS(text="welcome to virtual lab.Enter your file name to be explainedAssembly language is a low-level programming language for a computer or other programmable device specific "
	"to a particular computer architecture in contrast to most high-level programming languages, which are generally portable" 
	"across multiple systems. Assembly language is converted into executable machine code by a utility program referred to as an"
	" assembler like NASM, MASM, etc.", lang='en')
	tts.save("temp.mp3")
	mixer.init()
	mixer.music.load('temp.mp3')
	mixer.music.play()
	time.sleep(35)


complete = raw_input("do you want to enter a single instruction or complete program thrpugh file.\n 1.single inst \n 2.complete prog \n")
if int (complete) == 2:
	filename = raw_input("enter ur file name (txt file)")
	prog = open(filename,'r')
	f = prog.read()
	a = []
	a = f.split()     #saparating whitespaces and next line
	#print a
	n = len(a)
	#print n
	for i in range(1,n-1):
		compareinst(a[i])

else:
	singleinsta = raw_input("enter the single instruction")
	a = []
	a = singleinsta.split()
	print a     #saparating whitespaces and next line
	#print a
	n = len(a)
	#print n
	for i in range(0,n-1):
		compareinst(a[i])