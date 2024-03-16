from T4_function_V1 import *


#Scoring System 
score = 0

# Welcome
print("Welcome to the Spatial Resoning Test (SRT).")
time.sleep(1)
print("Please enter your group number and student number to continue the test.")
time.sleep(1)
print ("Please enter your Group number (number only)")
group_number = input('>')
time.sleep(0.5)
print("Please enter your student ID")
student_ID = input (">")


#Question 1

#Welcome
print("Spatial Resoning Test (SRT) Question 1")
time.sleep(1)
print("Please choose the 2D projection that CANNOT be obtained by rotating the 3D arrangement in space.")
time.sleep(1)

# Q1 cubes drawing
cubes1 = np.full((5,5,5),'')
cubes1[0,0,0:5] = 'r' 
cubes1[1,0,0] = 'g'
cubes1[0,1,0] = 'b'
cubes1[1,1,0] = 'y'
# draw the result
draw_cubes(cubes1)
time.sleep(1)


#draw projections
draw_cubes(cubes1, view='-xy')# draw the view from bottom in XY plane
print ("a")
draw_cubes(cubes1, view='xz')# draw the side view in XZ direction
print ("b")
draw_cubes(cubes1, view='yz')# draw the side view in YZ direction
print ("c")
draw_cubes(cubes1, flip='z', view='xy')# display the projection obtained from the flipped arrangement.
print ("d")
start_time_q1=time.time()

#interaction with user    
q1_ans = input("Enter a,b,c or d:")

if q1_ans == "a":
    print ("correct!")
    score = score + 1 
    q1_mark = 1
else:
    print ("The correct answer is a")
    q1_mark = 0

#time used
end_time_q1=time.time()
time_taken_q1=end_time_q1 - start_time_q1
print (f"You took {time_taken_q1:.2f} seconds")


#Question 2

#Welcome
print("Welcome to the Spatial Resoning Test (SRT) Question 2")
time.sleep(1)
print("Please choose the 2D projection that cannot be obtained by rotating the 3D arrangement in space.")
time.sleep(1)

#Q2 cubes drawing
cubes2 = np.full((5,5,5),'')
cubes2[0:3,0,0] = 'r'
cubes2[0:6,1,0] = 'g'
draw_cubes(cubes2)
time.sleep(1)

#draw projections
draw_cubes(cubes2, view='xy')# draw the view from bottom in XY plane
print("a")
draw_cubes(cubes2, flip='x', view='xz')# display the projection obtained from the flipped arrangement.
print("b")
draw_cubes(cubes2, view='-xy')# draw the side view in -xy direction
print("c")
draw_cubes(cubes2, view='yz')# draw the side view in YZ direction
print("d")
start_time_q2=time.time()

#interaction with user
q2_ans = input("Enter a,b,c or d:")

if q2_ans == "b":
    print ("correct!")
    score = score + 1 
    q2_mark = 1
else:
    print ("The correct answer is b")
    q2_mark = 0
    
end_time_q2=time.time()
time_taken_q2=end_time_q2 - start_time_q2
print (f"You took {time_taken_q2:.2f} seconds")


#Question 3

#Welcome
print("Welcome to the Spatial Resoning Test (SRT) Question 3")
time.sleep(1)
print("Please choose the 2D projection that cannot be obtained by rotating the 3D arrangement in space.")
time.sleep(1)


# Q3 cubes drawing
cubes3 = np.full((5,5,5),'')
cubes3[0:3,0,0] = 'r' 
cubes3[3,1:3,0] = 'g' 
cubes3[1:3,1:3,0:2] = 'b' 
cubes3[3,0,0] = 'm'
cubes3[1,2,2] = 'y'
draw_cubes(cubes3)
time.sleep(1)


#draw projections
draw_cubes(cubes3, view='xz')# draw the side view in XZ direction
print("a")
draw_cubes(cubes3, view='yz')# draw the side view in YZ direction
print("b")
draw_cubes(cubes3, view='-yz')# draw the side view in -YZ direction (other side)
print("c")
draw_cubes(cubes3, view='-xy')# draw the view from bottom in XY plane
print("d")
start_time_q3=time.time()

#interaction with user 
q3_ans = input ("Enter a,b,c or d:")

if q3_ans == "c":
    print ("correct")
    score = score + 1
    q3_mark = 1
else:
    print ("The correct answer is c")
    q3_mark = 0
    
end_time_q3=time.time()
time_taken_q3=end_time_q3 - start_time_q3
print (f"You took {time_taken_q3:.2f} seconds")


#conclusion
time_taken_sum = time_taken_q1 + time_taken_q2 + time_taken_q3
print ("Congratulations, you have finished the Spatial Resoning Test (SRT).")
print (f"You took {time_taken_sum:.2f} seconds to answer all three questions.")
print (f"You scored {score}/3.")


#save in local disk

#creating dataframe to store the results
overall_result = {
    'Student ID': [f'{student_ID}'],
    'Group Number': [f'{group_number}'],
    'Q1 Answer': [f'{q1_ans}'],
    'Q1 Mark': [f'{q1_mark}'],
    'Q2 Answer': [f'{q2_ans}'],
    'Q2 Mark': [f'{q2_mark}'],
    'Q3 Answer': [f'{q3_ans}'],
    'Q3 Mark': [f'{q3_mark}'],
    'Time (s)': [f'{time_taken_sum:.2f}'],
    'Score (out of 3)': [f'{score}'],
}

overall_result = pd.DataFrame(overall_result)
overall_result

#save in google form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeJe1fSLEzfx8iyUsECnEqmCD5_oBdYGofO_sGPC0x9HxdEEA/viewform'
send_to_google_form(overall_result,form_url)
