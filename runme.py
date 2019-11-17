#%%

'''
TITLE: "Runme.py - a rather silly BPSM Assignment 2 script"
AUTHOR: B034333
GITHUB: https://github.com/B034333-2019/Assignment2
README: https://github.com/B034333-2019/Assignment2/blob/master/B034333%20Assignment%202%20PDF%20file.odt
DESCRIPTION: A progam designed to search for and download fasta format files from the NCBI's protein database depending on the 
user's whims and wishes. 
These files are then used for multiple sequence alignment, of which the top 250 most similar sequences are chosen.
A conservation sequence plot is created, and the sequences compared to the PROSITE database of protein motifs. Finally, the 
user has the option of getting sequence and protein reports.
'''

#IMPORT MODULES

import sys
from sys import exit
import subprocess
from collections import defaultdict

#GLOBAL VARIABLE INITIALISATION

#Variable for the user input protein family name
pfn_var = ""

#Variable for the user input taxonomic group
tg_var = ""

#contatenation of pfn_var AND tg_var
search_query = ""

#Dictionary for reading fasta files into python script
fasta_dict = {}

#FUNCTIONS

#Function designed to obtain user input of the protein family name to be queried.
def test_pfn():
    pfn_var = ""
    while True:
        pfn_var = input("\033[1;32mPlease enter the protein family name you are interested in. Type 'exit' to leave the program. Capitalisation is not important, but spelling is: \033[1;m")
        pfn_var = pfn_var.lower()
        if pfn_var == "" or pfn_var.isdigit() == True or len(pfn_var.strip()) == 0:
            print("\033[1;31mYou must search for something - you cannot leave it empty, or input numbers!\033[1;m")
        elif pfn_var.lower() == "exit":
            print("\033[1;32mThank you for running runme.py! Have a bioinformatically awesome day!\033[1;m")
            sys.exit()
        else:
            y_n_query = input("\033[1;32mIs '" + str(pfn_var) + "' the protein family you wish to investigate? Y/N\033[1;m")
            if y_n_query.upper() == "Y":
                print("\033[1;32mThank you. You have inputted: '" + pfn_var + "'.\033[1;m")
                return pfn_var
            elif y_n_query.upper() == "N":
                print("\033[1;32mPlease enter the protein family name you are interested in.\033[1;m")
            elif y_n_query.lower() == "exit":
                print("\033[1;32mThank you for running runme.py! Have a bioinformatically awesome day!\033[1;m")
                sys.exit()
            else:
                print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
            
#Function designed to obtain user input of the taxonomy to be queried.
def test_tg():
    tg_var = ""
    while True:
        tg_var = input("\033[1;32mPlease enter the taxonomy name you are interested in. Type 'exit' to leave the program. Capitalisation is not important, but spelling is: \033[1;m")
        tg_var = tg_var.lower()
        if tg_var == "" or tg_var.isdigit() == True or len(tg_var.strip()) == 0:
            print("\033[1;31mYou must search for something - you cannot leave it empty, or input numbers!\033[1;m")
        elif tg_var.lower() == "exit":
            print("\033[1;32mThank you for running runme.py! Have a bioinformatically awesome day!\033[1;m")
            sys.exit()
        else:
            y_n_query = input("\033[1;32mIs '" + str(tg_var) + "' the taxonomy you wish to investigate? Y/N\033[1;m")
            if y_n_query.upper() == "Y":
                print("\033[1;32mThank you. You have inputted: '" + tg_var + "'.\033[1;m")
                return tg_var
            elif y_n_query.upper() == "N":
                print("\033[1;32mPlease enter the taxonomy name you are interested in.\033[1;m")
            elif y_n_query.upper() == "exit":
                print("\033[1;32mThank you for running runme.py! Have a bioinformatically awesome day!\033[1;m")
                sys.exit()
            else:
                print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")

#search_database(args): Confirms that both protein protein family and taxonomic group are correctly input before proceeding.
def search_database(pfn_var, tg_var):
    while True:
        correct_search = input("\033[1;32mSearching for " + pfn_var.capitalize() + " in the taxonomy " + tg_var.capitalize() + " in the NCBI Protein database. Is this correct? Y/N\033[1;m")
        if correct_search.upper() == "Y":
            print("\033[1;32mThank you.\033[1;m")
            break
        if correct_search.upper() == "N":
            print("\033[1;32mPlease run script again to input your protein family name and taxonomic group of interest.\033[1;m")
            break
        else:
            print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")

#write_variables(): a function to write out the user protein family group and taxonomy to file to then use as inputs in subsequent bash scripts
def write_variables():
    subprocess.call(["touch", "variables.txt"])
    f = open("variables.txt", "w")
    f.write(search_query)
    f.close()

#esearch(): function used to query the NCBI protein database and return the number of sequences found
def esearch():
    subprocess.call("./esearchxtract.sh", shell=True)
    with open("count", "r") as outfile:
        for line in outfile:
            count = int(line)
        if count <= 10000:
            while True:
                correct_search = input("\033[1;32mYour search has returned " + str(count) + " number of sequences. Type exit to leave script. CONTINUE to download sequences? Y/N\033[1;m")
                if correct_search.upper() == "Y":
                    print("\033[1;32mThank you. Running efetch to download sequences in fasta format. Please be patient.\033[1;m")
                    return count
                if correct_search.upper() == "N":
                    print("\033[1;32mPlease run script again to do a new search.\033[1;m")
                    break
                elif correct_search.lower() == "exit":
                    print("\033[1;32mThank you for running runme.py! Have a bioinformatically awesome day!\033[1;m")
                    sys.exit()
                else:
                    print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
        else:
            print("\033[1;31mI'm sorry, your search has resulted in more than 10,000 results. Please narrow your search scope and run the program again.\033[1;m")
            exit()

#execute_esearch(): function to run esearch and pipe result into efetch to fetch relevant FASTA files into a file called query_fasta.fasta
def execute_esearch():
    x = input("\033[1;32mYou are about to download FASTA files of your protein of interest. This may take a while. CONTINUE? Y/N\033[1;m")
    while True:
        if x.upper() == "Y":
            print("\033[1;32mThank you. Running script.\033[1;m")
            subprocess.call("./esearch.sh", shell=True)
            break
        if x.upper() == "N":
             print("\033[1;32mPlease run script again to do a new search.\033[1;m")
             break
        else:
            print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
            break
        
#execute_makeblastdb(): function to run makeblastdb of the fasta files for sequence similarity alignment into a DB called seq_db
def execute_makeblastdb():
    x = input("\033[1;32mYou are about to create a database of your sequences of interest against which to BLAST. This may take a few minutes. CONTINUE? Y/N\033[1;m")
    while True:
        if x.upper() == "Y":
            print("\033[1;32mThank you. Running script.\033[1;m")
            subprocess.call("./makeblastdb.sh", shell=True)
            break
        if x.upper() == "N":
             print("\033[1;32mPlease run script again to do a new search.\033[1;m")
             break
        else:
            print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
            break

#execute_blastp(): this function runs blastp against the previously created seq_db, using a modified version of outfmt -7 that includes the fasta headers
def execute_blastp():
    x = input("\033[1;32mYou are about to BLAST your protein sequences against your local database in a multiple sequence alignment. CONTINUE? Y/N\033[1;m")
    while True:
        if x.upper() == "Y":
            print("\033[1;32mThank you. Running script.\033[1;m")
            subprocess.call("./blastp.sh", shell=True)
            break
        if x.upper() == "N":
             print("\033[1;32mPlease run script again to do a new search.\033[1;m")
             break
        else:
            print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
            break

#execute_250_seq(): Once blastp has run, we extract the fasta headers only column from the 250 most similar sequences from the blastp output file   
def execute_250_seq():
    x = input("\033[1;32mThe max. 250 most similar sequences will be extracted. CONTINUE? Y/N\033[1;m")
    while True:
        if x.upper() == "Y":
            print("\033[1;32mThank you. Running script.\033[1;m")
            subprocess.call("./250extract.sh", shell=True)
            break
        if x.upper() == "N":
             print("\033[1;32mPlease run script again to do a new search.\033[1;m")
             break
        else:
            print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
            break

#execute_pullseq(): function that uses pullseq program with the headers of the 250 most similar sequence headers to create a new fasta file.
def execute_pullseq():
    x = input("\033[1;32mThe max. 250 most similar sequences will be extracted from your fasta sequences for further analysis. CONTINUE? Y/N\033[1;m")
    while True:
        if x.upper() == "Y":
            print("\033[1;32mThank you. Running pullseq.\033[1;m")
            subprocess.call("./pullseq.sh", shell=True)
            break
        if x.upper() == "N":
             print("\033[1;32mPlease run script again to do a new search.\033[1;m")
             break
        else:
            print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
            break
        
#execute_clustalo(): function that runs clustalo with input file containing the 250 most similar sequences in fasta format
def execute_clustalo():
    x = input("\033[1;32mYou are about to use clustalo to create a sequence clustering using your max. 250 most similar sequences. CONTINUE? Y/N\033[1;m")
    while True:
        if x.upper() == "Y":
            print("\033[1;32mThank you. Running script.\033[1;m")
            subprocess.call("./clustalo.sh", shell=True)
            break
        if x.upper() == "N":
             print("\033[1;32mPlease run script again to do a new search.\033[1;m")
             break
        else:
            print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
            break
        
#execute_plotcon(): function that runs the EMBOSS plotcon program to plot conservation of sequence alignment of 250 most similar sequences.
def execute_plotcon():
    x = input("\033[1;32mYou are about to use PLOTCON to create a sequence conservation plot of the max. 250 sequences. CONTINUE? Y/N\033[1;m")
    while True:
        if x.upper() == "Y":
            print("\033[1;32mThank you. Running script.\033[1;m")
            subprocess.call("./plotcon.sh", shell=True)
            break
        if x.upper() == "N":
             print("\033[1;32mPlease run script again to do a new search.\033[1;m")
             break
        else:
            print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
            break

#create dictionary of fasta FILE to send into patmatmotifs
def mofit_database_dict():
    fasta = defaultdict(str)
    with open("twofifty_final_fastas") as file1:
        for line in file1:
            if line[0] == '>':
                key = line.strip('\n')
            else:
                fasta[key] += line.strip('\n')
    return fasta
            
#testing by temporarily writing to a file
def patmatmotifs_loop():
    while True:
        x = input("\033[1;32mYou are about to compare your max. 250 most similar sequences against PROSITE protein motifs. CONTINUE? Y/N\033[1;m")
        if x.upper() == "Y":
            subprocess.call(["touch", "prositereport"])
            subprocess.call(["touch", "PROSITEdb"])
            for key, value in fasta_dict.items():
                subprocess.call(["touch", "temp.fasta"])
                with open("temp.fasta", "w") as f:
                    header = str(key) + "\n"
                    sequence = str(value) 
                    sequence = sequence + "\n"
                    f.write(header)
                    f.write(sequence)
                    f.close()
                    cmd = "patmatmotifs -sequence temp.fasta -sprotein1 True -outfile prositereport -full True"
                    subprocess.call(cmd, shell=True)
                    cmd2 = "cat prositereport >> PROSITEdb"
                    subprocess.call(cmd2, shell=True)
            subprocess.call(["echo", "-e", "Your final motif report is contained in the file PROSITEdb."])
            break
        if x.upper() == "N":
             print("\033[1;32mPlease run script again to do a new search.\033[1;m")
             break
        else:
             print("\033[1;31mPlease input Y ('Yes') or N ('No').\033[1;m")
               
        
def wildcard():
    x = ""
    while True:
        x = input("\033[1;32mYou can either run your 250 most similar sequences through an infoalign analysis to show information about all 250 sequences [Enter: 1], and/or run a pepstats analysis receive a report for protein statistics [Enter: 2]. To run both, [Enter: 3]. To exit the program, type 'exit'.\033[1;m")
        if x == "1":
            subprocess.call(["echo", "-e", "Running infoalign..."])
            subprocess.call("./infoalign.sh", shell=True)
            subprocess.call(["echo", "-e", "Your info analysis is available in the file infoalign.report."])
            break
        if x == "2":
            subprocess.call(["echo", "-e", "Running pepstats...)"])
            subprocess.call("./pepstats.sh", shell=True)
            subprocess.call(["echo", "-e", "Your protein statistics are available in the file stats.pepstats."])
            break
        if x == "3":
             subprocess.call(["echo", "-e", "Running infoalign and protein statistics..."])
             subprocess.call("./infoalign.sh", shell=True)
             subprocess.call("./pepstats.sh", shell=True)
             subprocess.call(["echo", "-e", "Your info analysis is available in the file infoalign.report."])
             subprocess.call(["echo", "-e", "Your protein statistics are available in the file stats.pepstats."])
             break
        if x.lower() == "exit":
            print("\033[1;32mThank you for running runme.py! Have a bioinformatically awesome day!\033[1;m")
            sys.exit()
        else:
            print("\033[1;31mPlease input 1 for infoalign, 2 for protein statistics, 3 for both, or type exit to quit program.\033[1;m")
            

def cleanup():
    subprocess.call(["echo", "-e", "Cleaning up files..."])
    subprocess.call("./cleanup.sh", shell=True)
    print("\033[1;32mAll clean! Thank you for running runme.py - have a bioinformatically awesome day!\033[1;m")

#SCRIPT / FUNCTION CALLS
            
#Retrieve user input
pfn_var = test_pfn()
tg_var = test_tg()
final_search = search_database(pfn_var, tg_var)

#Write variables to local folder
search_query = pfn_var + " AND " + tg_var
write_variables()

#Further analysis
esearch()
execute_esearch()
execute_makeblastdb()
execute_blastp()
execute_250_seq()
execute_pullseq()
execute_clustalo()
execute_plotcon()

#reading fasta file into Python script
fasta_dict = mofit_database_dict()

#Further analysis
patmatmotifs_loop()
wildcard()
cleanup()

print("\033[1;32mHere endeth the script. Thank you for running my silly script.\033[1;m")