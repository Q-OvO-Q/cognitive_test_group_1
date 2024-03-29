from spatial_function_V2 import *

# Welcome
#using HTML to display sized text
myhtml_w1 = HTML("<h1 align='center'>Welcome to the Spatial Resoning Test (SRT).</h1>")
display (myhtml_w1)
time.sleep(1)
myhtml_w2 = HTML ('<h2 align="center">Please enter your group number, age, gender and anonymised ID to continue the test.</h2>')
display (myhtml_w2)
#wait followed by clear output
time.sleep(2)
clear_output()

#user input user id
myhtml_w4 = HTML ('<h2>Please enter your anonymised ID (4 letters).</h2>')
display (myhtml_w4)
id_instructions = """
To generate an anonymous 4-letter unique user identifier please enter:
- two letters based on the initials (first and last name) of a childhood friend
- two letters based on the initials (first and last name) of a favourite actor / actress

e.g. if your friend was called Charlie Brown and film star was Tom Cruise
     then your unique identifier would be CBTC
"""
print(id_instructions)


user_id = ""  # Initialize the user_id variable

# Start a while loop that will run until a valid ID is entered
while True:
    user_id = input(">")
    # Use the is_valid_id function to check if the entered ID is valid
    if is_valid_id(user_id):
        print("Thank you, your user ID has been accepted.")
        print(f"User entered id: {user_id}")
        time.sleep(2)
        clear_output()
        break  # Exit the loop if the ID is valid
    else:
        print("Invalid ID. Please try again. ID must be exactly 4 letters.")
        time.sleep(2)
        clear_output()
        display (myhtml_w4)
        print(id_instructions)
        
#group number

myhtml_w3 = HTML ('<h2>Please enter your group Number.</h2>')
display (myhtml_w3)
#collect group number with input
group_number = input('>')
print("User entered group number:", group_number)
time.sleep(1)
clear_output()

#user input age
myhtml_w5 = HTML ('<h2>Please enter your age.</h2>')
display (myhtml_w5)
age = input (">")
print("User entered age:", age)
#wait before clear output
time.sleep(1)
clear_output()


#using button to choose gender
myhtml_w6 = HTML ('<h2>Please choose your physiological gender.</h2>')
display (myhtml_w6)
btnM = widgets.Button(description="Male")
btnF = widgets.Button(description="Female")

btnM.on_click(register_event)
btnF.on_click(register_event)

panel = widgets.HBox([btnM, btnF])
display (panel)

result = wait_for_event()

#using if to record the gender
if result["description"]=="Male":
    print ("User chose Male")
    gender = "Male"
else:
    print ("User chose Female")
    gender = "Female"
#wait before clear output
time.sleep(1)
clear_output()

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

myhtml_data1 = HTML('<h3>Please Press  "YES" below if you consent to the upload.</h3>')
display(myhtml_data1)

#defining two buttons
btnYES = widgets.Button(description="YES")

btnYES.on_click(register_event) 
#displaying buttons
panel = widgets.HBox([btnYES])
display (panel)
result = wait_for_event()

if result['description']=="YES":
    print("Thanks for your participation.")
    print("Please contact a.fedorec@ucl.ac.uk")
    print("If you have any questions or concerns")
    print("regarding the stored results.")
else:
    # end code execution by raising an exception
    raise(Exception("User did not consent to continue test."))

time.sleep(2)
clear_output()

#All data collected, pre-start session 
myhtml_data2 = HTML("<h1>Now, please be prepared for the 8 SRT questions... </h1>")
display(myhtml_data2)
time.sleep(2)
myhtml_data3 = HTML("<h1>And Get Started! </h1>")
display(myhtml_data3)
myhtml_data4 = HTML("<h1>Good LUCK! </h1>")
display(myhtml_data4)
time.sleep(2)
clear_output()

#Question 1

#Scoring System 
score = 0

#Q1 welcome
myhtml_11 = HTML("<h1>Spatial Resoning Test (SRT) Question 1</h1>")
display(myhtml_11)
time.sleep(1)
myhtml_x2 = HTML("<h2>Please observe the following 3D cubes and the 2D projections...</h2>")
display(myhtml_x2)
time.sleep(1)

# Q1 cubes displaying
image_path = 'G1_T4_Q1.jpg'
display(Image(filename=image_path))
start_time_q1=time.time()

#buttons 
myhtml_x3 = HTML("<h2>AND choose the 2D projection that CANNOT be obtained by rotating the 3D cubes in space.</h2>")
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


#Q2 cubes displaying
image_path = 'G1_T4_Q2.jpg'
display(Image(filename=image_path))
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


# Q3 cubes displaying
image_path = 'G1_T4_Q3.jpg'
display(Image(filename=image_path))
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

# Q4 cubes displaying
image_path = 'G1_T4_Q3.jpg'
display(Image(filename=image_path))
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

# Q5 cubes displaying
image_path = 'G1_T4_Q5.jpg'
display(Image(filename=image_path))
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

# Q6 cubes displaying
image_path = 'G1_T4_Q6.jpg'
display(Image(filename=image_path))
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

# Q7 cubes displaying
image_path = 'G1_T4_Q7.jpg'
display(Image(filename=image_path))
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

# Q8 false displaying 
image_path = 'G1_T4_Q8.jpg'
display(Image(filename=image_path))
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

#total time
time_taken_sum = time_taken_q1 + time_taken_q2 + time_taken_q3 + time_taken_q4 + time_taken_q5 +time_taken_q6 + time_taken_q7 + time_taken_q8


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
    'Age':[f'{age}'],
    'Time (s)': [f'{time_taken_sum:.2f}'],
    'Score (out of 8)': [f'{score}'],
    'Result (json)': test_result_json,
}

#save in google form in json
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdHrxcz50Ypc-OLfqZE0kMXAigUTToctgj1q6OkJNVDut7S6g/viewform'
send_to_google_form(test_result,form_url)


#Ranking system

#read online google form
sheetkey = "1ap0UUPdebaRlPsPQ9wdaCYAue3iFt99EA6Vp-ICoL3E"
form_url = f"https://docs.google.com/spreadsheet/ccc?key={sheetkey}&output=xlsx"
form_unclear_df = pd.read_excel(form_url)
form_df = form_unclear_df.dropna(how='all')


#sort the excel in dataframe
form_df_sorted_score = form_df.sort_values(by='Score (out of 8)', ascending=False).reset_index(drop=True)
form_df_sorted_time = form_df.sort_values(by='Time (s)', ascending=False).reset_index(drop=True)
#rank with plus one on the index
score_rank = form_df_sorted_score.index[form_df_sorted_score['User ID'] == f'{user_id}'].tolist()[0] + 1
time_rank = form_df_sorted_time.index[form_df_sorted_time['User ID'] == f'{user_id}'].tolist()[0] + 1

#average score and time
score_mean = form_df["Score (out of 8)"].mean()
time_mean = form_df["Time (s)"].mean()

#conclusion
myhtml_con1 = HTML("<h1 align='center' >Congratulations, you have finished the Spatial Resoning Test (SRT)!</h1>")
display(myhtml_con1)



#display the ranking on time and score. 
myhtml_con2 = HTML(f"""
<p style='text-align: center; font-size: 20px'>
The average time used is {time_mean:.1f} seconds, you took {time_taken_sum:.2f} seconds, ranking at {time_rank}th place.<p>
""")

display(myhtml_con2)
myhtml_con3 = HTML(
    f"""
<p style='text-align: center; font-size: 20px'>
The average score is {score_mean:.1f}, you scored {score} (out of 8), ranking at {score_rank}th place.</p>
""")
display(myhtml_con3)

#creating dataframe to show the overall results
myhtml_summary1 = HTML ('<h1>Here is a summary of your test.</h2>')
display (myhtml_summary1)


overall_result = {
    'User ID': [f'{user_id}'],
    'Group Number': [f'{group_number}'],
    'Age': [f'{age}'],
    'Gender': [f'{gender}'],
    'Time (s)': [f'{time_taken_sum:.2f}'],
    'Time Ranking': [f'{time_rank}'],
    'Score (out of 8)': [f'{score}'],
    'Score Ranking': [f'{score_rank}'],
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
}
#converting to dataframe
overall_result_df = pd.DataFrame(overall_result)
display (overall_result_df)
    

#Ending confirmation and goodbye
myhtml_summary2 = HTML ('<h2> Please press "OK" to confirm.</h2>')
display (myhtml_summary2)
#confirmation button
btnOK = widgets.Button(description="OK")
btnOK.on_click(register_event)
panel = widgets.HBox([btnOK])
display (panel)
wait_for_event()
clear_output()
#bye
myhtml_summary3 = HTML("<h2>Thanks! Wish you a lovely day! Bye~ </h2>")
display (myhtml_summary3)
#wait before clear
time.sleep(2)
clear_output()

