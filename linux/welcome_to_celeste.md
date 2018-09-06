# Welcome to celeste

## SSH

You can connect remotely on `celeste` via `ssh` with your `login` and `password`. 
If you have an **ssh client** (by default on most linux distributions and Mac OSX) you have to launch a shell emulator:

* MAC: Applications → Utilities → Terminal (https://superuser.com/questions/178735/how-do-you-get-a-shell-on-a-mac)
* Linux: find the application named `Terminal`. On Ubuntu type CTRL+ALT+T.

Once in the terminal you can type the following command (replace `login` with you real login):
```
ssh -X -p 443 login@celeste.phy.ulaval.ca
```
You wil be prompt for your password and finally see the command line:
```
login@celeste:~$
```

## First things to do 

There are a few things to set up your session. **You won't have to do it again.**

### Change your default password

Type the command 
```
passwd
```
and enter your new password.

### Activate the data analysis library ORCS

Type the command 
```
orb-change-mode stable
```
You won't have to do it again unless asked by the administrator.

### Find help on how to use a linux shell

If you're new to it and want to google some help, know that `shell` , `bash`, `command line` are more or less the same stuff.

You could find some help by looking at :
* https://ryanstutorials.net/linuxtutorial/
