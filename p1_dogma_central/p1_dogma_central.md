# Práctica 1, Dogma Central

### Funcionamiento General:

1. Al iniciar el programa, pide al usuario una secuencia
2. Verifica que la secuencia sea válida
3. Imprime la cadena complementaria de la secuencia
4. Obtiene la transcripción de la secuencia
5. Si tiene codón de inicio, obtiene la cadena de aminoacidos y la imprime
6. En otro caso indica que no tiene codón de inicio y termina el programa

### Funciones:
1. validacion(secuencia):  Recibe una cadena y verifica que sea una secuencia de ADN
2. complementaria(secuencia): Recibe una secuencia y obtiene su secuencia complementaria
3. transcripcion(secuencia): Recibe una secuencia y regresa la transcripción a mRNA
4. codon_inicio(secuencia): Recibe una secuencia y verifica si los primeros 3 caracteres forman un codón de inicio
5. aminoacidos(secuencia): Recibe una secuencia y regresa la cadena de aminoácidos que codifica
