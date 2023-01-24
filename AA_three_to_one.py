# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:34:13 2021
@author: Harshal Bodke
"""
import pandas as pd
import re
# Three-Letter Code List (tlc)
tlc = ["Ala", "Arg", "Asn", "Asp", "Asx", "Cys", "Glu", "Gln", "Glx", "Gly", "His", "Ile", "Leu", "Lys", "Met", "Phe", "Pro", "Ser", "Thr", "Trp", "Tyr", "Val"]
# One-Letter Code List (olc)
olc = ["A", "R", "N", "D", "B", "C", "E", "Q", "Z", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
# Three to One-Letter Code Amino Acid Dictionary
aminoacid_dict = {tlc[i] : olc[i] for i in range(0, len(tlc))}

data = pd.read_excel(r"Input.xlsx", sheet_name="Sheet1")
# protein_change=["Ala157Thr", "Leu115Phe", "Pro1274GlnfsTer7", "Y171Y", "Ala1406=", "p.Ala430Thr", "Ala62_Pro63insAlaAlaAlaProAlaAla"] #test example
protein_change = data["Protein.Change"].tolist()
slc_code = []
for pchange in protein_change:
    pchange = pchange.replace("p.","")
    split = pchange.split(";")
    pchange = split[0]
    aminoacids = re.findall("[A-Za-z]{3}", pchange)
    for name in aminoacids:
        for j in aminoacid_dict.keys():
            if name == j:
                pchange = pchange.replace(name, aminoacid_dict[j])
    slc_code.append(pchange)

data["Protein.Change_1"] = slc_code
data.to_excel("Output.xlsx", sheet_name="Output_AA_code", na_rep="--", index=False, freeze_panes=(1, 1))
print("Successfully Done!")
