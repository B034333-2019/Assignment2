#%%

#IMPORT MODULES

import os
import subprocess
from subprocess import call
import functools 
import operator
import re

#GLOBAL VARIABLES

#test input: glucose-6-phosphatase in birds (Aves) NEED TO CHECK FOR 6 in the string

#Variable for the user input protein family name
pfn_var = ""

#Variable for the user input taxonomic group
tg_var = ""

#Number of sequences that are found during esearch
seq_count = ""
#FUNCTIONS


#test_pfn: function that checks the user input for the protein family name is a string, and not a number or logic operator

def test_pfn():
    pfn_var = ""
    while True:
        pfn_var = input("Please enter the protein family name you are interested in. Capitalisation is not important, but spelling is: ")
        pfn_var = pfn_var.lower()
        if pfn_var.isdigit():
            print("Your input is not in the correct format. Please input text. Do not input numbers.")
        else:
            y_n_query = input("Is '" + str(pfn_var) + "' the protein family you wish to investigate? Y/N")
            if y_n_query.upper() == "Y":
                print("Thank you. You have inputted: '" + pfn_var + "'.")
                return pfn_var
                break
            elif y_n_query.upper() == "N":
                pfn_var = input("Please enter the protein family name you are interested in: ")
                continue
            else:
                print("Please input Y ('Yes') or N ('No').")


#test_pfn: function that checks the user input for the taxonomy is a string, and not a number or logic operator

def test_tg():
    tg_var = ""
    while True:
        tg_var = input("Please enter the taxonomic group you are interested in. Again, capitalisation is not important, but spelling is: ")
        tg_var = tg_var.lower()
        if tg_var.isdigit():
            print("Your input is not in the correct format. Please input text. Do not input numbers.")
        else:
            y_n_query = input("Is '" + str(tg_var) + "' the taxonomic group you wish to investigate? Y/N")
            if y_n_query.upper() == "Y":
                print("Thank you. You have inputted: '" + tg_var + "'.")
                return tg_var
                break
            elif y_n_query.upper() == "N":
                tg_var = input("Please enter the taxonomic group you are interested in: ")
                continue
            else:
                print("Please input Y ('Yes') or N ('No').")
               

#Execute both test_pfn and test_tg functions to retrieve user input of protein families and taxonomic group
#%%

def search_database(pfn_var, tg_var):
    touple = (pfn_var, tg_var)
    correct_search = input("Searching for " + pfn_var.capitalize() + " in the taxonomy " + tg_var.capitalize() + " in the NCBI database. Is this correct? Y/N")
    while True:
        if correct_search.upper() == "Y":
            return touple
        if correct_search.upper() == "N":
            print("Please run script again to input your protein family name and taxonomic group of interest.")
            break
        else:
            print("Please input Y ('Yes') or N ('No').")


def write_variables():
    subprocess.call(["touch", "variables.txt"])
    f = open("variables.txt", "w")
    f.write(search_query)
    f.close()

#%%
pfn_var = test_pfn()
tg_var = test_tg()
final_search = search_database(pfn_var, tg_var)

#print(final_search)



#%%
#Python call to unix to execute Edirect suite
#Variables
#search_query = "esearch -db gene -query " + pfn_var + " AND " + tg_var
#Example query:

search_query = pfn_var + " AND " + tg_var

#search_query = "esearch -db gene -query " + pfn_var + " AND " + tg_var
#esearch_touch = subprocess.call(["touch", "esearch.txt"])

def example_esearch():
    subprocess.call(["touch", "example_esearch.txt"])
    with open("example_esearch.txt", "w") as outfile:
        example_query = "glucose-6-phosphatase AND aves"
        subprocess.call(["esearch", "-db", "protein", "-query", example_query], stdout=outfile) 
        
def esearch():
    subprocess.call(["touch", "esearch.txt"])
    with open("esearch.txt", "w") as outfile:
        subprocess.call(["esearch", "-db", "homologene", "-query", search_query], stdout=outfile) 
        #output = subprocess.Popen(['grep', "Count", "esearch.txt"], stdout=subprocess.PIPE).communicate()
        #subprocess.call(["grep", "Count", "esearch.txt"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #seq_count = seq_count[6:8]
        #print(output)
        #print(type(output))
        correct_search = input("Your search has returned X number of sequences. Continue to download sequences? Y/N")
        while True:
            if correct_search.upper() == "Y":
                print("Thank you. Downloading sequences. Please be patient.")
                return seq_count
            if correct_search.upper() == "N":
                print("Please run script again to do a new search.")
                break
            else:
                print("Please input Y ('Yes') or N ('No').")
                break

def example_efetch():
    subprocess.call(["touch", "example_efetch.fasta"])
    with open("example_efetch.fasta", "w") as outfile:
        subprocess.call(["efetch", "-db", "protein", "-id", example_webenv_var, "-format", "fasta"], stdout=outfile) 
        
def efetch():
    subprocess.call(["touch", "efetch.fasta"])
    with open("efetch.fasta", "w") as outfile:
        cmd = "esearch -db protein -query " + search_query + " |  efetch -db protein -WebEnv " + webenv_var[0] + " -format fasta"
        subprocess.Popen(cmd, shell=True, stdout=outfile)
        #subprocess.call(["esearch", "-db", "protein", "-query", "'", search_query, "'", "|", "efetch", "-format", "fasta"], stdout=outfile)
         
#esearch -db protein -query "lycopene cyclase" |  efetch -format fasta
        
#get line
def example_extract_webenv():
    string_var = "WebEnv"
    matchedLine = ""
    splicedLine = ""
    subprocess.call(["touch", "example_esearch.txt"])
    with open('example_esearch.txt', 'r') as file:
        for line in file:
            if string_var in line:
                matchedLine = line
                splicedLine = matchedLine[10:][:-10]
                break
    with open("example_esearch_output.txt", "w") as file:
        file.write(splicedLine)
        return splicedLine
    
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
I cannot get around including a bash script here to run the various analysis programmes. I tried using /subprocess.call() with various 
syntaxes to have python execute scripts this way, but unfortunately the input/output piping didn't work correctly. I have tried to keep
bash scripting to a minimum.
'''
def execute_bash():
    x = input("You are about to download FASTA files of your protein of interest, and then perform a multiple sequence alignment. This may take a while. Proceed? Y/N")
    while True:
        if x.upper() == "Y":
            print("Thank you. Running script.")
            subprocess.call("./bashscript.sh", shell=True)
            break
        if x.upper() == "N":
             print("Please run script again to do a new search.")
             break
        else:
            print("Please input Y ('Yes') or N ('No').")
            break
            
#Function to iterate through a blastp search, in order to pick out the 250 most high-scoring sequences
 
    #%%
practice_list  = ["red", "green", "orange", "yellow"]    
    
def iterate_blastp():
    list_250 = []
    with open('blastoutput1.out', 'r') as file:
        for i in range(0,250,1) in file:
            list_250 = list_250.append(i)
            
            

#%%

example_results_return = example_esearch()
esearch()
    
#example_webenv_var = example_extract_webenv()
webenv_var = extract_webenv()
#print(example_webenv_var)
print(webenv_var)

write_variables()
execute_bash()

iterate_blastp()

#example_efetch()
#efetch()



#%% - end 

#Print to console what search choices are about to be made. Maybe include italics and capitals?



#print("Searching for " + pfn_var.capitalize() + " in the taxonomy " + tg_var.capitalize() + " in the NCBI database.")
#touple = (pfn_var, tg_var)

#print(type(touple))

#print(touple)

#print(touple[0], touple[1])

#%%

