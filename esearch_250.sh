#!/bin/bash

VAR=`cat 250_acc_numbers`

#Runs an esearch with the user's inputted variables and feeds the result into an efetch to retrieve fasta files
echo -e "Running esearch and efetch..."

esearch -db protein -query "$VAR" | efetch -format fasta > 250_fasta.fasta

