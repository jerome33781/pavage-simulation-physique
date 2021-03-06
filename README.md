# pavage-simulation-physique
Utilisation d'une simulation de forces électrostatiques pour résoudre un problème de pavage

On se place dans cette étude dans le cadre de la France et l'on cherche à optimiser la répartition d'hôpitaux sur le territoire. L'idée est d'utiliser la répulsion et l'attraction électrostatique, en considérant les hôpitaux comme des électrons et les villes comme des protons, pour que la répartition assure un service au plus grand nombre.   

## I. Simulation physique 

On met tout d'abord en place les différents corps intervenant dans l'étude et les forces qu'ils les lient.   
On se place dans l'approximation d'Euler : le système est immobile entre t et t+dt. J'ai utilisé premièrement des graphes matplotlib mis bout à bout puis le module tkinter pour implémenter l'animation de la simulation.  
Les points bleus seront des hopitaux, les rouges les villes et en noir le contour.  

premier test de la simulation physique :  
![anim 2](https://user-images.githubusercontent.com/83364235/173251261-aeb90e93-2886-46c6-8052-7cdac8a67390.gif)    

premier test d'un pavage dans un carré avec quelques villes :  
![pavage m=cste=1000](https://user-images.githubusercontent.com/83364235/173251327-e2976ad6-e422-4e42-994b-e80608c17f03.png)  

On se place dans le cadre du territoire français, ainsi j'ai récupéré les coordonnées gps des 100 plus grandes villes francaises et leur population, de sorte à les placer sur la carte en tant que point attracteur. J'ai récupéré via une image du térritoire le contour de la France, de sorte à définir les bordures de l'espace.   

On lance ainsi dans un premier temps la simulation sans points attracteur pour avoir une répartition initial uniforme, puis on rajoute les points attracteurs. On obtient une carte de la france de ce type. On remarque d'ailleurs que certains points sortent de la carte, cela s'explique par l'approximation d'Euler et le caractère divergent des forces lorsque les points se rapprochent.    

étape 1 : distribution uniforme   

![github unif](https://user-images.githubusercontent.com/83364235/173351483-c0307bbd-b7f9-4598-acde-888cfe7fc41d.PNG)    
 
étape 2 : pavage final   
![github pavage](https://user-images.githubusercontent.com/83364235/173351616-36b20121-8dc0-4291-b780-fd6b0c5f0244.PNG)  





De sorte à améliorer la compléxité de la simulation et d'avoir quelque chose de fluide, on peut définir l'espace comme une grille à 2 dimensions,et dire que les forces étant en 1/distance^2, les particules étant dans des cases ayant une distance de Hamming supérieure à 1 n'agissent pas l'une sur l'autre. On évite alors énormément de vérification de proximité avec la bordure, et moins de forces négligeable dues à des particules éloignées.

## II. Evaluation d'un pavage

Pour évaluer un pavage on pourrait calculer sa couvrance et pour cela considérer la surface de la France ramenée à l'échelle et la surface qu'occupent les zones d'activité des hôpitaux au sein du territoire. 
Une seconde façon d'évaluer le pavage est liée à la densité de population et de service. C'est cette méthode que j'ai décidé d'approfondir. On définit à partir des cent villes une carte de densité de la population :  

![densite_ville7](https://user-images.githubusercontent.com/83364235/173251762-b0a91309-b47a-4eff-9ba2-d9f31e8b75a2.png)

Puis on applique l'algorithme, et on en déduit une carte de densité des hopitaux :  

![densite_hopital_france6](https://user-images.githubusercontent.com/83364235/173251966-c6290e4d-5148-40fd-aca9-e0c8334ce61f.png)

En ramenant les intensités des cartes au même niveau, on peut alors comparer la différences des deux images et donc évaluer la qualité du pavage. 


## Remarque finale 

On pourrait plutôt que de trouver le meilleur pavage, effectuer une analyse prenant en compte un pavage déjà existant et cherchant les meilleurs nouveaux emplacements. Ainsi, connaissant les hopitaux français, on pourrait en déduire où placer le prochain hopital pour un pavage optimal. 



