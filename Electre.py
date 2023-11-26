import networkx as nx
import matplotlib.pyplot as plt

def DuelPromethe(v1,v2,poid,func,donnees):

    result=0
    for i in range (len(poid)):
       if (func[i]==0):
            if (donnees[v1][i]>donnees[v2][i]):
                result+=poid[i]
       else:
           if (donnees[v1][i]<donnees[v2][i]):
               result+=poid[i]
    return result

def matricePromethe(donnees,poid,func,nb_candida):
    matriceResult=[]
    for i in range(nb_candida):
        resultligne=[]
        for j in range(nb_candida):
            resultDuel=DuelPromethe(i,j,poid,func,donnees)
            resultligne.append(resultDuel)
        matriceResult.append(resultligne)
    for i in range(nb_candida):
        print(matriceResult[i])
    return matriceResult

def getClasementphiPlus(donnees,poid,func,nb_candida,modele):
    matcondence=matricePromethe(donnees,poid,func,nb_candida)
    scoreVoiturpositif = []
    for i in range(nb_candida):
        phiPlus =0
        for j in range(nb_candida):
            phiPlus += matcondence[i][j]
        scoreVoiturpositif.append(phiPlus)
    classementmodele=[]
    for i in range(nb_candida):
        valeurMax=max(scoreVoiturpositif)
        index=scoreVoiturpositif.index(valeurMax)
        scoreVoiturpositif[index]=0
        classementmodele.append(modele[index])
    return classementmodele

def getClasementphiMoins(donnees,poid,func,nb_candida,modele):
    matcondence=matricePromethe(donnees,poid,func,nb_candida)
    scoreVoiturNegatif = []
    for i in range(nb_candida):
        phiMoins =0
        for j in range(nb_candida):
            phiMoins += matcondence[j][i]
        scoreVoiturNegatif.append(phiMoins)
    classementmodele=[]
    for i in range(nb_candida):
        valeurMax=min(scoreVoiturNegatif)
        index=scoreVoiturNegatif.index(valeurMax)
        scoreVoiturNegatif[index]=1000
        classementmodele.append(modele[index])
    return classementmodele
def generer_graphe(liens):
    G = nx.DiGraph()

    for lien in liens:
        if(len(lien)==2):
            source, cible = lien
            G.add_edge(source, cible)
        else:
            node=lien
            G.add_node(node[0])
    return G
def afficher_graphe(graphe):
    pos = nx.spring_layout(graphe)
    nx.draw(graphe, pos, with_labels=True, font_weight='bold',arrows=True)
    plt.show()
def DuelELectre(v1,v2,poid,func,donnees,valVeto):
    veto=0
    result=0
    for i in range (len(poid)):
       if (func[i]==0):
            if (donnees[v1][i]>donnees[v2][i]):
                result+=poid[i]
            else :
                if (veto==0):
                    distance=donnees[v2][i]-donnees[v1][i]
                    if (distance > valVeto[i]):
                        veto=1
       else:
           if (donnees[v1][i]<donnees[v2][i]):
               result+=poid[i]
           else:
               if (veto == 0):
                   distance = donnees[v1][i] - donnees[v2][i]
                   if (distance > valVeto[i]):
                       veto = 1

    return result,veto

def matriceElectre(donnees,poid,func,nb_candida,valVeto):
    matriceResult=[]
    matriceVeto=[]
    for i in range(nb_candida):
        resultligne=[]
        vetoligne=[]
        for j in range(nb_candida):
            resultDuel,veto=DuelELectre(i,j,poid,func,donnees,valVeto)
            resultligne.append(resultDuel)
            vetoligne.append(veto)
        matriceResult.append(resultligne)
        matriceVeto.append(vetoligne)
    return matriceResult,matriceVeto

def Electre(donnees,poid,func,nb_candida,modele,valVeto,seuil):
    classementmodele = []
    matriceResult,matriceVeto=matriceElectre(donnees,poid,func,nb_candida,valVeto)
    liens=[]

    print("vet0",matriceVeto)
    print(matriceResult)
    isOnGraph=[]
    for i in range(nb_candida):
        isOnGraph.append(0)
    for i in range(nb_candida):

        for j in range(nb_candida):
            lien=[]
            if(matriceResult[i][j]>=seuil and matriceVeto[i][j]==0 and  i!=j):
                lien.append(modele[i])
                lien.append(modele[j])
                liens.append(lien)
                isOnGraph[i]=1
                isOnGraph[j]=1

    i=0
    for valeur in isOnGraph:
        if valeur==0:
            lien=[]
            lien.append(modele[i])
            liens.append(lien)
        i+=1
    graphe = generer_graphe(liens)
    afficher_graphe(graphe)





    return liens

def DuelELectreIs(v1,v2,poid,func,donnees,valVeto,valseuil):
    veto=0
    result=0
    for i in range (len(poid)):
       if (func[i]==0):
            if (donnees[v1][i]>donnees[v2][i]):
                result+=poid[i]
            else :
                distance = donnees[v2][i] - donnees[v1][i]
                if(valseuil[i]>distance):
                    distanceseuil=valseuil[i]-distance
                    result+=(distanceseuil*poid[i])/valseuil[i]
                if (veto==0):

                    if (distance > valVeto[i]):
                        veto=1
       else:
           if (donnees[v1][i]<donnees[v2][i]):
               result+=poid[i]
           else:
               distance = donnees[v1][i] - donnees[v2][i]
               if (valseuil[i] > distance):
                   distanceseuil = valseuil[i] - distance
                   result+= (distanceseuil * poid[i]) / valseuil[i]
               if (veto == 0):

                   if (distance > valVeto[i]):
                       veto = 1


    return result,veto

def matriceElectreIs(donnees,poid,func,nb_candida,valVeto,valseuil):
    matriceResult=[]
    matriceVeto=[]
    for i in range(nb_candida):
        resultligne=[]
        vetoligne=[]
        for j in range(nb_candida):
            resultDuel,veto=DuelELectreIs(i,j,poid,func,donnees,valVeto,valseuil)
            resultligne.append(resultDuel)
            vetoligne.append(veto)
        matriceResult.append(resultligne)
        matriceVeto.append(vetoligne)
    return matriceResult,matriceVeto

def ElectreIs(donnees,poid,func,nb_candida,modele,valVeto,seuil,valSeuil):
    classementmodele = []
    matriceResult,matriceVeto=matriceElectreIs(donnees,poid,func,nb_candida,valVeto,valSeuil)
    matriceResult,matriceVeto=matriceElectreIs(donnees,poid,func,nb_candida,valVeto,valSeuil)
    liens=[]
    for i in  range(nb_candida):
        print("vet0", matriceVeto[1])



    isOnGraph = []
    for i in range(nb_candida):
        isOnGraph.append(0)
    for i in range(nb_candida):

        for j in range(nb_candida):
            lien=[]
            if(matriceResult[i][j]>=seuil and matriceVeto[i][j]==0 and  i!=j):
                lien.append(modele[i])
                lien.append(modele[j])
                liens.append(lien)
                isOnGraph[i] = 1
                isOnGraph[j] = 1

    i = 0
    for valeur in isOnGraph:
        if valeur == 0:
            lien = []
            lien.append(modele[i])
            liens.append(lien)
        i += 1
    graphe = generer_graphe(liens)
    afficher_graphe(graphe)
    return liens
