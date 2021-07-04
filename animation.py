import os
import time

#using space and/or empty line to change location of your figure
def figure(n):
    line0=n*'\n'
    line1 =2*n*' ' + '88888888888\n'
    line2 =2*n*' ' + '88888888888\n'
    line3 =2*n*' ' + '888     888\n'
    line4 =2*n*' ' + '888     888\n'
    line5 =2*n*' ' + '888     888\n'
    line6 =2*n*' ' + '888     888\n'
    line7 =2*n*' ' + '88888888888\n'
    line8 =2*n*' ' + '88888888888\n'
    line9 =2*n*' ' + '888     888\n'
    line10=2*n*' ' + '888     888\n'
    line11=2*n*' ' + '888     888\n'
    line12=2*n*' ' + '888     888\n'
    line13=2*n*' ' + '88888888888\n'
    line14=2*n*' ' + '88888888888\n'
    f=line0+line1+line2+line3+line4+line5+line6+line7+line8+line9+line10+line11+line12+line13+line14
    print(f)
      

#this functions as clear the console screen (remove anything shown in curren screen)
clear = lambda: os.system('cls')

#clear screen before print image
clear()

#run the figure function 1000 times, each time, figure funtion will print images in different location and then clear screen before we run next figure function.
for i in range(0,1000):

    #keep n between 0-14 
    n=i%15

    #pass n to figure function and use n to control figure location
    figure(n+3)

    #the printing of figure will keep on screen for 0.5 second, and then the clear function will clear printing
    #you can set time to control the speed of animation.
    time.sleep(0.5)

    #clear screen before we start next loop    
    clear()
    
