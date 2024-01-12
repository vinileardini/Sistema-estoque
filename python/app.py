from login import login
from menu import menu


loginArea = login()

isSigned = loginArea.signedOrNot()

if isSigned == True:
    
    menu()

else:
    pass
    
    
 