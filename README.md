# Machine-Learning-Based-IDS
Using ML model to detect DoS attacks on a host system

BRIEF DESCRIPTION OF PROJECT
----------------------------------------------------------------------------------
Our project is based on SVM model to detect whether the connection(pair of IPs talking with each other) is attack or not.
We used a python packet sniffer to sniff the packets for cycles of two seconds and aggregated this information based on Source IP and Destionation IP pairs.
Converted these data into csv and combined those csv to create our own dataset for both attack and normal packets
Using the dataset we created, trained and SVM model to detect that said onnection was DoS attack or not.
The SVM model is saved into pickle so it can be used later without going through the hassle to create the model everytime we need to run program.
Same sniffer is used to create a DF(dataframe) that we feed SVM model for the analysis of packets.
The DF is sent from sniffer.py to MLIDS.py and the results of prediction is displayed on the GUI in tabular format


SYSTEM REQUIREMENT
----------------------------------------------------------------------------------
The project is completely based on Python Language (python 3.6 or above can run this) and run on LINUX SYSTEM ONLY.

Along with Python you need to make sure you have following packages install
sklearn
pandas
pickle

HOW TO RUN THE PROGRAM
----------------------------------------------------------------------------------
Create two VMs both running linux distro(preferably kali)
One VM to depict "attacker" Other to depict "Victim"
Download and run our program on "Victim" 
Run some DoS attacks on "Victim" from "Attacker"
When the program detects an attack it will hightlight it in red.

Run the .sh file or Run the MLIDS.py file to start the program
It will display the GUI. 
Click "Start"  Button to start sniffing and predicting packets

OUTPUT will be displayed on the GUI in Tabular format

Configuring the Sniffer(IMPORTANT PART) DO THIS BEFORE THE RUNNING THE PROGRAM
----------------------------------------------------------------------------------
Change the IP address to you Victim's IP (in which you download the program) inside the "sniffer.py" file at line 36


FOR MORE INFO GO THROUGH DOCUMENTATION ""

Contributers Names:
Ashutosh Bist https://github.com/AshutoshBist
Hrithik Gaikwad https://github.com/Hr09
Prof. Yash Shah https://github.com/yash1234shah

