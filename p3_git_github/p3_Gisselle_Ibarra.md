## Práctica 3 Genómica Computacional

1. Colócate dentro de tu carpeta practicas_genomica_computacional e inicializala como un repositorio local de git.
**Comando**
```bash
$ git init
```
**Salida**
```bash
Initialized empty Git repository in /home/gisselleibarra/Documents/GenómicaComputacional/Practicas/practicas_genomica_computacional/.git/
```

2. Agrega al área de espera todo el contenido de ésta carpeta.
**Comando**
```bash
$ git add .
```

3. Haz un primera confirmación de todo el contenido con el mensaje “Prácticas de Genomica Computacional”.
**Comando**
```bash
$ git commit -m "Prácticas Genómica Computacional"
```
**Salida**
```bash
[master (root-commit) cef6dfb] Prácticas Genómica Computacional
 15 files changed, 1921918 insertions(+)
 create mode 100644 "p1_dogma_central/p1_IbarraMontero_GisselleMar\303\255a.py"
 create mode 100644 p2_ngs_bash/.ipynb_checkpoints/MedinaAmayoDiegoAlonso-checkpoint.ipynb
 create mode 100644 p2_ngs_bash/.ipynb_checkpoints/p2_bash_ngs-checkpoint.ipynb
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/.ipynb_checkpoints/p2_bash_ngs-checkpoint.ipynb
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/data/filtered/cp_rabies_lyssavirus.gff3
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/data/raw_data/rabies_lyssavirus.fasta
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/data/raw_data/rabies_lyssavirus.fastq
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/data/raw_data/rabies_lyssavirus.gb
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/data/raw_data/rabies_lyssavirus.gff3
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/figures/barplot.png
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/scripts/.ipynb_checkpoints/p2_bash_ngs-checkpoint.ipynb
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/scripts/barplot_data.txt
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/scripts/p2_bash_ngs.ipynb
 create mode 100644 p2_ngs_bash/p2_gisselle_ibarra/scripts/plot_data.py
 create mode 100644 p3_git_github/p3_git.md
```

4. Crea un archivo .md en tu carpeta p1_dogma_central que describa qué hace tu programa. Si hay funciones dentro, qué hace cada función.
**Comando**
```bash
$ touch p1_dogma_central/p1_dogma_central.md
```

5. Agrega la modificación de la instrucción anterior a tu área de espera y luego haz la confirmación que lleve el siguiente mensaje “Descripcion de programa.”
**Comando**
```bash
$ git add p1_dogma_central/p1_dogma_central.md
```
**Comando**
```bash
$ git commit -m "Descripción de programa"
```
**Salida**
```bash
[master 7aa520f] Descripción de programa
 1 file changed, 17 insertions(+)
 create mode 100644 p1_dogma_central/p1_dogma_central.md
```

6. Checa el historial de confirmaciones que has hecho.
**Comando**
```bash
$ git log
```
**Salida**
```bash
commit 7aa520f660d9748df2cdb43a460de135272e6293 (HEAD -> master)
Author: GisselleIb <gisselleIb@ciencias.unam.mx>
Date:   Thu May 19 17:48:19 2022 -0500

    Descripción de programa

commit cef6dfb8e88af2a78553da20d70e043998741054
Author: GisselleIb <gisselleIb@ciencias.unam.mx>
Date:   Thu May 19 17:07:39 2022 -0500

    Prácticas Genómica Computacional
```

7. Checa en qué rama te encuentras.
**Comando**
```bash
$ git branch
```
**Salida**
```bash
* master
```

8. Conecta éste repositorio local a tu repositorio remoto.
**Comando**
```bash
$ git remote add origin git@github.com:GisselleIb/GC-Pr-cticas-GisselleIbarraMoreno.git
$ git branch -M main
$ git push -u origin main
```

9. Crea un archivo README.md en tu repositorio remoto que contenga:

    - A modo de encabezado: “Prácticas - Genómica computacional - 2022”

    - Luego una línea en blanco.

    - En la tercera línea tu nombre completo en negritas.

    - OPCIONAL: Una descripción del contenido de éste repositorio.

10. Agrega las modificaciones de tu repositorio remoto a tu repositorio local.
**Comando**
```bash
$ git pull origin main
```
**Salida**
```bash
From github.com:GisselleIb/GC-Pr-cticas-GisselleIbarraMoreno
 * branch            main       -> FETCH_HEAD
Merge made by the 'recursive' strategy.
 README.md | 5 +++++
 1 file changed, 5 insertions(+)
 create mode 100644 README.md
```

11. Guarda el archivo de ésta sección en tu repo local como: p3_tuNombre_tuApellido dentro de p3_git_github. Agregalo a área de espera, confirma con el mensaje “Comandos de p3” y agrégalo a tu repo remoto.

**Comando**
```bash
$ git add p3_git_github/p3_Gisselle_Ibarra.md
```
**Comando**
```bash
$ git commit -m "Comandos de p3"
```
