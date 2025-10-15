# Bash: Funzioni

## Primo esempio funzione

```bash
#!/bin/bash
function saluta {
echo -n "Ciao! "
}
for ((i=0; i<3; i++)); do
saluta
done
```


## Funzioni con parametri
