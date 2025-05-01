def lire_fasta(nom_fichier):
    file = open(nom_fichier)
    lines= file.readlines()
    sequence = ""
    for lig in lines:
        #ne récupérer que la ligne de séquence
        if not lig.startswith('>'):
            sequence += lig.strip()#supprimer les espaces
    return sequence.upper()#sequence en majuscule


seq1=lire_fasta("seq1.fasta" )
seq2=lire_fasta("seq2.fasta" )

#packages pour alignement
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
#alignement global sans pénalités (match = 1, mismatch = 0, gap = 0)
alignment = pairwise2.align.globalxx(seq1, seq2)
#afficher l'alignement
for a in alignment:
    print(format_alignment(*a))

    
#alignement global avec pénalités personnalisées
#(match, mismatch, open_gap, extend_gap)
alignment2 = pairwise2.align.globalms(seq1, seq2, 2, -1, -2, -0.5)
# afficher le premier alignement optimal
best_alignment = alignment2[0]

#sauvegarder l'alignement personnalisé
with open("alignement_personnalisé", "w")as fichier:
    fichier.write(format_alignment(*best_alignment))



               
               
               
