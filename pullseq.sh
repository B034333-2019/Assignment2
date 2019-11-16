#!/bin/bash

#Using pullseq with the -n flag file containing the headers of the 250 most similar sequences to output a fasta file of the same
/localdisk/data/BPSM/Assignment2/pullseq -i query_fasta.fasta -n 250_headers_only > twofifty_final_fastas

