
#  Mini-projet Bioinformatique – Alignement de séquences ADN

Ce mini-projet Python permet de lire deux séquences ADN à partir de fichiers `.fasta`, de les aligner globalement avec le module `Biopython.pairwise2`et d'afficher le score d'alignement
Dans ce projet, on fait aussi un alignement global personnalisé, et on enregistre le résultat dans un fichier `.txt`.

---

##  Fonctionnalités

- Lecture de deux fichiers `.fasta`
- Alignement global sans pénalités
- Affichage de l'alignement dans le terminal
- Alignement global avec pénalités
- Sauvegarde de l'alignement avec pénalités personnalisées dans un fichier texte

---

##  Exemple de fichiers `.fasta`

`seq1.fasta`
```
>seq1
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
```

`seq2.fasta`
```
>seq2
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGACCGATAG
```

---

## 💻 Lancer le script

```bash
python alignement_seq.py
```

Le fichier d'alignement sera sauvegardé sous :  
📄 `alignement_personnalisé.txt`



---

## 🧰 Dépendances

- Python 3
- biopython
- matplotlib

Installez-les avec :

```bash
pip install biopython matplotlib
```

---

##  Auteure

Rim Hamouda 

[🔗 https://www.linkedin.com/in/rim-hamouda-b33992214/) | (https://github.com/RimHamouda)
