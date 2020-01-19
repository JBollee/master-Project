# How long the time is to you ?

## Introduction

Cette expérience vise à explorer la capacité de sujets à tenir un rythme, ici celui des secondes, sans repère extérieur objectif et certains déterminants de la réussite à cette tâche: principalement la durée à tenir , l'entraînement et les retours sur performance, mais on explorera aussi les corrélations avec l'âge et la pratique de la musique . Elle ne s'appuie pas sur des acquis académiques en sciences cognitives, elle ne pourrait que constituer la première phase d'une série d'expériences sur cette capacité. 

Elle utilise des fonctions basiques du module expyriment dans Python.

L'expérience a deux variables indépendantes, donc quatre conditions, et chaque sujet en expérimente une seule. La première variable est la durée à décompter, la seconde est la présence ou l'absence de retours sur la performance. Les conditions sont attribuées au hasard à chaque sujet. Elle comporte une phase d'entraînement où les sujets peuvent décompter quinze secondes avec un décompte objectif sur l'ordinateur.
La tâche consiste à décompter mentalement une durée de trente ou soixante secondes et à appuyer sur une touche dès que le temps est, selon ce décompte, écoulé. Dans la condition avec retour, les sujets reçoivent ensuite des informations sur leur performance. La tâche est effectuée trois fois.  

 Table des matières:
 ```
 1- Création des stimuli textuels
 2- Questions, entraînement et randomisation des conditions
 3- Tâche et retours
 4- Perspectives
 5- Retours sur le cours
 ```
 ## Création et chargement des stimuli textuels
 
 Les sujets reçoivent un certain nombre d'instructions et certaines correspondent au début du décompte, il faut donc que leur apparition soit rapide. Elles sont chargées pour minimiser le délai de présentation.
 
 ```
 hello = expyriment.stimuli.TextScreen( heading ="Hello , welcome to"  , text= "How long the time is ?", text_size = 50, text_bold = True, text_italic= True, text_colour= (0,0, 255), heading_colour=(0, 255, 255), background_colour= (255,255,255) )

watch = expyriment.stimuli.TextBox(size = (300, 300) , text= "Remove your watch if you have one please and stay stil during the experiment", background_colour = (255,255,255), text_colour= (0,0, 255))

texts = [hello, pascal, watch...]

for item in texts:
	item.preload()

```
## Questions, entraînement et randomisation des conditions

On souhaite connaître l'âge et l'éventuelle pratique musicale des sujets, des facteurs pour lesquels on pourait établir des corrélations avec la performance. Pour l'âge j'utilise la fonction `expyriment.io.TextInput()` et pour la pratique musicale qui est une question fermée j'utilise deux touches du clavier :
```
age = expyriment.io.TextInput(message="How old are you please ?", message_text_size = 30, message_colour =(0, 255, 255), user_text_size = 20, user_text_colour = (255, 255, 0)).get()

data.append(age)

musician.present()
key, rt = exp.keyboard.wait()
data.append(key)
```

La phase d'entraînement vise à donner aux sujets la possibilité de suivre le rythme avec un référent extérieur. Le programme affiche à l'écran le nombre de secondes écoulées depuis le départ donné par la dernière frappe de touche. 
 ```
 exp.screen.clear()
for i in range(0,15):
    expyriment.stimuli.TextLine(text = str(i), text_size = 200).present()
    exp.clock.wait(1000)
```
 Il faut noter qu'utiliser le clavier peut occasionner des délais et une imprécision dans les temps de réponse de l'ordre de 20 ms, selon la [documentation expyriment](https://docs.expyriment.org/Timing.html). On le prendra en compte dans l'analyse des résultats.
 
J'utilise le module `random` pour assigner les conditions :
```
half_or_full = random.choice([0,1])
feedback = random.choice([0,1])
```
Et j'enregistre les conditions du sujet dans les données de l'expérience:

```
data = []
data.append(half_or_full)
data.append(feedback)
```
## Tâche

Le nombre d'essais déterminé en début d'expérience est exécuté par une boucle `for`. La tâche est exécutée selon les conditions par trois boucles `if` imbriquées portant sur les variables `half_or_full`, `feedback` et de nouveau `half_or_full`. 

```
for i in range(1,ntrials): #boucle condition de durée
    if (half_or_full == 0):
        ready30.present()
        
    else : ready60.present()
        
    exp.keyboard.wait()
    during_task.present()
    key, rt = exp.keyboard.wait()
    data.append(rt)

    #boucle condition de retour
    if (feedback == 1): 
        feedback_1.present(update = False)
	#deuxième boucle sur la durée
        if (half_or_full == 0):
            expyriment.stimuli.TextBox(size = (100, 100) , text = str((30000 - rt)* 0.001), position = (0, 0)).present(clear = False, update = False)
            if (30000 - rt > 0) :
                feedback_3.present(clear = False, update = False)
	
            else :
                feedback_2.present(clear = False, update = False)
				
        else :
            expyriment.stimuli.TextBox(size = (100, 100) , text = str((60000 - rt)*0.001), position = (0, 0)).present(clear = False, update = False)
             
            if (60000 - rt > 0) :
                feedback_3.present(clear = False, update = False)
                
            else :
                feedback_2.present(clear = False, update = False)
                
          feedback_4.present(clear = False)
          exp.keyboard.wait()
        
 ```
 On différencie le feedback selon si le sujet était en retard ou en avance sur l'horloge. Pour présenter les différents textes à l'écran il a fallu régler leurs positions relativement au centre de l'écran et faire en sorte qu'ils s'affichent tous en même temps par l'utilisation des arguments `clear` et `update`.
 
 ## Résultats et perspectives
 
 On obtient les temps de réponse pour chaque essai dans la condition dans laquelle était placé le sujet, sur un document par sujet. 
 
 J'aimerais améliorer cette expérience: 
 ..* en utilisant une technique de randomisation plus raffinée qui m'assure d'avoir un certain nombre de sujets pour chaque condition
 ..* en introduisant ensuite une phase d'analyse des données
 
 On pourrait, afin de faciliter le recueil de données, faire essayer à chacun des sujets les deux durées en utilisant le système de blocks d'expyriment et en randomisant l'ordre des deux conditions de temps. La variable de durée deviendrait alors "within-subjects".
 
 Enfin j'aimerais tester d'autres hypothèses, concernant la durée par exemple. On pourrait introduire des essais "sondes" c'est-à-dire des essais où le sujet devrait décompter un certain temps mais serait interrompu avant la fin de ce temps et interrogé sur la seconde à laquelle il se situait. Cela permettrait des estimations plus précises du moment où occure un décalage s'il s'en produit un. 
 
 ## Retours sur le cours
 
 ..* J'ai programmé pour la première fois de mon parcours cette année, je n'avais aucune expérience préalable.
 
 ..* Au cours de ces lectures j'ai pu apprendre à ouvrir un terminal et lui communiquer des instructions, sous la forme de fonctions. J'ai lu avec intérêt et appliqué les six premiers chapitres de *Automate the boring stuff with Python* et ai donc des notions sur les listes et les dictionnaires et les chemins vers les fichiers.  J'ai appris les bases des modules `expyriment` et `pygame` et ai appris à utiliser la documentation qui y était liée ainsi qu'à rechercher sur internet une partie de l'aide nécessaire à mon projet. 
 
 ..* J'aurais souhaité avoir accès à ce cours plus tard dans mon master et envisage d'ailleurs de le reprendre l'an prochain car j'ai l'impression de ne pas en avoir tiré assez d'enseignements car mes débuts étaient difficiles et lents. Le suivre en même temps que le cours de Datacamp où j'apprenais R était assez difficile et j'ai choisi de favoriser l'apprentissage de R au détriment de celui de Python dans la perspective de mon stage. Les débutants complets pourraient se voir conseiller plutôt de prendre seulement l'un des deux cours ou d'apprendre Python dans les deux.
