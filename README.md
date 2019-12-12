
 My project’s name is “How long the time is” and it aims to assess how regular or precise people can keep in counting seconds, whether it is influenced by the amount of seconds discounted and whether feedback helps them improve or not. 

# Experimental design: 
2x2 conditions, randomization of the time condition to avoid order effects (but for a further refinement I could choose another method of randomization) and random assignation of the feedback condition. 

For now I have written a resume of my steps but I haven’t set the if loop required to make feedback optional.

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
