from pypresence import Presence
import questionary
from time import sleep

client_id = questionary.text("Enter the client id for your discord application:").ask()
RPC = Presence(client_id)
RPC.connect()
state = questionary.text("Enter the first line of your custom rich presence:").ask()
details = questionary.text("Enter the rest of your custom rich presence:").ask()
large_image = questionary.text("Enter your image key:").ask()
RPC.update(state=state, details=details, large_image=large_image)
while True:
    sleep(15)