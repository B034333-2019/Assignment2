#!/bin/bash

VAR=`cat variables.txt`
VAR2=`cat esearch_output.txt`
 
echo $VAR
#Runs an esearch with the user's inputted variables and feeds the result into an efetch to retrieve fasta files
echo -e "Running esearch and efetch..."
esearch -db protein -query "$VAR" | efetch -format fasta > query_fasta.fasta

