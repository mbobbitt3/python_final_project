1. first install unzip command from apt if you don't have it already using "sudo apt install unzip" and then run install.sh 
then install the version of JDK at this link for linux x64 https://adoptium.net/temurin/releases/
2. follow instructions for setting up JDK with ghidra here. https://github.com/NationalSecurityAgency/ghidra/tree/master
3. then run run_scripts.sh 
4. after run_scripts.sh is run for the first time, unless you want to generate another cfg just run the
graph_generation.py script using python from the command line
5. use pip to isntall networkx, matplotlib, and seaborn 
NOTE: MAKE SURE SCRIPTS ARE RAN FROM THE ROOT PROOJECT DIRECTORY
NOTE: if you can't get ghidra to work, the output is already provided in the project you can just run
python scripts/graph_generation.py from the project directory and it will work.
