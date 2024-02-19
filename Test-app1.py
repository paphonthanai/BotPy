import tkinter as tk
def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='non')
        return

    output = ' '
    for i in range(1, 25):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)

window = tk.Tk()
window.title('Jinnie with smoke')
window.minsize(width=400, height= 400)

title_label = tk.Label(master=window, text='สูตรคุณ ฯลฯ')
title_label.pack()

number_input = tk.Entry(master=window)
number_input.pack()

go_button = tk.Button(master=window, text='ได้แก่',command=show_output)
go_button.pack()
command=show_output

output_label = tk.Label(master=window,text=number_input.pack())
output_label.pack()
