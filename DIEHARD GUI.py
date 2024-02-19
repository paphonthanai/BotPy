# Die HardGUI.py
from tkinter import *

GUI = Tk()
GUI.geometry('500x700')
GUI.state('zoom')
GUI.title('โปรแกรม Dashbord DieHard 4.0')

#def Fullscreen(event):
#	GUI.attributes('-fullscreen',True)

#def ExitFullscreen(event):
#	GUI.attributes('-fullscreen',False) 


#GUI.bind('<F11>',Fullscreen)
#GUI.bind('<F12>',ExitFullscreen)


# COLOR
bg = '#626770'
fg = '#ff0000'
GUI.configure(background = bg)



#FUllscreen
GUI.attributes('-fullscreen',False)
GUI.bind('<F10>', lambda event : GUI.attributes('-fullscreen', not GUI.attributes('-fullscreen')))

#FONT
f1=('Sprite coder', 20 , 'bold')
f2=('Sprite coder', 15 , 'bold')
f3=('Sprite coder', 10 , 'bold')
f4=('impact', 20 , 'bold')

# CANVAS
cw = '1980'
ch = '1020'
canvas = Canvas(GUI,width=cw, height=ch ,background=bg, bd=0, relief='ridge',highlightthickness=0) #bd=border 
canvas.place(x=0,y=0)

def MyFrame(x,y,width=300,height=400):
	frame1 = canvas.create_rectangle(0,0,width,height,fill=bg, outline=fg, width=3)
	canvas.move(frame1,x,y)

def FixedLabel(text='THIS IS A TEXT',x=50, y=50, font=f1, color=fg):
	L1 = Label(GUI, text=text, font=font , bg=bg , fg=color, justify=LEFT)
	L1.place(x=x,y=y)

MyFrame(20,20)
FixedLabel('MY COIN',30,100)
FixedLabel('โปรแกรมคำนวน Bit Coin',50,200,font=('Angsana New',30,'bold'),color='red')

# IoT Frame
MyFrame(500,20)
FixedLabel('IoT-Device 1',510,25,font=f2)
FixedLabel('Temp(C): 30\n HUMID (%) : 55\n STATUS : OK',505,50,font=f3)

# IoT Frame
MyFrame(1000,20)
FixedLabel('IoT-Device 1',1020,25,font=f2)
FixedLabel('Temp(C): 30\n HUMID (%) : 55\n STATUS : OK',1005,50,font=f3)

#CHECK STOCK
MyFrame(500,20)
FixedLabel('THAI STOCK',510,25,font=f2)


v_stockname = StringVar() #StringVar ตัวแปรสำหรับใช้กับ GUI


E1 = Entry(GUI, textvariable=v_stockname, font=f4,bg=bg,fg=fg)
E1.configure(insertbackground=fg) #Cursor color
E1.configure(highlightthickness=2,highlightbackground=fg,highlightcolor=fg)
E1.place(x=505,y=100)

v_result = StringVar()
v_result.set('My STOCK : 50 BATH')

LResult = Label(GUI, textvariable=v_result, font=f1 , bg=bg , fg=fg, justify=LEFT)
LResult.place(x=505,y=150)


from thaistock import SET
#['SCB ', '127.00', '-3.50', '-2.68%', '27/11/2021 03:19:54']
def CheckStockPrice(event):
	try:
		stockname = v_stockname.get()
		print(stockname)
		result = stockname
		text = 'STOCK: {}\nPRICE : {}'.format(result[0],result[1])
		v_result.set(text)
	except:
		v_result.set('NOT FOUND')
E1.bind('<Return>',CheckStockPrice)

GUI.mainloop()