# Welcome to celeste

## SSH

You can connect remotely on `celeste` via `ssh` with your `login` and `password`. 
If you have an **ssh client** (by default on most linux distributions and Mac OSX) you have to launch a shell emulator:

* MAC: Applications → Utilities → Terminal (https://superuser.com/questions/178735/how-do-you-get-a-shell-on-a-mac)
* Linux: find the application named `Terminal`. On Ubuntu type CTRL+ALT+T.

Once in the terminal you can type the following command (replace `login` with you real login):
```bash
ssh -X -p 443 login@celeste.phy.ulaval.ca
```
You wil be prompt for your password and finally see the command line:
```bash
login@celeste:~$
```

## First things to do 

There are a few things to set up your session. **You won't have to do it again.**

### Change your default password

Type the command 
```bash
passwd
```
and enter your new password.

### Activate the data analysis library ORCS

Type the command 
```bash
orb-change-mode stable
```
You won't have to do it again unless asked by the administrator.

### Find help on how to use a linux shell

If you're new to it and want to google some help, know that `shell` , `bash`, `command line` are more or less the same stuff.

You could find some help by looking at :
* https://ryanstutorials.net/linuxtutorial/

## Use Jupyter Lab on celeste

You can find some help on Jupyter and Jupyter Lab here: 
* https://jupyter.org/
* https://jupyterlab.readthedocs.io/en/latest/

To run a jupter server on celeste you must do the following:

### on celeste
In the shell
```bash
jupyter notebook --generate-config
```
Then you must generate a password hash (this password must be difficult to guess for security reasons). In the shell run the following command:
```bash
python -c 'from notebook.auth import passwd; print passwd()'
```
It will output something like
```
sha1:c37902605916:825a4062cc12b3e...
```

Then open the file `.jupyter/jupyter_notebook_config.py` and uncomment/change the following lines:
```python:jupyter/jupyter_notebook_config.py
c.NotebookApp.open_browser = False
c.NotebookApp.port = 9543 # here you must choose a port randomly between 9000 and 9900, if you have the same port as another user you may experience some problems (communicate with the administrator).
c.NotebookApp.password = u'sha1:e3505988559c:73931....' # put here the hashed password you generated
```

You can now run jupyter with
```bash
screen jupyter lab
```
and get out of here with `CTRL+A, CTRL+D.`

**Those steps should not be done again. If celeste is rebooted you will have to run the `screen jupyter lab` again.**

### On your local machine

You must first connect the output port of celeste to a port on your local machine. To do that just run in a shell:

```bash
ssh -p 443 -L 8099:localhost:9543 login@celeste.phy.ulaval.ca
```

Don't exit the shell.

You can finally open http://localhost:8099 in a web browser.

Remember that **these two last steps will have to be repeated each time you reboot your local machine.**


