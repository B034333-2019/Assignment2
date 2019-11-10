#!/bin/bash

#creates a blast database from the retrieved files from esearch.sh
echo -e "Running makeblastdb..." 
makeblastdb -in query_fasta.fasta -dbtype prot -out seq_db

