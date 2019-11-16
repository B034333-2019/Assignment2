#!/bin/bash

grep -v "^>" 250_final_fastas.fasta > testforpatmatmotif

patmatmotifs -sequence twofifty_final_fastas -sformat1 fasta -outfile prositereport -full True
