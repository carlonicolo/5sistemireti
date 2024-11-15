#! /usr/bin/bash

mkdir helloworld_v2 && cd helloworld_v2
touch helloworld_v2.c
echo "#include<stdio.h>" > helloworld_v2.c
echo " " >> helloworld_v2.c
echo "int main(){"  >> helloworld_v2.c
echo "printf(\"Hello to my hello world C program version version 2 \");" >> helloworld_v2.c
echo "return 0;" >> helloworld_v2.c
echo "}" >> helloworld_v2.c

echo " "
echo "cat helloworld_v2.c"
cat helloworld_v2.c

echo " "
echo "Compilazione file - gcc helloworld_v2.c -o hello_v2"
gcc helloworld_v2.c -o hello_v2
echo " "
echo "Compilazione terminata"

echo " "
echo "Permessi chmod +x"
chmod +x hello_v2
echo "Esecuzione programma ./hello_v2"
./hello_v2
echo " "
echo "Rimozione cartella"
cd .. && rm -R helloworld_v2
echo "Cartella rimossa"
ls -a



