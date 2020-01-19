# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:17:43 2020

@author: Lenovo
"""

import random
import expyriment

exp = expyriment.design.Experiment(name="How long the time is ?")

expyriment.control.initialize(exp)
expyriment.io.Screen(colour = (0, 0, 0), window_mode = 0, open_gl = 1, no_frame = True, window_size = 0)

#Paramètre du nombre d'essais
ntrials = 3

exp.add_data_variable_names(['age', 'music', 'Duration', 'Feedback', 'RT', 'RT', 'RT'])

# Préparer et charger les stimuli textuels
hello = expyriment.stimuli.TextScreen( heading ="Hello , welcome to"  , text= "How long the time is ?", text_size = 50, text_bold = True, text_italic= True, text_colour= (0,0, 255), heading_colour=(0, 0, 255), background_colour= (255,255,255) )

pascal = expyriment.stimuli.TextScreen(heading = "Les Pensées, Blaise Pascal", text = "L’un dit : il y a deux heures ; l’autre dit : il n’y a que trois quarts d’heure. Je regarde ma montre et je dis à l’un : vous vous ennuyez, et à l’autre : le temps ne vous dure guère, car il y a une heure et demie. Et je me moque de ceux qui disent que le temps me dure à moi et que j ’en juge par fantaisie. Ils ne savent pas que j ’en juge par ma montre.", text_italic= True, background_colour = (255,255,255), text_colour= (0,0, 0), heading_colour=(0, 100, 0), text_size = 30, text_justification= True)

watch = expyriment.stimuli.TextBox(size = (400, 200) , text= "Remove your watch if you have one please and stay still during the experiment", background_colour = (255,255,255), text_colour= (0,0, 255), text_size = 40)

task = expyriment.stimuli.TextBox(size = (500, 400) , text="You'll have to discount mentally a certain amount of time and press a key as soon as you're done. Simple isn't it ? \n Press a key if you're all set, you'll start training",text_size = 30, text_justification= True, background_colour = (255,255,255), text_colour= (0,0, 255) )

training = expyriment.stimuli.TextBox(text_size = 40, size = (500, 500) , text="Now the screen will discount 15 seconds to train you. \n Whenever you're ready to start, press a tab", background_colour = (255,255,255), text_colour= (0,0, 255))

ready30 = expyriment.stimuli.TextBox(size = (500, 500) , text="Press a tab when you're ready to start counting 30 seconds", text_colour=(0, 255, 255))

ready60 = expyriment.stimuli.TextBox(size = (500, 500) , text="Press a tab when you're ready to start counting 60 seconds", text_colour=(0, 255, 255))

during_task = expyriment.stimuli.TextBox(size = (500, 500) , text="Time goes by...", text_size = 50, text_bold = True, text_colour = (255, 255, 255), position = (0,0))

feedback_1 = expyriment.stimuli.TextBox(size = (100, 100) , text= "You were", position = (-100, 100))
feedback_2 = expyriment.stimuli.TextBox(size = (200, 200) , text= "late", position = (100, -100))
feedback_3 = expyriment.stimuli.TextBox(size = (200, 200) , text= "seconds early", position = (100, -100))
feedback_4 = expyriment.stimuli.TextBox(size = (200, 200) , text= "Well tried !", position = (0, -200))

musician = expyriment.stimuli.TextBox(size = (500, 500) , text="Do you play music or sing ? \n Please press Y for yes and N for no",text_size = 30, text_colour= (0,0, 255) )

thanks = expyriment.stimuli.TextBox(size = (500, 150) , text="Thanks !",text_size = 50, text_bold = True, background_colour = (255,255,255), text_colour= (0,0, 255) )

#Charger tous les textes

texts = [hello, pascal, watch, task, training , ready30, ready60, during_task, musician, thanks, feedback_1, feedback_2, feedback_3, feedback_4]

for item in texts:
	item.preload()


expyriment.control.start(skip_ready_screen=True)
exp.screen.clear()

for i in range(5): 
	texts[i].present()
	exp.keyboard.wait()

#Commencer l'entraînement
exp.screen.clear()
for i in range(0,16):
    expyriment.stimuli.TextLine(text = str(i), text_size = 200).present()
    exp.clock.wait(1000)

#Récolter des données complémentaires
data = []
age = expyriment.io.TextInput(message="How old are you please ?", message_text_size = 30, message_colour =(0, 255, 255), user_text_size = 20, user_text_colour = (255, 255, 0)).get()
data.append(age)

musician.present()
key, rt = exp.keyboard.wait()
data.append(key)

#Assigner les conditions
half_or_full = random.choice([0,1])
feedback = random.choice([0,1])

data.append(half_or_full)
data.append(feedback)

#Commencer les tâches: 
for i in range(0,ntrials): #boucle condition de durée
    if (half_or_full == 0):
        ready30.present()
        
    else : ready60.present()
        
    exp.keyboard.wait()
    during_task.present()
    key, rt = exp.keyboard.wait()
    data.append(rt)

    if (feedback == 1): #boucle condition de condition de feedback
        feedback_1.present(update = False)
        if (half_or_full == 0):#deuxième boucle de condition de durée
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


exp.data.add(data)

#End the experiment
thanks.present()
exp.clock.wait(2000)
expyriment.control.end()
quit
print(data)
