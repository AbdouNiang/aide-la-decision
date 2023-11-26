import pandas as pd
import Electre as elec


nomColone=[]
for i in range (7):
    nomColone.append("g"+str(i))


donnees=pd.read_csv("data/donnees.csv",names=nomColone)
nb_candidat=len(donnees)
nb_critere=len(donnees.columns)
donneesMat=[]
for i in range(nb_candidat):
    donneeL=[]
    for j in range(nb_critere):
        donneeL.append(donnees.iloc[i,j])
    donneesMat.append(donneeL)


poid=[0.2,0.1,0.25,0.2,0.15,0.05,0.05]
func=[1,0,1,1,0,0,1]
valVeto=[4000,150,2,10,3,50,5]
valSeuil=[800,10,0.2,2,2,10,2]
A1= [[80, 90, 600,5.4,8,5],[65,58,200,9.7,1,1],[83,60,400,7.2,4,7],[40,80,1000,7.5,7,10],[52,72,600,2.0,3,8],[94,96,700,3.6,5,6]]
A2=[0.1,0.2,0.2,0.1,0.2,0.2]
A3=[1,0,1,1,1,0]
A5=[1,2,3,4,5,6]
Veto=[45,29,550,6,4.5,4.5]
valSeuil2=[20,10,200,4,2,2]
modele=["Alpha romeo","Audi A4","Xantia","Peugeot 406","SAAB", "Laguna", "Passat", "BMW 320d" ,"xara", "Safrane"]
#print(pro.getClasementphiPlus(donneesMat,poid,func,nb_candidat,modele))
liens=elec.ElectreIs(donneesMat,poid,func,nb_candidat,modele,valVeto,0.6,valSeuil)
print(liens)


