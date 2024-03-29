#!/bin/bash

VAR=`cat variables.txt`
VAR2=`cat esearch_output.txt`

echo $VAR

esearch -db protein -query "$VAR" | efetch -format fasta > query_fasta.fasta

#makeblastdb -in query_fasta.fasta -dbtype prot -out seq_db

blastp -query query_fasta.fasta -db nr -remote -out blastp_output

