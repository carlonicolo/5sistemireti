#! /usr/bin/bash

echo "### For loop 1..5 ###"
for i in {1..5}
do
echo $i
done

echo " "

echo "### For loop in words... ###"
for i in pippo pluto bunny
do
echo $i
done

echo " "
echo "### While loop ###"
j=1
while [[ $j -le 10 ]] ; do
   echo "$j"
  (( j += 1 ))
done