
import random
from math import sqrt


## remarques

# generer les hopitaux d'une autre maniere : en avoir un peu en bretagne des le depart ( la meme concentration que le reste de la france


## definition des classes

class corps_repulsif :
    def __init__(self,coord,vitesse,masse):
        self.masse = masse
        self.coord = coord
        self.vitesse = vitesse
        self.rayon = (self.masse/3.14)**(1/3)

class corps_attractifs :
    def __init__(self,coord,vitesse,masse):
        self.masse = masse
        self.coord = coord
        self.vitesse = vitesse
        self.rayon = (self.masse/3.14)**(1/3)

## générateurs de corps

def generateur_corps_repulsifs (nbr_corps):
    liste_corps = []
    for k in range (nbr_corps):
        m = 1000
        while m <=0 :
            m = 1000
        liste_corps.append( corps_repulsif((random.uniform(200,600),random.uniform(150,600)),(random.uniform(0,1),random.uniform(0,1)),m) )
    return liste_corps

def generateur_bretagne (nbr_corps):
    liste_corps = []
    for k in range (nbr_corps):
        x = random.uniform(30,150)
        y = random.uniform(200,250)
        m = 1000
        while m <=0 :
            m = 1000
        liste_corps.append( corps_repulsif((x,y),(random.uniform(0,1),random.uniform(0,1)),m) )
    return liste_corps

def generateur_nord (nbr_corps):
    liste_corps = []
    for k in range (nbr_corps):
        x = random.uniform(350,420)
        y = random.uniform(25,100)
        m = random.gauss(400,1000)
        while m <=0 :
            m = random.gauss(400,1000)
        liste_corps.append( corps_repulsif((x,y),(random.uniform(0,1),random.uniform(0,1)),m) )
    return liste_corps


def generateur_corps_attractif (nbr_corps):
    liste_corps = []
    for k in range (nbr_corps):
        m = random.gauss(100,500)
        while m <=0 :
            m = random.gauss(100,500)
        liste_corps.append( corps_repulsif((random.uniform(200,600),random.uniform(150,600)),(0,0),m) )
    return liste_corps

## Opérations

def addition_couple (a,b):
        (x,y) = a
        (z,t) = b
        return (z+x,t+y)

def soustraction_couple (a,b):
        (x,y) = a
        (z,t) = b
        return (z-x,t-y)

def scalaire_couple (a,k):
        (x,y) = a
        return (x*k,y*k)

def distance_couple (a,b):
        (x,y) = a
        (z,t) = b
        return sqrt((x-z)**2 + (y-t)**2)

def soustraction(self,other):
    if self == other : return (0,0)
    else :
        a = self.coord
        b = other.coord
        (x,y) = a
        (z,t) = b
        return (z-x,t-y)

def add(self,other):
    if self == other :
        a = self.coord
        (x,y) = a
        return (2*x,2*y)
    else :
        a = self.coord
        b = other.coord
        (x,y) = a
        (z,t) = b
        return (z+x,t+y)

def scalaire(self,k):
    a = self.coord
    (x,y) = a
    return(k*x,k*y)

def mult (self,other):
    if self == other :
        a = self.coord
        (x,y) = a
        return (x*x,y*y)
    else :
        a = self.coord
        b = other.coord
        (x,y) = a
        (z,t) = b
        return (x*z,y*t)

def signe(self):
    a = self.coord
    x,y = a
    if x< 0 and y < 0 : return (-1,-1)
    elif x>= 0 and y < 0 : return (1,-1)
    elif x>= 0 and y >= 0 : return (1,1)
    elif x< 0 and y >= 0 : return (-1,1)

def distance(self,other):
    c,d = soustraction(self,other)
    return sqrt(c*c + d*d)

## Physique


def force_attractive (self,other,g):
    if self == other : self.dv = (0,0)
    else :
        self.dist = distance(self,other)
        if self.dist == 0 :
            self.dv = (0,0)
        else :
            self.direction = scalaire_couple (soustraction(self,other),1/self.dist)
            self.dv = scalaire_couple(self.direction, ((g*other.masse)/(self.dist*self.dist)))
            if self.dist < self.rayon + other.rayon :
                self.dv = scalaire_couple(self.dv,-0.5)
                self.vitesse = scalaire_couple(self.vitesse ,-0.9)
    self.vitesse = addition_couple ( self.vitesse, self.dv)

def force_repulsive (self,other,q):
    if self == other : self.dv = (0,0)
    else :
        self.dist = distance(self,other)
        if self.dist == 0 :
            self.dv = (0,0)
        else :
            self.direction = scalaire_couple (soustraction(self,other),-1/self.dist)
            self.dv = scalaire_couple(self.direction,q*(other.masse)/(self.dist*self.dist))
            if self.dist < self.rayon + other.rayon :
                self.dv = scalaire_couple(self.dv,-0.5)
                self.vitesse = scalaire_couple(self.vitesse ,-0.8)
    self.vitesse = addition_couple ( self.vitesse, self.dv)

def frottements(self,alpha):
    self.vitesse = scalaire_couple(self.vitesse,(1-alpha))

# def cadre(self):
#     a = self.coord
#     r = self.rayon
#     x,y = a
#     c,b = self.vitesse
#
#     if x > 600-r:
#         if c > 0 :
#             self.vitesse = (-0.9*c,b)
#         self.coord = (x-1,y)
#     if x < 100+r :
#         if c < 0 :
#             self.vitesse = (-0.9*c,b)
#         self.coord = (x+1,y)
#     if y > 600-r :
#         if b > 0 :
#             self.vitesse = (c,-0.9*b)
#         self.coord = (x,y-1)
#     if y < 100+r:
#         if b < 0 :
#             self.vitesse = (c,-0.9*b)
#         self.coord = (x,y+1)

centre = (405,350)

def cadre_corps (self,liste_corps_cadre):
    rep = False
    for corps in liste_corps_cadre :
        self.dist = distance(self,corps)
        if self.dist < self.rayon + corps.rayon : rep = True
    if rep :
        #self.vitesse = scalaire_couple(self.vitesse ,-0.8)
        point = self.coord
        dist = distance_couple(point,centre)
        direction = scalaire_couple(soustraction_couple(centre,point),-1/dist)
        self.vitesse = scalaire_couple(direction,0.9*distance_couple(self.vitesse,(0,0)))
# def repechage(self):
#     a = self.coord
#     r = self.rayon
#     x,y = a
#     c,b = self.vitesse
#
#     if x > 900-r:
#         if c > 0 :
#             self.vitesse = (-0.5*c,b)
#         #self.coord = (600,y)
#     if x < -200+r :
#         if c < 0 :
#             self.vitesse = (-0.5*c,b)
#         #self.coord = (0,y)
#     if y > 900-r :
#         if b > 0 :
#             self.vitesse = (c,-0.5*b)
#         #self.coord = (x,600)
#     if y < -200+r:
#         if b < 0 :
#             self.vitesse = (c,-0.5*b)
#         #self.coord = (x,0)



## simulation

from tkinter import *
from PIL import ImageGrab

def animation (temps_max,liste_corps_repulsifs,liste_corps_attractifs,g,q,alpha,liste_corps_cadre,numero):

    root = Tk()
    root.title = ('simulation gravité')
    canvas = Canvas( root, width = 700 , height = 700 , bg = 'white')
    canvas.grid(row=0,column=0)

    def photo():
        box = (Canvas.winfo_rootx(canvas),Canvas.winfo_rooty(canvas),Canvas.winfo_rootx(canvas)           +Canvas.winfo_width(canvas),Canvas.winfo_rooty(canvas) + Canvas.winfo_height(canvas))
        img = ImageGrab.grab(bbox=box)
        img.save("image_pavage/image_distribution{}.png".format(numero))



    temps = 0
    liste_cadre_chunk = chunk(liste_corps_cadre)
    liste_attractif_chunk = chunk(liste_corps_attractifs)
    while temps < temps_max :
        temps += 1
        if temps == 500 : photo()
        canvas.delete('all')
        print(temps)

        liste_repulsif_chunk = chunk(liste_corps_repulsifs)

        for k in range (len(liste_corps_repulsifs)) :

            corps1 = liste_corps_repulsifs[k]
            x,y = corps1.coord
            k,l = (int(x/50),int(y/50))


            #cadre(corps1)
            #repechage(corps1)

            for i in range (3):
                for j in range(3):
                    if k+i-1 >= 0 and k+i-1 < 16 and l+j-1 >= 0 and l+j-1 < 16 :

                        for corps2 in liste_repulsif_chunk[k+i-1][l+j-1]:
                            force_repulsive(corps1,corps2,q)

                        for corps3 in liste_attractif_chunk[k+i-1][l+j-1] :
                            force_attractive(corps1,corps3,g)

            frottements(corps1,alpha)
            if k >= 0 and k < 16 and l >= 0 and l < 16 :
                cadre_corps(corps1,liste_cadre_chunk[k][l])
            corps1.coord = addition_couple(corps1.coord,corps1.vitesse)

            x,y = corps1.coord
            r = corps1.rayon
            canvas.create_oval(x-r,y-r,x+r,y+r,fill ='blue')
           #canvas.create_oval((x-7*r),(y-7*r),(x+7*r),(y+7*r),outline = 'black')

        for corps in liste_corps_cadre :
            x,y = corps.coord
            r = corps.rayon
            canvas.create_oval(x-r,y-r,x+r,y+r,fill ='black')

        #canvas.create_oval(400,345,410,355,fill ='pink')

        for corps in liste_corps_attractifs :
            x,y = corps.coord
            r = corps.rayon
            canvas.create_oval(x-r,y-r,x+r,y+r,fill ='red')



        canvas.update()

    mainloop()
    return liste_coord_masse(liste_corps_repulsifs)


def decoupage(liste_corps):
    liste_chunk = []
    for k in range (16):
        liste_chunk.append([[] for i in range (16)])
    for corps in liste_corps :
        x,y = corps.coord
        k,l = (int(x/50) ,int(y/50))
        if k >= 0 and k < 16 and l >= 0 and l < 16 :
            liste_chunk[k][l].append(corps)
    return liste_chunk

def chunk(liste_corps):
    liste_chunk = []
    for k in range (16):
        liste_chunk.append([[] for i in range (16)])
    liste_decoupage = decoupage(liste_corps)
    for k in range(16) :
        for j in range (16):
            for x in range(3):
                for y in range(3):
                    if k+x-1 >= 0 and k+x-1 < 16 and j+y-1 >= 0 and j+y-1 < 16 :
                        liste_chunk[k][j] += (liste_decoupage[k+x-1][j+y-1])
    return liste_chunk
# on rassemble dans une seule liste tous les corps pris en compte dans les calculs d'un corps dans un chunk.




def photo_fin (temps_max,liste_corps_repulsifs,liste_corps_attractifs,g,q,alpha,liste_corps_cadre,numero):

    root = Tk()
    root.title = ('simulation gravité')
    canvas = Canvas( root, width = 700 , height = 700 , bg = 'white')
    canvas.grid(row=0,column=0)

    def photo():
        box = (Canvas.winfo_rootx(canvas),Canvas.winfo_rooty(canvas),Canvas.winfo_rootx(canvas)           +Canvas.winfo_width(canvas),Canvas.winfo_rooty(canvas) + Canvas.winfo_height(canvas))
        img = ImageGrab.grab(bbox=box)
        img.save("image_pavage/image_distribution{}.png".format(numero))

    liste_cadre_chunk = chunk(liste_corps_cadre)
    liste_attractif_chunk = chunk(liste_corps_attractifs)


    temps = 0
    while temps < temps_max :
        temps += 1
        canvas.delete('all')
        #print(temps)

        liste_repulsif_chunk = chunk(liste_corps_repulsifs)

        for k in range (len(liste_corps_repulsifs)) :

            corps1 = liste_corps_repulsifs[k]
            x,y = corps1.coord
            k,l = (int(x/50),int(y/50))

            frottements(corps1,alpha)
            #cadre(corps1)
            #repechage(corps1)

            if k >= 0 and k < 16 and l >= 0 and l < 16 :
                cadre_corps(corps1,liste_cadre_chunk[k][l])

                for corps2 in liste_repulsif_chunk[k][l]:
                    force_repulsive(corps1,corps2,q)

                for corps3 in liste_attractif_chunk[k][l] :
                    force_attractive(corps1,corps3,g)

            corps1.coord = addition_couple(corps1.coord,corps1.vitesse)

    for corps1 in liste_corps_repulsifs:
        x,y = corps1.coord
        r = corps1.rayon
        canvas.create_oval(x-r,y-r,x+r,y+r,fill ='blue')
        #canvas.create_oval((x-7*r),(y-7*r),(x+7*r),(y+7*r),outline = 'black')
    canvas.create_oval(345,345,355,355,fill ='black')
    for corps in liste_corps_attractifs :
            x,y = corps.coord
            r = corps.rayon
            canvas.create_oval(x-r,y-r,x+r,y+r,fill ='red')

    for corps in liste_corps_cadre :
            x,y = corps.coord
            r = corps.rayon
            canvas.create_oval(x-r,y-r,x+r,y+r,fill ='black')

    canvas.update()

    mainloop()
    photo()
    return liste_coord_masse(liste_corps_repulsifs)



test1_r = generateur_corps_repulsifs(2000)
test_peu = generateur_corps_repulsifs(250)
test1_a = generateur_corps_attractif(10)
test_bretagne = generateur_bretagne(7)
test_nord = generateur_nord(200)

carré_centre = generateur_corps_repulsifs(700)
bretagne = generateur_bretagne(70)
nord = generateur_nord(70)

repartition = carré_centre + bretagne + nord

ini = test_peu + test_bretagne



## etude equilibre

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import floor
from math import ceil
from scipy.ndimage.filters import gaussian_filter

def is_ok(x,y,r):
    n = 10*int(r)+1
    if x < 100+ n: return False
    if x >= 699 - n : return False
    if y < 100 + n : return False
    if y >= 699 - n: return False
    else : return True


def dessin(matrix,m,x,y,r):
    a = floor(x)
    b = floor(y)
    n = int(10*r)
    for i in range (2*n):
        for j in range (2*n):
            d = distance_couple((a,b),(a+i-n,b+j-n))
            if d <= n :
                if abs(a+i-n) < 700 and abs(b+j-n) < 700 :
                    matrix[-(b+j-n),(a+i-n)] += m



def liste_coord_masse(liste_corps):
    l_coord_masse = []
    for corps in liste_corps :
        l_coord_masse.append([corps.coord,corps.masse,corps.rayon])
    return l_coord_masse

def densite_hopital(temps_max,liste_corps_repulsifs,liste_corps_attractifs,g,q,alpha,liste_corps_cadre,numero):
    coord_masse_rep = animation(temps_max,liste_corps_repulsifs,liste_corps_attractifs,g,q,alpha,liste_corps_cadre,numero)

    dense = np.zeros((700,700))
    for corps in coord_masse_rep :
        x,y = corps[0]
        m = corps[1]
        r = corps[2]
        dessin(dense,m/10000,x,y,r)

    dense_smooth = gaussian_filter(dense,sigma=10)
    ax = sns.heatmap(dense_smooth)
    ax.invert_yaxis()
    ax.axis('equal')
    ax.figure.savefig("image_densite/densite_hopital_france{}".format(numero))
    plt.show()
    return dense_smooth

def densite_ville(liste_corps_attractifs,numero):

    coord_masse_att = liste_coord_masse(liste_corps_attractifs)

    dense = np.zeros((700,700))
    for corps in coord_masse_att :
        x,y = corps[0]
        m = corps[1]
        r = corps[2]
        if is_ok(x,y,r):
            dessin(dense,(m**(3/2)/(0.6*1000000)),y,-x,r)

    dense_smooth = gaussian_filter(dense,sigma=10)
    ax = sns.heatmap(dense_smooth)
    ax.invert_yaxis()
    ax.axis('equal')
    ax.figure.savefig("image_densite/densite_ville{}".format(numero))
    plt.show()
    return dense_smooth



def comparatif_densite (temps_max,liste_corps_repulsifs,liste_corps_attractifs,g,q,alpha,liste_corps_cadre,numero):

    d_hop = densite_hopital(temps_max,liste_corps_repulsifs,liste_corps_attractifs,g,q,alpha,liste_corps_cadre,numero)
    dville = densite_ville(liste_corps_attractifs,numero)
    score = comparaison_image(d_hop,dville)
    return score

def comparaison_image(im1,im2):
    s = 0
    for i in range(len(im1)):
        for j in range(len(im1[0])):
            s += abs ( im1[i][j] - im2[i][j])
    print("{} %".format(5*s/10000))






## recuperer contour france et convertir en cadre de corps

import matplotlib.image as mpimg

image = mpimg.imread("carte_france.png")

def is_noir(liste):
    rep = False
    for i in liste :
        if i != 1 : rep = True
    return rep

def is_bordure(couple,image):
    x,y = couple
    (a,b,c) = image.shape
    if x < 2 or x >= a-2 : return False
    if y < 2 or y >= b-2 : return False
    else  :
        for k in range(5):
            for l in range(5):
                if is_noir(image[x-k-2,y-l-2]) == False : return False
        return True



def contour_france(image):
    compteur= 0
    liste_coord = []
    (a,b,c) = image.shape
    for k in range (a):
        for l in range (b):
            if is_bordure((k,l),image) : liste_coord.append((k,l))
    return liste_coord

def min_max(liste):
    x,y = liste[0]
    minx = x
    maxx = x
    miny = y
    maxy = y
    for couple in liste :
        a,b = couple
        if a > maxx : maxx = a
        if a < minx : minx = a
        if b > maxy : maxy = b
        if b < miny : miny = b
    return (minx,maxx,miny,maxy)

def normaliser_contour(contour):
    minx,maxx,miny,maxy = min_max(contour)
    maxi = max(maxx-minx,maxy-miny)
    r = 700/maxi
    for k in range(len(contour)) :
        contour[k] = scalaire_couple ( addition_couple(contour[k],(-minx,-miny) ) , r )
    return contour


cadre_france = contour_france(image)
cadre_france_simplifié = cadre_france[::5]

def retourner(liste):
    for k in range (len(liste)):
        x,y = liste[k]
        liste[k] = y,x
    return liste

def scatter(liste_coord):
    for couple in liste_coord :
        x,y = couple
        plt.scatter(x,y,color='black')
    plt.axis('equal')
    plt.show()

def generer_cadre_corps (liste,masse):
    liste_corps = []
    for k in range (len(liste)):
        liste_corps.append(corps_repulsif(liste[k],(0,0),masse))
    return liste_corps

liste_corps_cadre_france = generer_cadre_corps(normaliser_contour(retourner(cadre_france)),1000)



## récuperer les villes de france et convertir en corps attractifs

def lecture_fichier(nom_fichier):
    f = open(nom_fichier,'r',encoding= 'utf-8')
    lignes = f.readlines()
    f.close()
    return lignes

def mise_en_forme(nom_fichier):
    liste = lecture_fichier(nom_fichier)
    res = []
    villes = []
    for ligne in liste :
        l = ligne.strip().split(",")
        if l[4] in liste_ville and l[4] not in villes:
            res.append([l[4],liste_pop_france[liste_ville.index(l[4])],l[6],l[7]])
            villes.append(l[4])
    return res

def recuperer_ville(nom_fichier):
    liste = mise_en_forme(nom_fichier)
    rep = []
    for ville in liste :
        if ville[0] not in ville_a_enlever :
            rep.append(ville)
    return rep

def coord_villes(liste_villes):
    rep = []
    for ville in liste_villes :
        x,y = float(ville[-2]),float(ville[-1])
        rep.append((x,y))
    return rep

def corriger_coord_villes(liste_villes):
    liste_coord = coord_villes(liste_villes)
    for k in range (len(liste_villes)) :
        x,y = liste_coord[k]
        liste_villes[k][-2],liste_villes[k][-1] = y,-x
    return liste_villes


def normaliser_coord_villes (liste_coord):
    minx,maxx,miny,maxy = min_max(liste_coord)
    maxi = max(maxx-minx,maxy-miny)
    r = 650/maxi
    for k in range(len(liste_coord)) :
        liste_coord[k] = scalaire_couple ( addition_couple(liste_coord[k],(-minx,-miny) ) , r )
        # on bricole pour que la geographie soit bonne
        x,y = liste_coord[k]
        liste_coord[k] = x,1.45*y
        liste_coord[k] = addition_couple( liste_coord[k] , (20,10 ))
    return liste_coord


def normaliser_villes(liste_villes):
    new_liste_coord = normaliser_coord_villes(coord_villes(corriger_coord_villes(liste_villes)))
    for k in range (len(liste_villes)) :
        x,y = new_liste_coord[k]
        liste_villes[k][-2],liste_villes[k][-1] = x,y
    return liste_villes


def villes_vers_corps(liste_ville):
    liste_corps = []
    for ville in liste_ville :
        liste_corps.append(corps_attractifs((ville[-2],ville[-1]),(0,0),5*ville[1]*0.0023279017178517935))
    return liste_corps


def scatter_ville(liste_cadre,liste_ville):
    for couple in liste_ville :
        x,y = couple
        plt.scatter(x,y,color='red')
    for couple in liste_cadre :
        x,y = couple
        plt.scatter(x,y,color='black')
    plt.axis('equal')
    plt.show()

# generer les hopitaux d'une autre maniere : en avoir un peu en bretagne des le depart ( le concentration que le reste de la france


## base de données villes

liste_ville = ["Paris","Marseille","Lyon","Toulouse","Nice","Nantes","Strasbourg","Montpellier","Bordeaux","Rennes","Le Havre","Reims","Lille","Saint-Etienne","Toulon","Angers","Brest","Grenoble","Dijon","Le Mans","Clermont-Ferrand","Amiens","Limoges","Aix-en-Provence","Nîmes","Tours","Saint-Denis","Metz","Villeurbanne","Besançon","Caen","Orléans","Mulhouse","Rouen","Perpignan","Boulogne-Billancourt","Nancy","Roubaix","Argenteuil","Fort-de-France","Tourcoing","Montreuil","Saint-Paul","Versailles","Avignon","Poitiers","Saint-Denis","Nanterre","Créteil","Pau","Aulnay-sous-Bois","La Rochelle","Vitry-sur-Seine","Calais","Colombes","Asnières-sur-Seine","Bourges","Rueil-Malmaison","Champigny-sur-Marne","Saint-Maur-des-Fossés","Antibes","Dunkerque","Béziers","Courbevoie","Saint-Pierre","Saint-Nazaire","Cannes","Colmar","Quimper","Valence","Villeneuve-d’Ascq","Aubervilliers","Mérignac","Les Abymes","Drancy","Troyes","Lorient","Le Tampon","Saint-Quentin","La Seyne-sur-Mer","Antony","Neuilly-sur-Seine","Niort","Noisy-le-Grand","Sarcelles","Charleville-Mézières","Chambéry","Beauvais","Pessac","Vénissieux","Cholet","Cergy","Levallois-Perret","Ajaccio","Vannes","Montauban","Laval","Evreux","Hyères","Issy-les-Moulineaux"]

liste_pop_france = [2147857,807071,453187,398423,345892,277728,267051,229055,218948,212494,193259,191325,191164,183522,166442,156327,156217,156203,153813,150605,141004,139210,137502,137067,137740,137046,132573,127498,127299,122308,117157,116559,112002,108758,107241,107042,105830,98039,95416,94778,94204,91146,88980,88476,88312,87012,86871,86219,82630,80610,80315,80055,79322,78170,77184,76314,76075,74671,74658,73613,73383,72333,71428,70105,69849,68616,68214,67163,67127,66568,65706,63524,63300,63290,62624,62612,61844,61258,61092,60968,60420,60364,59346,58460,58241,58092,57592,57355,56851,56487,56320,55162,54994,54697,54773,54421,54379,54076,53258,53152]

def somme(l):
    rep = 0
    for k in l :
        rep+= k
    return rep

ville_a_enlever = ["Fort-de-France","Ajaccio","Le Tampon","Saint-Denis","Saint-Paul","Saint-Pierre","Les Abymes"]

liste_villes_france = recuperer_ville("cities.csv")
liste_villes_france_normalisées = normaliser_villes(liste_villes_france)

liste_corps_ville_france = villes_vers_corps(liste_villes_france_normalisées)