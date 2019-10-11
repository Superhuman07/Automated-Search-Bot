# Automated-Search-Bot
Search from bing/google/yahoo multiple times by just clicking the run button.

<b> First download the python language for windows OS</b>

Download get-pip.py to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run python get-pip.py. This will install pip.
Verify a successful installation by opening a command prompt window and navigating to your Python installation's script directory (default is C:\Python27\Scripts). Type pip freeze from this location to launch the Python interpreter.
pip freeze displays the version number of all modules installed in your Python non-standard library; On a fresh install, pip freeze probably won't have much info to show but we're more interested in any errors that might pop up here than the actual content
Microsoft Windows [Version 6.2.9200]
(c) 2012 Microsoft Corporation. All rights reserved.

C:\Users\Username>cd c:\Python27\Scripts

c:\Python27\Scripts>pip freeze
antiorm==1.1.1
enum34==1.0
requests==2.3.0
virtualenv==1.11.6
It would be nice to be able to run Pip from any location without having to constantly reference the full installation path name. If you followed the Python installation instructions above, then you've already got the pip install location (default = C:\Python27\Scripts) in your Windows' PATH ENVIRONMENT VARIABLE. If you did not follow those steps, refer to them above now.
Verify a successful environment variable update by opening a new command prompt window (important!) and typing pip freeze from any location
Microsoft Windows [Version 6.2.9200]
(c) 2012 Microsoft Corporation. All rights reserved.

C:\Users\Username>pip freeze
antiorm==1.1.1
enum34==1.0
requests==2.3.0
virtualenv==1.11.6

<H2> HOW TO RUN </h2>

1. Press control+R and type cmd
2. Change the dir to the bot dir using <code> cd yourdirname </code> 
3. Type <code> python search.py </code>

##Help documentation
On Windows,

To run a python module without typing "python",

--> Right click any python(*.py) file

--> Set the open with property to "python.exe"

--> Check the "always use this program for this file type"

--> Append the path of python.exe to variable environment e.g. append C:\Python27 to PATH environment variable.

To Run a python module without typing ".py" extension

--> Edit PATHEXT system variable and append ".PY" extension to the list.
