#=====================================
# Nom du fichier : test.Python  	 =
# Date: 01/04/2021					 =
# Auteur : Thomas TBP				 =
# Objectif :  lire fichier txt		 =
#=====================================

import os
import numpy as np
import pandas as pd
import re 


Fichier_testG= open('C:/Python/1.Audit/vsalaire_v2.txt')
toutesleslignesG = Fichier_testG.readlines()
regex = re.compile(" {2,}")
output = list(map(lambda x: regex.sub(";", x), toutesleslignesG))
with open('C:/Python/1.Audit/vsalaire_2.csv', "w") as f:
	f.writelines(output)
df = pd.read_csv('C:/Python/1.Audit/vsalaire_2.csv', skiprows = 1, delimiter =";")
df.to_csv('C:/Python/1.Audit/vsalaire_v6.csv')


