# Python Scripting Help for Vision
Vision 5.0 External Signalling Support Module for Python. It can be used to script the Ferroelectric Tester using Python through the Vision Suite.

Below the tutorial has been outlined.
## Step 1 : Configure the program in the Editor Aide
![[image(1).png]]
The Task Definition can be configured in the Editor Aide as shown above.

After selecting and correctly sequencing the tasks, select the "Move Editor List to Editor" Button to configure further.

For the given configuration, the following pop-ups will show in which you are to rename if required and configure the tasks. 
![[image(2).png]]
Configuring the "File Start/Abort"
![[image(4).png]]
Configuring the "Signal File - Write". Here you are required to specify the path and configure the options for "Wait for File Deletion" or "Timed Wait" as necessary. For the tutorial, configure as shown.

After completing this the Editor will look like this. 
![[unnamed2.png]]
## Step 2 : Moving from Editor to Current Test Defintion
This can be moved to the Current Test Definition by Right Clicking and will finally appear as shown :
![[unnamed.png]]

## Step 3: Configuring the script in python

For the python side, the example.py script can be alongside the main module. Or it can be configured as shown in the example.py script.

Et fini.