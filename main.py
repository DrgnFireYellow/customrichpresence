from pypresence import Presence
import tkinter
from time import sleep

window = tkinter.Tk()
window.title("Custom Rich Presence")
tkinter.Label(text="Client ID").pack()
client_id = tkinter.Entry()
client_id.pack()
tkinter.Label(text="Custom Rich Presence").pack()
details = tkinter.Entry()
details.pack()
tkinter.Label(text="Your image key").pack()
large_image = tkinter.Entry()
large_image.pack()

def start_rpc():
    RPC = Presence(client_id.get())
    RPC.connect()
    RPC.update(details=details.get(), large_image=large_image.get())
    tkinter.Label(text="Activated!", fg="green").pack()
    tkinter.Label(text="Close window to stop rich presence", fg="red").pack()

start_button = tkinter.Button(text="Activate", command=start_rpc)
start_button.pack()
tkinter.mainloop()
