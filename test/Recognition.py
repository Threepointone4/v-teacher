import string
import pyttsx
from gtts import gTTS
import os
from pygame import mixer 
import time# Load the required library

#from translation import baidu, google, youdao, iciba

text = raw_input("enter the instruction")
a = []
#registers = "AX BX CX DX AL CL BL DL AH BH CH SI DI"

a = text.split()
#r =registers.split()

print a
#print r
b = len(a) 
#print(google('hello word',dst ='hi'))

for i in range(0,b):
	if 'MOV' == a[i]:
		'''engine = pyttsx.init()
		engine.say('it moves the content of'+a[1]+'to'+a[2])
		engine.runAndWait()'''
	  	tts = gTTS(text="it moves the content of A X " +'register' + 'to' + ' B  X' +'register', lang='hi')
		tts.save("MOV.mp3")
		mixer.init()
		mixer.music.load('MOV.mp3')
		mixer.music.play()
		time.sleep(10)
		n = input("DO U WANT TO KNOW MORE ABOUT INSTR 1 to yes ")
		if n == 1:
			for k in range(i+1,i+3):

				#j=i+1
				if a[k] == 'AX':
					tts = gTTS(text='A X is the primary accumulator; it is used in input/output and most arithmetic instructions. For example, in multiplication operation, one operand is stored in E A X or A X or A L register according to the size of the operand.', lang='hi')
					tts.save("AX.mp3")
					mixer.init()
					mixer.music.load('AX.mp3')
					mixer.music.play()				
					print 'success1'
					time.sleep(15)
				#i = i+1
				
				elif  a[k] == 'BX':

					tts = gTTS(text='B X is the primary accumulator; it is used in input/output and most arithmetic instructions. For example, in multiplication operation, one operand is stored in E B X or B X or A L register according to the size of the operand.', lang='hi')
					tts.save("BX.mp3")
					mixer.init()
					mixer.music.load('BX.mp3')
					mixer.music.play()
					#pygame.mixer.music.get_pos('BX.mp3')
					print 'success2'
					time.sleep(15)

			#i=i+1	




	    #continue


	elif "int" ==a[i]:
		tts = gTTS(text='it gives the permission to acess the register', lang='hi')
		tts.save("INT.mp3")
		mixer.init()
		mixer.music.load('INT.mp3')
		mixer.music.play()
		i=i+1
		time.sleep(15)
