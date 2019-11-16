#!/bin/bash

VAR=`cat variables.txt`


#Running a conservation plot using plotcon using input file 250_clustalo_output and output to plotcon.svg

echo -e "Running plotcon..."
plotcon -sequences 250_clustalo_output -winsize 8 -graph svg
echo -e "Thank you. Your conservation plot is available in the file 'plotcon.svg'. Opening file..."

#xdg-open plotcon.svg

