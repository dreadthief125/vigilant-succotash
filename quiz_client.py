import socket
from tkinter import *
from threading import Thread
nickname=input("Username?")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_aderess='127.0.0.1'
port=8000
client.connect(((ip_aderess,port)))
print("Connected to the quiz game! Please enjoy your stay.")
class GUI:
  def __init__(self):
    self.Window=Tk()
    self.Window.withdraw()
    self.login=Toplevel()
    self.login.title("Login")
    self.login.resizable(width=True,height=True)
    self.pls=Label(self.login,
                  text="Please login to continue.",
                  justify=CENTER,
                  font="Helvetica 14 bold")
    self.pls.place(relheight=0.15,relx=0.2,rely=0.07)
    self.labelName= Label(self.login,
                          text="Name:",
                          font="Helvetica 12")

    self.labelName.place(relheight=0.2,
                         relx=0.1,
                         rely=0.2)
    self.entryName=Entry(self.login, font='Helvetica 14')
    self.entryName.place(relwidth=0.4,relheight=0.12,relx=0.25,rely=0.2)
    self.entryName.focus()
    self.go = Button(self.login,text="CONTINUE",font="Helvetica 14 bold",command=lambda:self.goAhead(self.entryName.get()))
    self.go.place(relx=0.4,rely=0.55)
    self.Window.mainloop()

    
       
  def goAhead(self,name):
    self.login.destroy()
    self.name=name
    rcv= Thread(target=self.recive) 
    rcv.start()



  def recive(self):
    while True:
      try:
        message=client.recv(2048).decode('utf-8')
        if message=='nickname':
          client.send(self.name.encode('utf-8'))
        else:
          pass
      except:
        print("Error occured... mb D:")
        client.close()
        break
g=GUI()


