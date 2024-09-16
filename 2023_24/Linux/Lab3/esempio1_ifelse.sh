#! /usr/bin/bash

read -p "Inserisci il primo numero intero: " val1
read -p "Inserisci il secondo numero intero: " val2



if [ $val1 -gt $val2 ]
then
echo "$val1 is greater than $val2"
elif [ $val1 -lt $val2 ]
then
echo "$val1 is less than $val2"
elif [ $val1 -eq $val2 ]
then
echo "$val1 is equal to $val2"
fi