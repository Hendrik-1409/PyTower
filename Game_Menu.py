from tkinter import *
import Game

class Nochmal:
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Menu Towerdefense')
        self.n=1

        self.l1 = Label(self.root, width=76, height=20, fg='black', bg='white', font=('Courier', 16, 'bold'), text ='''Spielregeln:
Towerdefense ist ein Spiel in dem alle 2 Sekunden ein Gegner sich auf den
Weg macht um dein  Schloss anzugreifen, positioniere deine Türme um den
Weg zu Beschützen und die Gegner zu Töten.''')
        self.l1.pack()

        self.b1 = Button(self.root, width=60, height=4, fg='white', bg='green', font=('Courier', 20, 'bold'), text = 'Programm starten', command = self.c1)
        self.b1.pack()

        self.b2 = Button(self.root, width=60, height=4, fg='white', bg='red', font=('Courier', 20, 'bold'), text = 'Programm beenden', command = self.c2)
        self.b2.pack()


    def c1(self):
        self.root.destroy()
        Game.main()

    def c2(self):
        self.root.destroy()

def main():
    Nochmal()
    mainloop()

if __name__ == "__main__":
    main()