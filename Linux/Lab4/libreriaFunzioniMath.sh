#!/bin/bash

function multipli {
    local n=$1
    local k=$2
    echo "I primi $k multipli di $n:"
    local i=1
    while [ $i -le $k ]; do
        ((x=n*i))
        echo -n "$x "
        ((i++))
    done
    echo 
  }
  
function somma {
    local s=0
    while [ $1 ]; do
        ((s=s+$1))
        shift
    done
    return $s
}

function prodotto {
    local p=1
    while [ $1 ]; do
        ((p=p*$1))
        shift
    done
    return $p
}

multipli 5 7
somma 1 2 3 4 5 6 7 8
echo "Somma -> $? "

prodotto 4 5 10
echo "Prodotto -> $?"