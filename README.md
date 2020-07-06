# KetoGator

## Current dependencies 
### PyQt5: 
pip install PyQt5
### Pandas:
pip install pandas
### Excel for Pandas:
pip install xlrd
### For writing Excel sheets
pip install xlwt
### For connecting to MySQL databases
pip install mysql-connector-python
### For Excel sheet editing:
pip install openpyxl
### For graphical representation
pip install matplotlib

## Possible Installs and Configurations
### Sudo Installs for the QC library to work with OpenGL
I set up by Ubuntu WSL the same way as instructed at the beginning of the class. However, after packaging the program, there were some issues interally with the Linux system.
There were errors that were given in relation to not being able to find "xcb" and not finding some libxcb.so files.
I had to do the following to fix this error:

sudo apt-get install libxcb-icccm4-dev libxcb-image0-dev libxcb-shm0-dev libxcb-keysyms1-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-xfixes0-dev libxcb-xkb-dev libxkbcommon-x11-dev libxkbcommon-dev libxcb-xinerama0-dev

This will have to be installed before the program can be ran, *IF* a xcb error is produced.

### VcXsrv
Again, VcXsrv was set up just the way as instructed in class. However, I was getting the following libGL (library for OpenGL) errors:
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast

I found that it was a configuration with the server.
I did the following options for setting up the VcXsrv server and it fixed the OpenGL errors:
    1. Choose Multiple Windows
    2. Set Display to the value 0
    3. Choose the Start No Client option
    4. Disable the Native OpenGL option.

In class, our config files keep the display value to -1 and the Native OpenGL option is Enabled. When I changed these two options, the libGL errors went away. These errors could cause problems in the display.

This will have to be changed before running the program, or it could possible cause errors with the UI.

## MySQL Configuration File (LATER)
The MySQL connector looks for a configuration file called mysql.conf. It should specify host, database, user, password, and port information for the target database.

The package should install all dependencies.

Our project specifications have changed by the "customer" of this project just recently (6/27). This config will be added at another time.

## GitHub Link
https://github.com/KylerKatz/KetoGator/tree/dain_kg_package4

## PyPl
pip install KetoGator==1.0.11

## Executable line
kgstart

## Username and Password
Username: user
Password: password