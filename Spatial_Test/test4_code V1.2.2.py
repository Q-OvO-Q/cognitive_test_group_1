import json 
import time
import requests
import numpy as np
import pandas as pd
import ipywidgets as widgets
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from jupyter_ui_poll import ui_events
from IPython.display import display, Image, clear_output, HTML


from test4_function import *



# Welcome
myhtml_w1 = HTML("<h1>Welcome to the Spatial Resoning Test (SRT).</h1>")
display (myhtml_w1)
time.sleep(1)
myhtml_w2 = HTML ('<h2>Please enter your group number, gender and anonymised ID to continue the test.</h2>')
display (myhtml_w2)
time.sleep(1)

#group number
print ("Please enter your group number (number only)")
group_number = input('>')
print("User entered group number:", group_number)
time.sleep(0.5)

#anoymised ID
id_instructions = """

Enter your anonymised ID

To generate an anonymous 4-letter unique user identifier please enter:
- two letters based on the initials (first and last name) of a childhood friend
- two letters based on the initials (first and last name) of a favourite actor / actress

e.g. if your friend was called Charlie Brown and film star was Tom Cruise
     then your unique identifier would be CBTC
"""

print(id_instructions)
user_id = input("> ")

print("User entered id:", user_id)



    
    
    
#data consent
myhtml_data1 = HTML("<h1>DATA CONSENT INFORMATION:</h1>")
display(myhtml_data1)

data_consent_info = """


Please read:

We wish to record your response data
to an anonymised public data repository. 
Your data will be used for educational teaching purposes
practising data analysis and visualisation."""
print(data_consent_info)

myhtml_data1 = HTML('<h3>Please type   "yes"   in the box below if you consent to the upload.</h3>')
display(myhtml_data1)

result = input("> ") 

if result == "yes": 
    print("Thanks for your participation.")
    print("Please contact a.fedorec@ucl.ac.uk")
    print("If you have any questions or concerns")
    print("regarding the stored results.")
    
else: 
    # end code execution by raising an exception
    raise(Exception("User did not consent to continue test."))
    
    

    
#gender
gender_instruction = """


Please choose your physiological gender.
"""

print (gender_instruction)
btnM = widgets.Button(description="Male")
btnF = widgets.Button(description="Female")

btnM.on_click(register_event)
btnF.on_click(register_event)

panel = widgets.HBox([btnM, btnF])
display (panel)

result = wait_for_event()

if result["description"]=="Male":
    print ("User chose Male")
    gender = "Male"
else:
    print ("User chose Female")
    gender = "Female"
    
time.sleep(2)
clear_output()
    
myhtml_data2 = HTML("<h1>Now, please be prepared for the 8 SRT questions and get started.</h1>")
display(myhtml_data2)

time.sleep(4)
clear_output()
 





    

    
#Question 1

#Scoring System 
score = 0

#Welcome
myhtml_11 = HTML("<h1>Spatial Resoning Test (SRT) Question 1</h1>")
display(myhtml_11)
time.sleep(1)
myhtml_x2 = HTML("<h2>Please observe the following 3D cubes and the 2D projections.</h2>")
display(myhtml_x2)
time.sleep(1)

# Q1 cubes drawing

# define a 5 x 5 x 5 cube space

# to draw a cube in the space
# we set the entry to a colour

# allowed colours:
#
# r - red,     g - green, b - blue, 
# m - magenta, c - cyan,  y - yellow
# k - black,   w - white

# define 3d 5x5x5 string array with entries set to '' 
cubes1 = np.full((5,5,5),'')

# construct cube arrangement 
# by inserting color codes into 3D array

# specify colours for specific cubes
cubes1[0,0,0:5] = 'r' 
cubes1[1,0,0] = 'g'
cubes1[0,1,0] = 'b'
cubes1[1,1,0] = 'y'

# draw the result
draw_cubes(cubes1)


#draw projections
draw_cubes(cubes1, view='-xy')# draw the view from bottom in XY plane
print ("A")
draw_cubes(cubes1, view='xz')# draw the side view in XZ direction
print ("B")
draw_cubes(cubes1, view='yz')# draw the side view in YZ direction
print ("C")
draw_cubes(cubes1, flip='z', view='xy')# display the projection obtained from the flipped arrangement.
print ("D")
start_time_q1=time.time()

#buttons 
myhtml_x3 = HTML("<h2>Please choose the 2D projection that CANNOT be obtained by rotating the 3D cubes in space.</h2>")
display(myhtml_x3)

btnA = widgets.Button(description="A")
btnB = widgets.Button(description="B")
btnC = widgets.Button(description="C")
btnD = widgets.Button(description="D")

btnA.on_click(register_event) 
btnB.on_click(register_event) 
btnC.on_click(register_event) 
btnD.on_click(register_event) 

panel = widgets.HBox([btnA, btnB, btnC, btnD])
display (panel)

result = wait_for_event()
clear_output()

#interaction with user 
myhtml_x4 = HTML("<h2>Correct!</h2>")
myhtml_15 = HTML("<h2>Sorry! The correct answer is A.</h2>")

    
if result['description']=="A":
    display (myhtml_x4)
    score = score + 1 
    q1_mark = 1
else:
    display (myhtml_15)
    q1_mark = 0

#save answer
if result['description']=="A":
    q1_ans="A"
elif result['description']=="B":
    q1_ans="B"
elif result['description']=="C":
    q1_ans="C"
elif result['description']=="D":
    q1_ans="D"

#time used
end_time_q1=time.time()
time_taken_q1=end_time_q1 - start_time_q1
print (f"You took {time_taken_q1:.2f} seconds.")
time.sleep(2)
clear_output()








#Question 2

#Welcome
myhtml_21 = HTML("<h1>Spatial Resoning Test (SRT) Question 2</h1>")
display(myhtml_21)
time.sleep(1)
display(myhtml_x2)
time.sleep(1)


#Q2 cubes drawing
# define 3d 5x5x5 string array with entries set to '' 
cubes2 = np.full((5,5,5),'')

# construct cube arrangement 
# by inserting color codes into 3D array

# specify colours for specific cubes
cubes2[0:3,0,0] = 'r' #  use slice indexing to fill blocks x=0,1,2        y=0  z=0 
cubes2[0:6,1,0] = 'g' #  use slice indexing to fill blocks x=0,1,2,3,4,5  y=0  z=0 

# draw the result
draw_cubes(cubes2)

#draw projections
draw_cubes(cubes2, view='xy')# draw the view from bottom in XY plane
print("A")
draw_cubes(cubes2, flip='x', view='xz')# display the projection obtained from the flipped arrangement.
print("B")
draw_cubes(cubes2, view='-xy')# draw the side view in -xy direction
print("C")
draw_cubes(cubes2, view='yz')# draw the side view in YZ direction
print("D")
start_time_q2=time.time()

#buttons 
display(myhtml_x3)

btnA = widgets.Button(description="A")
btnB = widgets.Button(description="B")
btnC = widgets.Button(description="C")
btnD = widgets.Button(description="D")

btnA.on_click(register_event) 
btnB.on_click(register_event) 
btnC.on_click(register_event) 
btnD.on_click(register_event) 

panel = widgets.HBox([btnA, btnB, btnC, btnD])
display (panel)

result = wait_for_event()
clear_output()

#interaction with user 
myhtml_15 = HTML("<h2>Sorry! The correct answer is B.</h2>")
 
if result['description']=="B":
    display (myhtml_x4)
    score = score + 1 
    q2_mark = 1
else:
    display (myhtml_15)
    q2_mark = 0

#save answer
if result['description']=="A":
    q2_ans="A"
elif result['description']=="B":
    q2_ans="B"
elif result['description']=="C":
    q2_ans="C"
elif result['description']=="D":
    q2_ans="D"


end_time_q2=time.time()
time_taken_q2=end_time_q2 - start_time_q2
print (f"You took {time_taken_q2:.2f} seconds.")
time.sleep(2)
clear_output()








#Question 3

#Welcome
myhtml_31 = HTML("<h1>Spatial Resoning Test (SRT) Question 3</h1>")
display(myhtml_31)
time.sleep(1)
display(myhtml_x2)
time.sleep(1)


# Q3 cubes drawing

# define 3d 5x5x5 string array with entries set to '' 
cubes3 = np.full((5,5,5),'')

# construct cube arrangement 
# by inserting color codes into 3D array

cubes3[0:3,0,0] = 'r' 
cubes3[3,1:3,0] = 'g' 
cubes3[1:3,1:3,0:2] = 'b' 
cubes3[3,0,0] = 'm'
cubes3[1,2,2] = 'y'

# draw the result
draw_cubes(cubes3)

#draw projections
draw_cubes(cubes3, view='xz')# draw the side view in XZ direction
print("A")
draw_cubes(cubes3, view='yz')# draw the side view in YZ direction
print("B")
draw_cubes(cubes3, view='-yz')# draw the side view in -YZ direction (other side)
print("D")
draw_cubes(cubes3, view='-xy')# draw the view from bottom in XY plane
print("D")
start_time_q3=time.time()

#buttons 
display(myhtml_x3)

btnA = widgets.Button(description="A")
btnB = widgets.Button(description="B")
btnC = widgets.Button(description="C")
btnD = widgets.Button(description="D")

btnA.on_click(register_event) 
btnB.on_click(register_event) 
btnC.on_click(register_event) 
btnD.on_click(register_event) 

panel = widgets.HBox([btnA, btnB, btnC, btnD])
display (panel)

result = wait_for_event()
clear_output()

#interaction with user 
myhtml_35 = HTML("<h2>Sorry! The correct answer is C.</h2>")
 
if result['description']=="C":
    display (myhtml_x4)
    score = score + 1 
    q3_mark = 1
else:
    display (myhtml_35)
    q3_mark = 0

    
#save answer
if result['description']=="A":
    q3_ans="A"
elif result['description']=="B":
    q3_ans="B"
elif result['description']=="C":
    q3_ans="C"
elif result['description']=="D":
    q3_ans="D"

end_time_q3=time.time()
time_taken_q3=end_time_q3 - start_time_q3
print (f"You took {time_taken_q3:.2f} seconds.")
time.sleep(2)
clear_output()








#Question 4

#Welcome
myhtml_41 = HTML("<h1>Spatial Resoning Test (SRT) Question 4</h1>")
display(myhtml_41)
time.sleep(1)
display(myhtml_x2)
time.sleep(1)

# Q4 cubes drawing
cubes4= np.full((5,5,5),'')
#inserting coulours
cubes4[1:4,2,3] = 'r' 
cubes4[0,3,4] = 'g' 
cubes4[3:4,1:3,3] = 'b' 
cubes4[3,0,0] = 'm'
cubes4[4,3,3] = 'y'

# draw the result
draw_cubes(cubes4)


#draw projections
draw_cubes(cubes4, view='-xy')# draw the view from bottom in XY plane
print("A")
draw_cubes(cubes4, view='-yz')# draw the side view in -YZ direction (other side)
print("B")
draw_cubes(cubes4, view='xz')# draw the side view in XZ direction
print("C")
draw_cubes(cubes4, view='yz')# draw the side view in YZ direction
print("D")
start_time_q4=time.time()

#buttons 
display(myhtml_x3)

btnA = widgets.Button(description="A")
btnB = widgets.Button(description="B")
btnC = widgets.Button(description="C")
btnD = widgets.Button(description="D")

btnA.on_click(register_event) 
btnB.on_click(register_event) 
btnC.on_click(register_event) 
btnD.on_click(register_event) 

panel = widgets.HBox([btnA, btnB, btnC, btnD])
display (panel)

result = wait_for_event()
clear_output()

#interaction with user 
myhtml_45 = HTML("<h2>Sorry! The correct answer is B.</h2>")
 
if result['description']=="B":
    display (myhtml_x4)
    score = score + 1 
    q4_mark = 1
else:
    display (myhtml_45)
    q4_mark = 0

#save answer
if result['description']=="A":
    q4_ans="A"
elif result['description']=="B":
    q4_ans="B"
elif result['description']=="C":
    q4_ans="C"
elif result['description']=="D":
    q4_ans="D"

end_time_q4=time.time()
time_taken_q4=end_time_q4 - start_time_q4
print (f"You took {time_taken_q4:.2f} seconds.")
time.sleep(2)
clear_output()









# Question 5

#Welcome
myhtml_51 = HTML("<h1>Spatial Resoning Test (SRT) Question 5</h1>")
display(myhtml_51)
time.sleep(1)
display(myhtml_x2)
time.sleep(1)

# Q5 cubes drawing
cubes5= np.full((5,5,5),'')
cubes5[4,3,2:4] = 'r' 
cubes5[2:3,0,0:2] = 'g' 
cubes5[2,1:2,2:3] = 'b' 
draw_cubes(cubes5)

#draw projections
draw_cubes(cubes5, view='-yz')
print("A")
draw_cubes(cubes5, view='xy')
print("B")
draw_cubes(cubes5, view='yz')
print("C")
draw_cubes(cubes5, view='xz')
print("D")
start_time_q5=time.time()

#buttons 
display(myhtml_x3)

btnA = widgets.Button(description="A")
btnB = widgets.Button(description="B")
btnC = widgets.Button(description="C")
btnD = widgets.Button(description="D")

btnA.on_click(register_event) 
btnB.on_click(register_event) 
btnC.on_click(register_event) 
btnD.on_click(register_event) 

panel = widgets.HBox([btnA, btnB, btnC, btnD])
display (panel)

result = wait_for_event()
clear_output()

#interaction with user 
myhtml_55 = HTML("<h2>Sorry! The correct answer is A.</h2>")
 
if result['description']=="A":
    display (myhtml_x4)
    score = score + 1 
    q5_mark = 1
else:
    display (myhtml_55)
    q5_mark = 0

#save answer
if result['description']=="A":
    q5_ans="A"
elif result['description']=="B":
    q5_ans="B"
elif result['description']=="C":
    q5_ans="C"
elif result['description']=="D":
    q5_ans="D"


end_time_q5=time.time()
time_taken_q5=end_time_q5 - start_time_q5
print (f"You took {time_taken_q5:.2f} seconds.")
time.sleep(2)
clear_output()








# Question 6

#Welcome
myhtml_61 = HTML("<h1>Spatial Resoning Test (SRT) Question 6</h1>")
display(myhtml_61)
time.sleep(1)
display(myhtml_x2)
time.sleep(1)

# Q6 cubes drawing
cubes6= np.full((5,5,5),'')
cubes6[4,0:3,3] = 'r' 
cubes6[0,0:3,1] = 'g' 
cubes6[2,0:3,4] = 'b' 
cubes6[1,0:3,0] = 'y'
draw_cubes(cubes6)

#draw projections
draw_cubes(cubes6, view='xy')
print("A")
draw_cubes(cubes6, view='yz')
print("B")
draw_cubes(cubes6, view='xz')
print("C")
draw_cubes(cubes6, view='-xz')
print("D")
start_time_q6=time.time()

#buttons 
display(myhtml_x3)

btnA = widgets.Button(description="A")
btnB = widgets.Button(description="B")
btnC = widgets.Button(description="C")
btnD = widgets.Button(description="D")

btnA.on_click(register_event) 
btnB.on_click(register_event) 
btnC.on_click(register_event) 
btnD.on_click(register_event) 

panel = widgets.HBox([btnA, btnB, btnC, btnD])
display (panel)

result = wait_for_event()
clear_output()

#interaction with user 
myhtml_65 = HTML("<h2>Sorry! The correct answer is D.</h2>")
 
if result['description']=="D":
    display (myhtml_x4)
    score = score + 1 
    q6_mark = 1
else:
    display (myhtml_65)
    q6_mark = 0
    
#save answer
if result['description']=="A":
    q6_ans="A"
elif result['description']=="B":
    q6_ans="B"
elif result['description']=="C":
    q6_ans="C"
elif result['description']=="D":
    q6_ans="D"

end_time_q6=time.time()
time_taken_q6=end_time_q6 - start_time_q6
print (f"You took {time_taken_q6:.2f} seconds.")
time.sleep(2)
clear_output()








# Question 7

#Welcome
myhtml_71 = HTML("<h1>Spatial Resoning Test (SRT) Question 7</h1>")
display(myhtml_71)
time.sleep(1)
display(myhtml_x2)
time.sleep(1)

# Q7 cubes drawing
cubes7= np.full((5,5,5),'')
cubes7[1,0:4,3] = 'g' 
cubes7[2,0:4,4] = 'b' 
cubes7[3,0:4,3] = 'm'
cubes7[4,0:4,2] = 'y'
draw_cubes(cubes7)

#draw projections
draw_cubes(cubes7, view='xy')
print("A")
draw_cubes(cubes7, view='-yz')
print("B")
draw_cubes(cubes7, view='xz')
print("C")
draw_cubes(cubes7, view='yz')
print("D")
start_time_q7=time.time()

#buttons 
display(myhtml_x3)

btnA = widgets.Button(description="A")
btnB = widgets.Button(description="B")
btnC = widgets.Button(description="C")
btnD = widgets.Button(description="D")

btnA.on_click(register_event) 
btnB.on_click(register_event) 
btnC.on_click(register_event) 
btnD.on_click(register_event) 

panel = widgets.HBox([btnA, btnB, btnC, btnD])
display (panel)

result = wait_for_event()
clear_output()

#interaction with user 
myhtml_75 = HTML("<h2>Sorry! The correct answer is B.</h2>")
 
if result['description']=="B":
    display (myhtml_x4)
    score = score + 1 
    q7_mark = 1
else:
    display (myhtml_75)
    q7_mark = 0
    
#save answer
if result['description']=="A":
    q7_ans="A"
elif result['description']=="B":
    q7_ans="B"
elif result['description']=="C":
    q7_ans="C"
elif result['description']=="D":
    q7_ans="D"

end_time_q7=time.time()
time_taken_q7=end_time_q7 - start_time_q7
print (f"You took {time_taken_q7:.2f} seconds.")
time.sleep(2)
clear_output()







# Question 8

#Welcome
myhtml_81 = HTML("<h1>Spatial Resoning Test (SRT) Question 8</h1>")
display(myhtml_81)
time.sleep(1)
display(myhtml_x2)
time.sleep(1)

# Q8 cubes drawing
cubes8= np.full((5,5,5),'')
cubes8[0:2,0:4,1] = 'g' 
cubes8[0:2,0:4,3] = 'm'
cubes8[0:2,0:4,2] = 'y'
draw_cubes(cubes8)

#draw projections
draw_cubes(cubes8, view='-xy')
print("A")
draw_cubes(cubes8, view='xy')
print("B")
draw_cubes(cubes8, view='yz')
print("C")
draw_cubes(cubes8, view='xz')
print("D")
start_time_q8=time.time()

#buttons 
display(myhtml_x3)

btnA = widgets.Button(description="A")
btnB = widgets.Button(description="B")
btnC = widgets.Button(description="C")
btnD = widgets.Button(description="D")

btnA.on_click(register_event) 
btnB.on_click(register_event) 
btnC.on_click(register_event) 
btnD.on_click(register_event) 

panel = widgets.HBox([btnA, btnB, btnC, btnD])
display (panel)

result = wait_for_event()
clear_output()

#interaction with user 
myhtml_85 = HTML("<h2>Sorry! The correct answer is A.</h2>")
 
if result['description']=="A":
    display (myhtml_x4)
    score = score + 1 
    q8_mark = 1
else:
    display (myhtml_85)
    q8_mark = 0
    
#save answer
if result['description']=="A":
    q8_ans="A"
elif result['description']=="B":
    q8_ans="B"
elif result['description']=="C":
    q8_ans="C"
elif result['description']=="D":
    q8_ans="D"


end_time_q8=time.time()
time_taken_q8=end_time_q8 - start_time_q8
print (f"You took {time_taken_q8:.2f} seconds.")
time.sleep(2)
clear_output()









#conclusion
time_taken_sum = time_taken_q1 + time_taken_q2 + time_taken_q3 + time_taken_q4 + time_taken_q5 +time_taken_q6 + time_taken_q7 + time_taken_q8
myhtml_con1 = HTML("<h1>Congratulations, you have finished the Spatial Resoning Test (SRT)!</h1>")
display(myhtml_con1)
myhtml_con2 = HTML(f"<h2>You took {time_taken_sum:.2f} seconds to answer all 8 questions.</h2>")
display(myhtml_con2)
myhtml_con3 = HTML(f"<h2>You scored {score}/8.</h2>")
display(myhtml_con3)







#creating dataframe to show the overall results
overall_result = {
    'User ID': [f'{user_id}'],
    'Group Number': [f'{group_number}'],
    'Gender': [f'{gender}'],
    'Q1 Answer': [f'{q1_ans}'],
    'Q1 Mark': [f'{q1_mark}'],
    'Q2 Answer': [f'{q2_ans}'],
    'Q2 Mark': [f'{q2_mark}'],
    'Q3 Answer': [f'{q3_ans}'],
    'Q3 Mark': [f'{q3_mark}'],
    'Q4 Answer': [f'{q4_ans}'],
    'Q4 Mark': [f'{q4_mark}'],
    'Q5 Answer': [f'{q5_ans}'],
    'Q5 Mark': [f'{q5_mark}'],
    'Q6 Answer': [f'{q6_ans}'],
    'Q6 Mark': [f'{q6_mark}'],
    'Q7 Answer': [f'{q7_ans}'],
    'Q7 Mark': [f'{q7_mark}'],
    'Q8 Answer': [f'{q8_ans}'],
    'Q8 Mark': [f'{q8_mark}'],
    'Time (s)': [f'{time_taken_sum:.2f}'],
    'Score (out of 8)': [f'{score}'],
}

overall_result_df = pd.DataFrame(overall_result)
display (overall_result_df)





#save the result in json format
test_result = {'Q1 Answer': [f'{q1_ans}'],
    'Q1 Mark': [f'{q1_mark}'],
    'Q2 Answer': [f'{q2_ans}'],
    'Q2 Mark': [f'{q2_mark}'],
    'Q3 Answer': [f'{q3_ans}'],
    'Q3 Mark': [f'{q3_mark}'],
    'Q4 Answer': [f'{q4_ans}'],
    'Q4 Mark': [f'{q4_mark}'],
    'Q5 Answer': [f'{q5_ans}'],
    'Q5 Mark': [f'{q5_mark}'],
    'Q6 Answer': [f'{q6_ans}'],
    'Q6 Mark': [f'{q6_mark}'],
    'Q7 Answer': [f'{q7_ans}'],
    'Q7 Mark': [f'{q7_mark}'],
    'Q8 Answer': [f'{q8_ans}'],
    'Q8 Mark': [f'{q8_mark}'],
}

test_result = pd.DataFrame (test_result)
test_result_json = test_result.to_json()

#creat a data frame for upload 
test_result = {
    'User ID': [f'{user_id}'],
    'Group Number': [f'{group_number}'],
    'Gender': [f'{gender}'],
    'Time (s)': [f'{time_taken_sum:.2f}'],
    'Score (out of 8)': [f'{score}'],
    'Result (json)': test_result_json,
}



#save in google form 2 without gender nor json
#form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfSWJuJPzaJ9ZqUD3ct7RlQHQ6UdThCfqI1k3gi87T64u3D9Q/viewform'
#send_to_google_form(overall_result,form_url)




#save in google form 3 with gender and in json
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdHrxcz50Ypc-OLfqZE0kMXAigUTToctgj1q6OkJNVDut7S6g/viewform'
send_to_google_form(test_result,form_url)








