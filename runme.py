#%%

#IMPORT MODULES

import os
import subprocess
from subprocess import call
import functools 
import operator

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
    pfn_var = input("Please enter the protein family name you are interested in. Capitalisation is not important, but spelling is: ")
    while True:
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
    tg_var = input("Please enter the taxonomic group you are interested in. Again, capitalisation is not important, but spelling is: ")
    while True:
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
        subprocess.call(["esearch", "-db", "gene", "-query", example_query], stdout=outfile) 
        
def esearch():
    subprocess.call(["touch", "esearch.txt"])
    with open("esearch.txt", "w") as outfile:
        subprocess.call(["esearch", "-db", "gene", "-query", search_query], stdout=outfile) 
        output = subprocess.Popen(['grep', "Count", "esearch.txt"], stdout=subprocess.PIPE).communicate()
        #subprocess.call(["grep", "Count", "esearch.txt"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #seq_count = seq_count[6:8]
        print(output)
        print(type(output))
        correct_search = input("Your search has returned X number of sequences. Continue to download sequences? Y/N")
        while True:
            if correct_search.upper() == "Y":
                print("Thank you. Downloading sequences.")
                return seq_count
            if correct_search.upper() == "N":
                print("Please run script again to do a new search.")
                break
            else:
                print("Please input Y ('Yes') or N ('No').")
                break
            
example_esearch()
esearch()

#%% - end 

#Print to console what search choices are about to be made. Maybe include italics and capitals?



#print("Searching for " + pfn_var.capitalize() + " in the taxonomy " + tg_var.capitalize() + " in the NCBI database.")
#touple = (pfn_var, tg_var)

#print(type(touple))

#print(touple)

#print(touple[0], touple[1])

#%%

