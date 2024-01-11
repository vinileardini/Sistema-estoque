from login import login
from menu import menu

login()

if login.signedOrNot() == True:
    
    menu()

else:
    pass
    
    
