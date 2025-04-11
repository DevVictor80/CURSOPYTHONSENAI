import tkinter as tk 

def fnAdição():
    x= float(entryNumero1.get())
    y= float(entryNumero2.get())
    resultado = x + y
    lblResultado.config(text=f'A soma é {resultado}:')

def fnSubtração():
    x= float(entryNumero1.get())
    y= float(entryNumero2.get())
    resultado = x - y
    lblResultado.config(text=f'A subtração é {resultado}:')


janela = tk.Tk() #desenha uma janela 
janela.title("Wincalc - a super calculadora")
janela.geometry('800x800')#tamanho da janela 

lblTitulo = tk.Label(janela,
                     text='Wincalc',
                     font=('Old English Text MT',32),
                     fg='white' ,
                     bg='gray',
                     width=800)
lblTitulo.pack(padx=5,pady=5)


lblNumero1 = tk.Label( janela,
                      text='Digite um numero',
                      font=('Calibri',30))
lblNumero1.pack(padx=5,pady=5)

entryNumero1 = tk.Entry(janela, 
                        width=800,
                        font=('Calibri',32))
entryNumero1.pack(padx=5,pady=5)
lblNumero2 = tk.Label( janela,
                      text='Digite um numero',
                      font=('Calibri',30))
lblNumero2 = tk.Label( janela,
                      text='Digite um numero',
                      font=('Calibri',30))
lblNumero2.pack(padx=5,pady=5)

entryNumero2 = tk.Entry(janela, 
                        width=800,
                        font=('Calibri',32))
entryNumero2.pack(padx=5,pady=5)
lblNumero2 = tk.Label( janela,
                      text='Digite um numero',
                      font=('Calibri',30))

btnkAdição=tk.Button(janela,
                      text='Adição',
                      font=('Calibri',32),
                      #width=800,
                      command=fnAdição)
btnkAdição.pack(padx=5,pady=5)
btnmultiplicação=tk.Button(janela,
                      text='Multiplicação',
                      font=('Calibri',32),
                      #width=800,
                      command=None)
btnmultiplicação.pack(padx=5,pady=5)
btnsubitração=tk.Button(janela,
                      text='Subtração',
                      font=('Calibri',32),
                      #width=800,
                      command=fnSubtração)
btnsubitração.pack(padx=5,pady=5)
btnDivisão=tk.Button(janela,
                      text='Divisão',
                      font=('Calibri',32),
                      #width=800,
                      command=None)
btnDivisão.pack(padx=5,pady=5)

lblResultado=tk.Label(janela,text='0.0',font=('calibri',22))
lblResultado.pack(padx=5,pady=5)


janela.mainloop() #mantem o programa rodando, precisa ser o ultimo cod