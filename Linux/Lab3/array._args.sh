#! /usr/bin/bash

# chomd +x array_args.sh
# ./array_args.sh blue yellow green


echo "for con Argomenti passati allo script"

z=1

for x in $@
do
    echo "arg $z is $x"
    z=$((z+1))
done

myarr=("pippo" "pluto" "bunny")

#${myArray[@]}


for i in ${myarr[@]}; do
echo $i
done

for i in ${!myarr[@]}; do
  echo "element $i is ${myarr[$i]}"
done

echo ${myarr[2]}