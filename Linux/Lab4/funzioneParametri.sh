#!/bin/bash
function saluta {
    while [ $1 ]; do
    echo "Ciao $1"
    shift
    done
}

saluta 'Marina' 'Chiara' 'Elena'