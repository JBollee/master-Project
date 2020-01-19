# How long the time is to you ?

## Introduction

Cette expérience vise à explorer la capacité de sujets à tenir un rythme, ici celui des secondes, sans repère extérieur objectif et certains déterminants de la réussite à cette tâche: principalement la durée à tenir , l'entraînement et les retours sur performance, mais on explorera aussi les corrélations avec l'âge et la pratique de la musique . Elle ne s'appuie pas sur des acquis académiques en sciences cognitives, elle ne pourrait que constituer la première phase d'une série d'expériences sur cette capacité. 

Elle utilise des fonctions basiques du module expyriment dans Python.

L'expérience a deux variables indépendantes, donc quatre conditions, et chaque sujet en expérimente une seule. La première variable est la durée à décompter, la seconde est la présence ou l'absence de retours sur la performance. Les conditions sont attribuées au hasard à chaque sujet. Elle comporte une phase d'entraînement où les sujets peuvent décompter quinze secondes avec un décompte objectif sur l'ordinateur.
La tâche consiste à décompter mentalement une durée de trente ou soixante secondes et à appuyer sur une touche dès que le temps est, selon ce décompte, écoulé. Dans la condition avec retour, les sujets reçoivent ensuite des informations sur leur performance. La tâche est effectuée trois fois.  

 Table des matières:
 ```
 1- Création des stimuli textuels
 2- Entraînement et randomisation des conditions
 3- Tâche
 4- Retours
 5- Perspective
 6- Retours sur le cours
 ```
 ## Création et chargement des stimuli textuels
 
 Les sujets reçoivent un certain nombre d'instructions et certaines correspondent au début du décompte, il faut donc que leur apparition soit rapide. Elles sont chargées pour minimiser le délai de présentation.
 
 ```
 hello = expyriment.stimuli.TextScreen( heading ="Hello , welcome to"  , text= "How long the time is ?", text_size = 50, text_bold = True, text_italic= True, text_colour= (0,0, 255), heading_colour=(0, 255, 255), background_colour= (255,255,255) )
hello.preload()

watch = expyriment.stimuli.TextBox(size = (300, 300) , text= "Remove your watch if you have one please and stay stil during the experiment", background_colour = (255,255,255), text_colour= (0,0, 255))
watch.preload()

```
## Entraînement et randomisation des conditions

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
Et j'enregistre les conditions du sujet dans 
#Code to be written, step by step
 
 Before first step: -Open the file “Results.csv”, write first line “Number; Name; Time discounted; Feedback; Time_1; First_RT; Time_2; Second_RT ; Time_3 ; Third_RT ” 

1. Step 1 (optional): 
Greeting the participant

2. Step 2 (Preparation): 
- Telling them to remove their watch if they have one (and click when they have finished)
-	Telling them what they’ll have to do: discount in their minds one minute, half a minute or 15 seconds and click when they’re done (ie as soon as they think time is over). Tell them to click if they have understood.
-	Tell them the computer is going to count fifteen seconds with them to train them. Tell them to click when they want to start training

3. Step 3 (Training): 
- Display a clock/numbers of seconds during 15 seconds – 
-	Ask them to click whenever they want to start the task

4. Step 4 (randomizing the the feedback) : 
- add a line to the csv file 
-	Sort a number (0 or 1), name this variable “Feedback” and write it to the csv file

5. Step 5.1 (randomizing the amount of time discounted for 1st task): 
- [Sort a number (30 or 60),] name this variable “time_1” and write it to the csv file

 Step 5.2 (1st Task): 
-[Display a black screen during three seconds. Display “When you want the “time”seconds to start, press a tab”
-	From the moment the participant presses, count the time 
-	Stop counting when the participant presses another tab]- Time is named RT1
-	Write in the csv file: “; RT1” 
#IF Feedback == 1, Step 5.3- (OPTIONNAL- Feedback): 
[- If RT1>time, display “You were (RT1-time) seconds late, well tried!”
-	If RT1<time, display “You were (time-RT1) seconds early, well tried!”
-	If abs(RT1-time) <2, display “Bravo !”
-	Ask to click whenever they want to start again]

6. ELSE Step 6.1:  
cf step 5.1 […] part (I shall make it a function) name this variable “time_2” and write it to the csv file 
 
  6.2: (2nd task): 
 Cf 5.2, […] part (I shall make it a function)
-	- Time is named RT2
-	Write in the csv file: “; RT2”
IF Feedback = 1, Step 6.3 (OPTIONNAL- Feedback): cf 5.3, […] will be made a function and applied to RT2

7. Step 7.1: 
cf step 5.1 […]  part (I shall make it a function) name this variable “time_3” and write it to the csv file 

Step 7.2 (3rd task): Cf 5.2, […]  part (I shall make it a function)
- Time is named RT3 -Write in the csv file: “; RT3”
 IF Feedback = 1, Step 7.3 (OPTIONNAL- Feedback): cf 5.3, […]  part will be made a function and applied to RT2

8. Step 8 (End the task) - Ask to click when they want to end the task and see their results
- Display a screen with their three results : “You were first (if RT1>time display “(RT1-time_1) seconds late”, if not display “(time_1-RT1) seconds early”) then …”
-	Then display “thanks”
-	And close the csv file.
9. Step 9 (Retour au début ou fin): - Back to step 1
-	Add a special tab to press to end the collection of data and close the csv file
