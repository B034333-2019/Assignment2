#!/bin/bash

VAR=`cat variables.txt`

echo $VAR

esearch -db protein -query "$VAR" -spell | xtract -pattern ENTREZ_DIRECT -element Count > count
