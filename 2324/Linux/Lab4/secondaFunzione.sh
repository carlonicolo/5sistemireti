#!/bin/bash
function prima {
    echo "Prima funzione."
    seconda
    echo "Ancora la prima funzione."
}
function seconda {
    echo "Seconda funzione."
}
echo "Inizio."
prima