#!/bin/bash

VAR=`cat variables.txt`
echo $VAR

esearch -db protein -query $VAR |  efetch -format fasta