#importing the windows client app

import win32com.client
x = win32com.client.Dispatch("AppRobotic.API")
# importing the webbrowser library
import webbrowser

# specify URL
url = "https://www.google.com"

# open with default browser maybe windows explorer but the user can change the default web browser to chrome
webbrowser.open_new(url) 

#checking the webbrowser if they are installed or not 
# open with Safari, if installed
webbrowser.get('safari').open_new(url) 
# open with Firefox, if installed
webbrowser.get('firefox').open_new_tab(url) 
# open with Chrome, if installed
webbrowser.get(using='google-chrome').open_new(url)

# wait a bit for page to open for 3 seconds
x.Wait(3000)
# use UI Item Explorer to find the X,Y coordinates of Search box
x.MoveCursor(438, 435)
# click inside Search box
x.MouseLeftClick

x.Type("AppRobotic")
x.Type("{ENTER THE REQUIRED STRING YOU WANT TO SEARCH}")
