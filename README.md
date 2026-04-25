FILE INTEGRITY CHECKER

*Company Name* : Codtech IT Solutions Private Limited
*Name* : Sayyad Arban Ali
*Intern Id* : CTIS5711
*Domain* : Cyber Security & Ethical Hacking
*Duration* : 16 Weeks
*Mentor* : Neela Santosh


# Simple File Integrity Monitor (FIM)

This is a Python program that checks if files have been changed by looking at special codes called cryptographic hash values.

## Project Overview

This program was made to show how to keep files from being changed on purpose or by accident. It does this by making a kind of fingerprint of the file and checking it all the time.

## Features

- It uses a way of making these digital fingerprints called SHA-256 Hashing. This means it can tell if even a small thing has been changed in the file like a space or a comma.

- It checks the file all the time so it can tell you away if something has been changed.

- It is good at using computer memory so it can check files without using too much memory.

- It has a way of working with the user, where you can tell it which file to check and see when things have been changed.

## How It Works

1. First the program makes a code, for the file you want to check.

2. Then it keeps checking the file and making new codes to compare with the one.

3. If the codes are not the same the program tells you. Updates the code so it can keep checking.

##. Usage

1. You need to have Python 3.x on your computer.

2. You need to get a file called monitor.py.

3. Open the terminal. Command prompt and type:

```bash

python monitor.py

```

4. Tell the program which file you want to check by typing the path to the file like C:\Documents\test.txt.

## Security Use Cases

- You can use this program to check files that should not be changed.

- It can help you find out if someone has changed log files without permission.

- It is a way to learn about keeping files safe which is called File Integrity Monitoring.

#output
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/ada23a4c-3eca-4677-8301-dd0c2bf5bee7" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/ad1698a7-e660-4573-ad6b-87378bd0fc1c" />
