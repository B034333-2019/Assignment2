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

#GLOBAL VARIABLES

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
        pfn_var = input("Please enter the protein family name you are interested in. Type 'exit' to leave the program. Capitalisation is not important, but spelling is: ")
        pfn_var = pfn_var.lower()
        if pfn_var == "" or pfn_var.isdigit() == True or len(pfn_var.strip()) == 0:
            print("You must search for something - you cannot leave it empty, or input numbers!")
        elif pfn_var.lower() == "exit":
            print("Thank you for running runme.py! Have a bioinformatically awesome day!")
            sys.exit()
        else:
            y_n_query = input("Is '" + str(pfn_var) + "' the protein family you wish to investigate? Y/N")
            if y_n_query.upper() == "Y":
                print("Thank you. You have inputted: '" + pfn_var + "'.")
                return pfn_var
            elif y_n_query.upper() == "N":
                print("Please enter the protein family name you are interested in.")
            elif y_n_query.lower() == "exit":
                print("Thank you for running runme.py! Have a bioinformatically awesome day!")
                sys.exit()
            else:
                print("Please input Y ('Yes') or N ('No').")
            
#Function designed to obtain user input of the taxonomy to be queried.
def test_tg():
    tg_var = ""
    while True:
        tg_var = input("Please enter the taxonomy name you are interested in. Type 'exit' to leave the program. Capitalisation is not important, but spelling is: ")
        tg_var = tg_var.lower()
        if tg_var == "" or tg_var.isdigit() == True or len(tg_var.strip()) == 0:
            print("You must search for something - you cannot leave it empty, or input numbers!")
        elif tg_var.lower() == "exit":
            print("Thank you for running runme.py! Have a bioinformatically awesome day!")
            sys.exit()
        else:
            y_n_query = input("Is '" + str(tg_var) + "' the taxonomy you wish to investigate? Y/N")
            if y_n_query.upper() == "Y":
                print("Thank you. You have inputted: '" + tg_var + "'.")
                return tg_var
            elif y_n_query.upper() == "N":
                print("Please enter the taxonomy name you are interested in.")
            elif y_n_query.upper() == "exit":
                print("Thank you for running runme.py! Have a bioinformatically awesome day!")
                sys.exit()
            else:
                print("Please input Y ('Yes') or N ('No').")

#search_database(args): Confirms that both protein protein family and taxonomic group are correctly input before proceeding.
def search_database(pfn_var, tg_var):
    while True:
        correct_search = input("Searching for " + pfn_var.capitalize() + " in the taxonomy " + tg_var.capitalize() + " in the NCBI Protein database. Is this correct? Y/N")
        if correct_search.upper() == "Y":
            print("Thank you.")
            break
        if correct_search.upper() == "N":
            print("Please run script again to input your protein family name and taxonomic group of interest.")
            break
        else:
            print("Please input Y ('Yes') or N ('No').")

#write_variables(): a function to write out the user protein family group and taxonomy to file to then use as inputs in bash scripts
def write_variables():
    subprocess.call(["touch", "variables.txt"])
    f = open("variables.txt", "w")
    f.write(search_query)
    f.close()

#example_esearch(): unused function that was to be used for running an example query using glucose-6-phosphatase and Aves as pfn_var and tg_var respectively
def example_esearch():
    subprocess.call(["touch", "example_esearch.txt"])
    with open("example_esearch.txt", "w") as outfile:
        example_query = "glucose-6-phosphatase AND aves"
        subprocess.call(["esearch", "-db", "protein", "-query", example_query], stdout=outfile) 
       

#esearch(): function used to query the NCBI protein database and return the number of sequences found (WORK IN PROGRESS)
def esearch():
    subprocess.call("./esearchxtract.sh", shell=True)
    with open("count", "r") as outfile:
        for line in outfile:
            count = int(line)
        if count <= 10000:
            while True:
                correct_search = input("Your search has returned " + str(count) + " number of sequences. Continue to download sequences? Y/N")
                if correct_search.upper() == "Y":
                    print("Thank you. Running efetch to download sequences in fasta format. Please be patient.")
                    return count
                if correct_search.upper() == "N":
                    print("Please run script again to do a new search.")
                    break
                else:
                    print("Please input Y ('Yes') or N ('No').")
                    break
        else:
            print("I'm sorry, your search has resulted in more than 10,000 results. Please narrow your search scope and run the program again.")
            exit()
            
#example_efetch(): unused function used to fetch a fasta file based on the previous esearch results
def example_efetch():
    subprocess.call(["touch", "example_efetch.fasta"])
    with open("example_efetch.fasta", "w") as outfile:
        subprocess.call(["efetch", "-db", "protein", "-id", example_webenv_var, "-format", "fasta"], stdout=outfile) 

#example efetch(): unused function that was to be used to fetch a fasta file based on previous esearch results
def efetch():
    subprocess.call(["touch", "efetch.fasta"])
    with open("efetch.fasta", "w") as outfile:
        cmd = "esearch -db protein -query " + search_query + " |  efetch -db protein -WebEnv " + webenv_var[0] + " -format fasta"
        subprocess.Popen(cmd, shell=True, stdout=outfile)
        #subprocess.call(["esearch", "-db", "protein", "-query", "'", search_query, "'", "|", "efetch", "-format", "fasta"], stdout=outfile)

#extract_webenv(): unused function that was to be used to extract the WebEnv section of an esearch query to feed into NCBI's history servers to retrieve fasta files.
def extract_webenv():
    string_var = "WebEnv"
    string_var_2 = "QueryKey"
    matchedLine = ""
    splicedLine = ""
    splicedLine2 = ""
    subprocess.call(["touch", "esearch.txt"])
    with open('esearch.txt', 'r') as file:
        for line in file:
            if string_var in line:
                matchedLine = line
                splicedLine = matchedLine[10:][:-10]
                break
            if string_var_2 in line:
                matchedLine2 = line
                splicedLine2 = matchedLine2[9:][:-11]
        with open("esearch_output.txt", "w") as file:
            file.write(splicedLine) #matchedLine
            file.write(splicedLine2)
            return [splicedLine, splicedLine2]

'''
I cannot get around including a bash script here to run the various analysis programmes. I tried using subprocess.call() with various 
syntaxes to have python execute scripts this way, but unfortunately the input/output piping didn't work correctly. I have tried to keep
bash scripting to a minimum.
'''

#execute_esearch(): function to run esearch and pipe result into efetch to fetch relevant FASTA files into a file called query_fasta.fasta
def execute_esearch():
    x = input("You are about to download FASTA files of your protein of interest. This may take a while. Proceed? Y/N")
    while True:
        if x.upper() == "Y":
            print("Thank you. Running script.")
            subprocess.call("./esearch.sh", shell=True)
            break
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break
        
#execute_makeblastdb(): function to run makeblastdb of the fasta files for sequence similarity alignment into a DB called seq_db
def execute_makeblastdb():
    x = input("You are about to create a database of your sequences of interest against which to BLAST. This may take a while. Proceed? Y/N")
    while True:
        if x.upper() == "Y":
            print("Thank you. Running script.")
            subprocess.call("./makeblastdb.sh", shell=True)
            break
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break

#execute_blastp(): this function runs blastp against the previously created seq_db, using a modified version of outfmt -7 that includes the fasta headers
def execute_blastp():
    x = input("You are about to BLAST your protein sequences against your local database in a multiple sequence alignment. Proceed? Y/N")
    while True:
        if x.upper() == "Y":
            print("Thank you. Running script.")
            subprocess.call("./blastp.sh", shell=True)
            break
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break

#execute_250_seq(): Once blastp has run, we extract the fasta headers only column from the 250 most similar sequences from the blastp output file   
def execute_250_seq():
    x = input("The max. 250 most similar sequences will be extracted. Proceed? Y/N")
    while True:
        if x.upper() == "Y":
            print("Thank you. Running script.")
            subprocess.call("./250extract.sh", shell=True)
            break
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break

#execute_pullseq(): function that uses pullseq program with the headers of the 250 most similar sequence headers to create a new fasta file.
def execute_pullseq():
    x = input("The max. 250 most similar sequences will be extracted from your fasta sequences for further analysis. Proceed? Y/N")
    while True:
        if x.upper() == "Y":
            print("Thank you. Running pullseq.")
            subprocess.call("./pullseq.sh", shell=True)
            break
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break
        
#execute_clustalo(): function that runs clustalo with input file containing the 250 most similar sequences in fasta format
def execute_clustalo():
    x = input("You are about to use clustalo to create a sequence clustering using your max. 250 most similar sequences. Proceed? Y/N")
    while True:
        if x.upper() == "Y":
            print("Thank you. Running script.")
            subprocess.call("./clustalo.sh", shell=True)
            break
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break
        
#execute_plotcon(): function that runs the EMBOSS plotcon program to plot conservation of sequence alignment of 250 most similar sequences.
def execute_plotcon():
    x = input("You are about to use PLOTCON to create a sequence conservation plot of the max. 250 sequences. Proceed? Y/N")
    while True:
        if x.upper() == "Y":
            print("Thank you. Running script.")
            subprocess.call("./plotcon.sh", shell=True)
            break
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break

'''

#create a dictionary of 250 most similar fasta sequences - LEGACY
def mofit_database_dict():
    fasta = defaultdict(list)
    with open("twofifty_final_fastas") as file_one:
        for line in file_one:
            if line.startswith(">"):
                fasta[line.strip("\n")].append(next(file_one).rstrip())
    return fasta
'''

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

'''
def patmatmotifs_loop():
    subprocess.call(["touch", "prositereport"])
    for value in fasta_dict.values():
            sequence = str(value)
            cmd = "patmatmotifs -sequence " + sequence + " -outfile prositereport -full True >> prositereport"
            subprocess.call(cmd, shell=True)
'''             
            
#testing by temporarily writing to a file
def patmatmotifs_loop():
    x = input("You are about to compare your max. 250 most similar sequences against PROSITE protein motifs. Proceed? Y/N")
    while True:
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
                    cmd = "patmatmotifs -sequence temp.fasta -sprotein1 True -verbose False -outfile prositereport" #-full True"
                    subprocess.call(cmd, shell=True)
                    cmd = "cat prositereport >> PROSITEdb"
                    subprocess.call(cmd, shell=True)
                    break
            subprocess.call(["echo", "-e", "Your final motif report is contained in the file PROSITEdb."])
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break    
        
def wildcard():
    x = ""
    while True:
        x = input("You can either run your 250 most similar sequences through an infoalign analysis to show information about all 250 sequences [Enter: 1], and/or run a pepstats analysis receive a report for protein statistics [Enter: 2]. To run both, enter 3. To exit the program, type 'exit'.")
        if x == "1":
            subprocess.call(["echo", "-e", "running infoalign..."])
            subprocess.call("./infoalign.sh", shell=True)
            subprocess.call(["echo", "-e", "Your info analysis is available in the file infoalign.report."])
            break
        if x == "2":
            subprocess.call(["echo", "-e", "running pepstats..."])
            subprocess.call("./pepstats.sh", shell=True)
            subprocess.call(["echo", "-e", "Your protein statistics are available in the file stats.pepstats."])
            break
        if x == "3":
             subprocess.call(["echo", "-e", "running infoalign and protein statistics..."])
             subprocess.call("./infoalign.sh", shell=True)
             subprocess.call("./pepstats.sh", shell=True)
             subprocess.call(["echo", "-e", "Your info analysis is available in the file infoalign.report."])
             subprocess.call(["echo", "-e", "Your protein statistics are available in the file stats.pepstats."])
             break
        if x.lower() == "exit":
            print("Thank you for running runme.py! Have a bioinformatically awesome day!")
            sys.exit()
        else:
            print("Please input 1 for infoalign, 2 for protein statistics, 3 for both, or type exit to quit program.")
            continue
            
        



'''
#retrieve top 250 similar sequences and put them in a file as a list
def loop_250():
    list_250 = []
    subprocess.call(["touch", "250_list.txt"])
    f = open("250_list.txt", "w")
    with open('250_acc_numbers', 'r') as file:
        for i in file:
            list_250 = list_250.append(i)
    f.write(list_250)
    f.close()
'''
          
def loop_250():
    list = open("250_acc_numbers").readlines()
    list[:] = [list.rstrip('\n') for line in list]
    list = str(list)
    subprocess.call(["touch", "250_list.txt"])
    f = open("250_list.txt", "w")
    f.write(list)
    f.close()
    





#Function to iterate through a blastp search, in order to pick out the 250 most high-scoring sequences
 
    
'''
#function unused
def iterate_blastp():
    list_250 = []
    with open('blastoutput1.out', 'r') as file:
        for i in range(0,250,1) in file:
            list_250 = list_250.append(i)
'''        
            




   
#example_webenv_var = example_extract_webenv()
#example_results_return = example_esearch()
#webenv_var = extract_webenv()
#print(example_webenv_var)
#print(webenv_var)

#FUNCTION CALLS
            
#Retrieve user input
pfn_var = test_pfn()
tg_var = test_tg()
final_search = search_database(pfn_var, tg_var)

search_query = pfn_var + " AND " + tg_var

write_variables()

#Further analysis

esearch()
#execute_esearch()
#execute_makeblastdb()
#execute_blastp()
#execute_250_seq()
#execute_pullseq()
#execute_clustalo()
#execute_plotcon()

#fasta_dict = mofit_database_dict()

#patmatmotifs_loop()

#wildcard()



