# Visual-Ploxys
Graphical interface made for use of ploxys

#What is it?

It is a GUI made for you to watch the ploxys (see here the original project: https://github.com/victor-cortez/ploxys), with this GUI you can easily choose the configurations,sit down and watch the ploxys living. And after the simulation you can get the entire data saved in your computer automatically.

#How to Install

If you have Windows or a windows emulator like wine, you can simply download the .exe and enjoy.

If you want only to use the program and cant use the .exe, you just need to download from the repository the files "ploxys.pi" and "ploxys_ui.py" and install PyQt5 and SIP if you dont already have installed the packages.

Links to install:
http://pyqt.sourceforge.net/Docs/PyQt5/installation.html#downloading-pyqt5
https://riverbankcomputing.com/software/pyqt/download5
https://riverbankcomputing.com/software/sip/download
http://pyqt.sourceforge.net/Docs/sip4/

If you want the entire source make sure you have the PyQt5 and the SIP installed.


The backup.py is just a backup of the code, you can ignore it | The image.jpg is the main image wich is expandable, you dont need to download | the ploxys.exe is a single-file executable made with Pyinstaller | The ploxys.py is the main script, wich you will run to use the program | The ploxys.ui is the UI file made in QT Designer | ploxys_ui.py is the essence of the program, it contains the UI programming and the entire ploxys system. | The run.bat is a bash script i made to easily convert the QT Designer file (.ui) to the python script (.py), be aware that it overwrites the entire file, so be careful

#How to use it

Set the number in each number selector, and be sure the minimal lifespan is lower than the maximal lifespan, otherwise the simulation will not start. The number of ploxys alive, the current round (it starts from 0 so if you choose 200 rounds it will end in the round 199) and the framerate in fps are shown in the right-upper side, as LED displays. When everything is okay, choose in wich folder the program will save the data from the simulation, and press start (do not try to overwrite or write into an existing folder). After this you can sit down and enjoy the animation.

Previous animation i done right after finishing the ploxys with the primitive method of saving frame-by-frame and putting them into a stop-motion animation: https://www.youtube.com/watch?v=Gnu9ugKHomQ
