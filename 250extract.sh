#!/bin/bash

#remove top 5 lines from the blastp output file
grep -v "#" blastp_output | head -251 > 250_seq.txt

#print only column three - the headers to file
awk -F "\t" '{print $3}' 250_seq.txt > 250_headers_only


