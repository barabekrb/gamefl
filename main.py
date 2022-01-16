from field import Field

from time import sleep
from pprint import pprint
import os

def custom_clear(): 
    if os.name == 'nt':
        def inner():
          _ =  os.system("cls")
    else:
        def inner():
            _ = os.system("clear")
    return inner

clear = custom_clear()

field = Field(15, 15)

while(True):
    pprint(field.field)
    field = field.new_state()
    sleep(0.2)
    clear()
