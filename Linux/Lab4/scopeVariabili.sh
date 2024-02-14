#!/bin/bash
   
function pippo {
    local a
    a=2
    echo "Pippo: a = $a"
    }
     
function pluto {
    echo "Pluto: a = $a"
    a=3
    echo "Pluto: a = $a"
   }
a=1
echo "a = $a"
pippo
echo "a = $a"
pluto
echo "a = $a"