# pip install jupyter_ui_poll
from IPython.display import display, Image, clear_output, HTML
import time
import random
import pandas as pd 

import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from jupyter_ui_poll import ui_events

import requests
from bs4 import BeautifulSoup
import json 
# Button widgets 

event_info = {
    'type': '',
    'description': '',
    'time': -1
}

def wait_for_event(timeout=-1, interval=0.001, max_rate=20, allow_interupt=True):    
    start_wait = time.time()

    # set event info to be empty
    # as this is dict we can change entries
    # directly without using
    # the global keyword
    event_info['type'] = ""
    event_info['description'] = ""
    event_info['time'] = -1

    n_proc = int(max_rate*interval)+1
    
    with ui_events() as ui_poll:
        keep_looping = True
        while keep_looping==True:
            # process UI events
            ui_poll(n_proc)

            # end loop if we have waited more than the timeout period
            if (timeout != -1) and (time.time() > start_wait + timeout):
                keep_looping = False
                
            # end loop if event has occured
            if allow_interupt==True and event_info['description']!="":
                keep_looping = False
                
            # add pause before looping
            # to check events again
            time.sleep(interval)
    
    # return event description after wait ends
    # will be set to empty string '' if no event occured
    return event_info

# this function lets buttons 
# register events when clicked
def register_event(btn):
    # display button description in output area
    event_info['type'] = "click"
    event_info['description'] = btn.description
    event_info['time'] = time.time()
    return
def on_button_clicked(image_path):
    clear_output()
    display(HTML(f'<img src="{image_path}">'))

btn1 = widgets.Button(description="Circle")
btn2 = widgets.Button(description="Square")
btn3 = widgets.Button(description="Rectangle")
btn4 = widgets.Button(description="Heart")
btn5 = widgets.Button(description="Triangle")
btn6 = widgets.Button(description="Cylinder")
btn7 = widgets.Button(description="Right Arrow")
btn8 = widgets.Button(description="Sun")
btn9 = widgets.Button(description="Diamond")
btn10 = widgets.Button(description="Yellow")
btn11 = widgets.Button(description="Green")
btn12 = widgets.Button(description="Blue")
btn13 = widgets.Button(description="First")
btn14 = widgets.Button(description="Second")
btn15 = widgets.Button(description="Third")

btn1.on_click(register_event) 
btn2.on_click(register_event) 
btn3.on_click(register_event) 
btn4.on_click(register_event) 
btn5.on_click(register_event) 
btn6.on_click(register_event) 
btn7.on_click(register_event) 
btn8.on_click(register_event) 
btn9.on_click(register_event) 
btn10.on_click(register_event) 
btn11.on_click(register_event) 
btn12.on_click(register_event) 
btn13.on_click(register_event) 
btn14.on_click(register_event) 
btn15.on_click(register_event) 

def generate_answer(grid_number):
    if grid_number == 1: 
        myhtml1 = HTML("<h1>Indicate your answer below:</h1>")
        display(myhtml1)
        myhtml2 = HTML("<h2>Please only choose one answer.</h2>")
        display(myhtml2)

        panel = widgets.HBox([btn1, btn2, btn3])
        display(panel)
        result = wait_for_event(timeout=5)
        clear_output()

    if result['description']!="":
        print(f"User clicked: {result['description']}")
    else:
        print("User did not click in time")

# Function to generate subtext after each question 
def display_answer_caption():
    myhtml1 = HTML("<h1>Indicate your answer below:</h1>")
    display(myhtml1)
    myhtml2 = HTML("<h2>Please only choose one answer.</h2>")
    display(myhtml2)

# Function to display image grids 
image_links = ["testimage0.png", "testimage1.png", "testimage2.png", "testimage3.png", "testimage4.png", "testimage5.png", "testimage6.png", "testimage7.png"]

def display_grids(image_links):
    image = Image(image_links, width = 700)
    display(image)
    time.sleep(12)
    clear_output(wait=False)


def ask_questions(grid_number):
    total_time = 0
    correct_answers = 0
    
    start_grid_timer = time.time()  # Start timer 
    
    if grid_number == 1:
        myhtml31 = HTML("<h2>1. What color was the Circle in Grid 1?</h2>")
        display(myhtml31)
        display_answer_caption()
        panel = widgets.HBox([btn10, btn12, btn11])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Yellow":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
            print("Correct!") 
            clear_output()
        
        myhtml30 = HTML("<h2>2. What shape was on the left of the diamond in Grid 1?</h2>")
        display(myhtml30)
        display_answer_caption()
        panel = widgets.HBox([btn3, btn5, btn1])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Triangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml3 = HTML("<h2>3. Which shape was purple in Grid 1?</h2>")
        display(myhtml3)
        display_answer_caption()
        panel = widgets.HBox([btn2, btn3, btn5])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Triangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter

    end_grid_timer = time.time()  # Stop timer for the current grid
    grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration

    total_time += grid_duration
    
    # Question 2
    if grid_number == 2:
        myhtml4 = HTML("<h2>1. What color was the triangle in Grid 2?</h2>")
        display(myhtml4)
        display_answer_caption()
        panel = widgets.HBox([btn10, btn12, btn11])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Blue":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml5 = HTML("<h2>2. What shape was in red in Grid 2?</h2>")
        display(myhtml5)
        display_answer_caption()
        panel = widgets.HBox([btn3, btn5, btn1])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Rectangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml6 = HTML("<h2>3. Which shape was green in Grid 2?</h2>")
        display(myhtml6)
        display_answer_caption()
        panel = widgets.HBox([btn2, btn5, btn1])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Square":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter

        end_grid_timer = time.time()  # Stop timer for the current grid
        grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration

        total_time += grid_duration
    
    # Question 3
    if grid_number == 3:
        myhtml7 = HTML("<h2>1. Which row was the circle in Grid 3?</h2>")
        display(myhtml7)
        display_answer_caption()
        panel = widgets.HBox([btn13, btn14])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Second":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml8 = HTML("<h2>2. Which column was the diamond in in Grid 3?</h2>")
        display(myhtml8)
        display_answer_caption()
        panel = widgets.HBox([btn13, btn14, btn15])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Second":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml9 = HTML("<h2>3. Which shape was on the left of the orange square in Grid 3?</h2>")
        display(myhtml9)
        display_answer_caption()
        panel = widgets.HBox([btn2, btn1, btn3])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Circle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
            
        myhtml10 = HTML("<h2>3. Which shape was on the top of the orange square in Grid 3</h2>")
        display(myhtml10)
        display_answer_caption()
        panel = widgets.HBox([btn5, btn1, btn3])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Circle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter

        end_grid_timer = time.time()  # Stop timer for the current grid
        grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration

     # Question 4
    if grid_number == 4:
        myhtml11 = HTML("<h2>1. What color was the square in Grid 4?</h2>")
        display(myhtml11)
        display_answer_caption()
        panel = widgets.HBox([btn12, btn10, btn11])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Green":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml12 = HTML("<h2>2. What shape was in blue in Grid 4?</h2>")
        display(myhtml12)
        display_answer_caption()
        panel = widgets.HBox([btn9, btn1, btn2])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Diamond":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml13 = HTML("<h2>3. Which shape was yellow in Grid 4?</h2>")
        display(myhtml13)
        display_answer_caption()
        panel = widgets.HBox([btn2, btn6, btn1])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Cylinder":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter

        end_grid_timer = time.time()  # Stop timer for the current grid
        grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration

        total_time += grid_duration
        
          # Question 5
    if grid_number == 5:
        myhtml14 = HTML("<h2>1. What shape was inside the circle in Grid 5?</h2>")
        display(myhtml14)
        display_answer_caption()
        panel = widgets.HBox([btn2, btn5, btn8])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Triangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml15 = HTML("<h2>2. What shape was in green in Grid 5?</h2>")
        display(myhtml15)
        display_answer_caption()
        panel = widgets.HBox([btn4, btn8, btn2])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Square":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml16 = HTML("<h2>3. What shape was inside the heart in Grid 5?</h2>")
        display(myhtml16)
        display_answer_caption()
        panel = widgets.HBox([btn1, btn6, btn7])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Circle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
    
        myhtml17 = HTML("<h2>3. Which row was the cylinder in?</h2>")
        display(myhtml17)
        display_answer_caption()
        panel = widgets.HBox([btn13, btn14, btn15])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Third":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter

        end_grid_timer = time.time()  # Stop timer for the current grid
        grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration

        total_time += grid_duration
    
          # Question 6
    if grid_number == 6:
        myhtml18 = HTML("<h2>1. What shape was in yellow in Grid 6?</h2>")
        display(myhtml18)
        display_answer_caption()
        panel = widgets.HBox([btn2, btn5, btn8])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Triangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml19 = HTML("<h2>2. What colour was the triangle in Grid 6?</h2>")
        display(myhtml19)
        display_answer_caption()
        panel = widgets.HBox([btn10, btn11, btn12])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Yellow":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml20 = HTML("<h2>3. What shape was inside the heart in Grid 6?</h2>")
        display(myhtml20)
        display_answer_caption()
        panel = widgets.HBox([btn1, btn6, btn7])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Right Arrow":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
            
        myhtml21 = HTML("<h2>4. What shape contained the square in Grid 6?</h2>")
        display(myhtml21)
        display_answer_caption()
        panel = widgets.HBox([btn1, btn4, btn9])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Circle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        end_grid_timer = time.time()  # Stop timer for the current grid
        grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration

         # Question 7
    if grid_number == 7:
        myhtml22 = HTML("<h2>1. What shape was inside the heart in Grid 7?</h2>")
        display(myhtml22)
        display_answer_caption()
        panel = widgets.HBox([btn2, btn1, btn8])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Circle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml23 = HTML("<h2>2. What row was the smiley face in, in Grid 7?</h2>")
        display(myhtml23)
        display_answer_caption()
        panel = widgets.HBox([btn13, btn14, btn15])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Third":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml24 = HTML("<h2>3. What shape contained the right arrow in Grid 7?</h2>")
        display(myhtml24)
        display_answer_caption()
        panel = widgets.HBox([btn5, btn4, btn8])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Heart":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml25 = HTML("<h2>4. Pick one of the shapes that contained the circle in Grid 7.</h2>")
        display(myhtml25)
        display_answer_caption()
        panel = widgets.HBox([btn4, btn2, btn5])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Triangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
            
        myhtml26 = HTML("<h2>5. What other shape contained contained the circle in Grid 7.</h2>")
        display(myhtml26)
        display_answer_caption()
        panel = widgets.HBox([btn4, btn2, btn5])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Triangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter

        end_grid_timer = time.time()  # Stop timer for the current grid
        grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration

        total_time += grid_duration

     # Question 8
    elif grid_number == 8:
        myhtml22 = HTML("<h2>1. What shape was inside the heart in Grid 8?</h2>")
        display(myhtml22)
        display_answer_caption()
        panel = widgets.HBox([btn7, btn3, btn8])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Right Arrow":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml23 = HTML("<h2>2. What row was the divison sign in, in Grid 8?</h2>")
        display(myhtml23)
        display_answer_caption()
        panel = widgets.HBox([btn13, btn14, btn15])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Second":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml24 = HTML("<h2>3. What shape contained the smiley face in Grid 8?</h2>")
        display(myhtml24)
        display_answer_caption()
        panel = widgets.HBox([btn5, btn4, btn8])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Heart":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        myhtml25 = HTML("<h2>4. What shape contained the sun in Grid 8.</h2>")
        display(myhtml25)
        display_answer_caption()
        panel = widgets.HBox([btn4, btn9, btn6])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Triangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter

        end_grid_timer = time.time()  # Stop timer for the current grid
        grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration

        total_time += grid_duration
    
    return total_time, min(correct_answers, 30)

total_time = 0
total_correct_answers = 0

# Calculates and accumulate the total time taken by the user and total number of correct answers using the increment counter 
for grid_number in range(1, 8):    # Accumulates the total_time and total_correct_answers 
    grid_duration, correct_answers = ask_questions(grid_number)
    total_time += grid_duration
    total_correct_answers += correct_answers


# Print the results of the user 
def print_results(total_correct_answers, total_time):
    myhtml30 = HTML("<h2>Well done! You have completed the test! Here are your results:</h2>")
    display(myhtml30)
    print("\nTotal Time Taken for all Grids:", round(total_time), "seconds")
    print("\nTotal Accuracy for all Grids:", (total_correct_answers), "out of 30")

from IPython.display import HTML, display, clear_output
import time
import requests
from bs4 import BeautifulSoup
import json

def test_instructions(color, word):
    style = f"color: {color}; font-size: 50px;"
    html_out = HTML(f"""<span style='{style}'>{word}</span>""")
    first_instruction = HTML(f'<h1 style="{style}">Welcome to the Memory test.</h1>')
    display(first_instruction)
    time.sleep(3)
    clear_output(wait=False)
    second_instruction = HTML(f'<h1 style="{style}">The test will display images of 7 colored grids with different shapes of different colors. Each grid will be displayed for 10 seconds.</h1>')
    display(second_instruction)
    time.sleep(5)
    clear_output(wait=False)
    third_instruction = HTML(f'<h1 style="{style}">Be prepared to answer a series of questions about the position and color of each shape.</h1>')
    display(third_instruction)
    time.sleep(5)
    clear_output(wait=False)
    
def display_consent_information():
    display(HTML("<h1 align='center'>Data Consent Information</h1>"))
    display(HTML("""
    <p style="text-align: center; font-size: 18px">
    We wish to record your response data to an anonymized public data repository.<br>
    Your data will be used for educational teaching purposes practicing data analysis and visualization.<br>
    If you do not want your data to be used, please close this program immediately.<br>
    Otherwise, press Enter to continue.
    </p>
    """))
    input("Press Enter to continue...")
    clear_output() 
    
def display_information_collection():
    display(HTML("""
    <h1 align='center'>Information Collection</h1>
    <p style="text-align: center; font-size: 18px">
    First, please provide your anonymised ID. Follow the guidance below:<br>
    - The first two letters are based on the initials (first and last name) of a childhood friend.<br>
    - The last two letters are based on the initials (first and last name) of a favorite actor/actress.<br>
    - For example, if your friend was called Charlie Brown and the film star was Tom Cruise, then your ID would be CBTC.
    </p>
    """))
    user_id = input("Please enter your anonymised ID: ")
    clear_output()
    
    display(HTML("""
    <p style="text-align: center; font-size: 18px">
    Next, please provide your age.
    </p>
    """))
    age = input("Please enter your age: ")
    clear_output()
    
    display(HTML("""
    <p style="text-align: center; font-size: 18px">
    Next, please provide your gender.
    </p>
    """))
    gender = input("Please enter your gender: ")
    clear_output()
    
    return user_id, age, gender

def send_to_google_form(data_dict, form_url):
    form_id = form_url.split("/")[len(form_url.split("/")) - 2] # Extract the form ID
    view_form_url = f'https://docs.google.com/forms/d/e/{form_id}/viewform'
    post_form_url = f'https://docs.google.com/forms/d/e/{form_id}/formResponse'

    page = requests.get(view_form_url)
    if page.status_code == 200:
        content = BeautifulSoup(page.content, "html.parser").find('script', type='text/javascript')
        if content:
            content_text = content.text
            if content_text:
                content_text = content_text[27:-1]
                result = json.loads(content_text)[1][1]
                form_dict = {}

                loaded_all = True
                for item in result:
                    if item[1] not in data_dict:
                        print(f"Form item {item[1]} not found. Data not uploaded.")
                        loaded_all = False
                        return False
                    form_dict[f'entry.{item[4][0][0]}'] = data_dict[item[1]]

                post_result = requests.post(post_form_url, data=form_dict)
                if post_result.ok:
                    print("Thank you for your participation.")
                    return True
                else:
                    print("Error uploading data.")
            else:
                print("Content text is empty.")
        else:
            print("Script element with type 'text/javascript' not found.")
    else:
        print(f"Failed to retrieve form page. Status code: {page.status_code}")

    return False

def memory_test():
    total_time = 0
    total_correct_answers = 0 
    
    # Display instructions and collect user information
    display_consent_information()
    user_id, age, gender = display_information_collection()
    test_instructions('black', 'Memory Test')
    
    for i, image_link in enumerate(image_links, start=1):  # Display each grid
        display_grids(image_link)
        grid_duration, correct_answers = ask_questions(i)  # Return total time and total correct answers 
        total_time += grid_duration
        total_correct_answers += correct_answers

    print_results(total_correct_answers, total_time)
    
   # Initialize data_dict
    data_dict = {
        "User ID": user_id,
        "Age": age,
        "Gender": gender,
        "Time Taken": total_time,
        "Number of Correct Answers": total_correct_answers
    }
    
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeCEsBro8-LD8-aOWTdcutYJQ-CLOAtxNO2P91w1ddGfKlfmQ/viewform?usp=sharing'
    result = send_to_google_form(data_dict, form_url)
    if result:
        print("For any questions, please contact Alex Fedorec at @a.fedorec@ucl.ac.uk")
    else:
        print("Failed to upload data.")
