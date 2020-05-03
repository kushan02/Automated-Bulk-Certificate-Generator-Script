# Automated-Certificate-Generator-Script
This python script automates the process of generating multiple certificates for a given list of people from a template image file. To explain it in a better way, say you need to provide digital certificates for any purpose, so you create a template for a certificate, this script will take care of the generation of certificate for different people using txt file as an input of names

#### Project Idea (Origin):
I am a core-committee member of the University Coding Club, and hence we organize many competitons, workshops or events where we need to provide a certificate of participation to the users. To make this process automated, I decided to write a small helper script to provide me with ready to send, automatically generated certificates. 

#### Requirements:
1. Python 3+
2. OpenCV (you can google how to install opencv for python environment)
3. A template certificate image

#### Usage:
Simply edit the input and output file path for the csv input file and template image and the generated certificates file and run it.

Format of input csv file:
The input file must contain a comma seperated list of the ranks, their user handles and the names of people you want to provide certificate to.

eg. Rank  User_handle Name  
    1     jon_doe     John Doe
    2     smith       Smith
    
