#!/bin/bash

#runs blastp with output blastp_output
echo -e "Running blastp... please be patient."

#changed outfmt to include headers

blastp -query query_fasta.fasta -db seq_db -outfmt '7 qseqid sseqid stitle pident length mismatch gapopen qstart qend sstart send evalue bitscore' -out blastp_output

