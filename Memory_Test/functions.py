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

from functions import *

# Displaying the messsage at the beginning of the test 
def test_instructions(color, word):
    style = f"color: {color}; font-size: 50px;" #predetermined style for HTML text, colour and fontsize, style has to be enclosed with quote marks 
    html_out = HTML(f"""<span style='{style}'>{word}</span>""") # <span> tag is to format regular text as opposed to <h1> which are headers, <span style= '{style}'> used to specify style in start tag

    first_instruction = HTML(f'<h1 style="{style}">Welcome to the Memory test. A series of Grids will be displayed with different shapes and colors in different locations.</h1>')
    
    display(first_instruction)
    time.sleep(3)
    clear_output(wait=False)
    
    second_instruction = HTML(f'<h1 style="{style}">Be prepared to answer a series of questions about the position and color of each shape.</h1>')
    
    display(second_instruction)
    time.sleep(3)
    clear_output(wait=False)

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

# Function to let button register events 
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
btn4 = widgets.Button(description="Square")
btn5 = widgets.Button(description="Triangle")
btn6 = widgets.Button(description="Circle")
btn7 = widgets.Button(description="Circle")
btn8 = widgets.Button(description="Triangle")
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
image_links = ["testimage0.png", "testimage1.png", "testimage2.png"]

def display_grids(image_links):
    image = Image(image_links, width = 400)
    display(image)
    time.sleep(3)
    clear_output(wait=False)
    print("Colored grids are displayed...")

def ask_questions(grid_number):
    print(f"\nAnswer the following questions for Grid {grid_number}:")
    total_time = 0
    correct_answers = 0
    
    start_grid_timer = time.time()  # Start timer 
    
    if grid_number == 1:
        print("1. What color was the circle in Grid 1?")
        display_answer_caption()
        panel = widgets.HBox([btn10, btn12, btn11])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Yellow":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        print("2. What shape was on the left of the diamond in Grid 1?")
        display_answer_caption()
        panel = widgets.HBox([btn3, btn5, btn1])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Triangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        print("3. Which shape was purple in Grid 1?")
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
        print("1. What color was the triangle in Grid 2?")
        display_answer_caption()
        panel = widgets.HBox([btn10, btn12, btn11])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Blue":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        print("2. What shape was in red in Grid 2?")
        display_answer_caption()
        panel = widgets.HBox([btn3, btn5, btn1])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Rectangle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        print("3. Which shape was green in Grid 2?")
        display_answer_caption()
        panel = widgets.HBox([btn4, btn5, btn6])
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
        print("1. Which row was the circle in in Grid 3?")
        display_answer_caption()
        panel = widgets.HBox([btn13, btn14])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Second":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        print("2. Which column was the diamond in in Grid 3")
        display_answer_caption()
        panel = widgets.HBox([btn13, btn14, btn15])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Second":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter
        
        print("3. Which shape was on the left of the orange square in Grid 3")
        display_answer_caption()
        panel = widgets.HBox([btn2, btn1, btn3])
        display(panel)
        result = wait_for_event(timeout=20)
        clear_output()
        if result['description'] == "Circle":  # Check if the answer is correct
            correct_answers += 1  # Increment correct answer counter

        end_grid_timer = time.time()  # Stop timer for the current grid
        grid_duration = end_grid_timer - start_grid_timer  # Calculate grid duration
        
    return total_time, min(correct_answers, 9)

total_time = 0
total_correct_answers = 0

for grid_number in range(1, 4):    # Accumulates the total_time and total_correct_answers 
    grid_duration, correct_answers = ask_questions(grid_number)
    total_time += grid_duration
    total_correct_answers += correct_answers
    
    print("\nYour answers for Grid", grid_number, "have been recorded.")

# Print the results of the user 
def print_results(total_correct_answers, total_time):
    print("\nTotal time taken for all Grids:", round(total_time), "seconds")
    print("\nTotal Accuracy for all Grids:", (total_correct_answers), "out of 9")

print_results(total_correct_answers, total_time)

def send_to_google_form(data_dict, form_url):
    ''' Helper function to upload information to a corresponding google form 
        You are not expected to follow the code within this function!
    '''
    form_id = form_url[34:90]
    view_form_url = f'https://docs.google.com/forms/d/e/{form_id}/viewform'
    post_form_url = f'https://docs.google.com/forms/d/e/{form_id}/formResponse'

    page = requests.get(view_form_url)
    content = BeautifulSoup(page.content, "html.parser").find('script', type='text/javascript')
    content = content.text[27:-1]
    result = json.loads(content)[1][1]
    form_dict = {}
    
    loaded_all = True
    for item in result:
        if item[1] not in data_dict:
            print(f"Form item {item[1]} not found. Data not uploaded.")
            loaded_all = False
            return False
        form_dict[f'entry.{item[4][0][0]}'] = data_dict[item[1]]
    
    post_result = requests.post(post_form_url, data=form_dict)
    return post_result.ok
def memory_test()
    total_time = 0
    total_correct_answers = 0 
    # 
    # Collect user information
    name = input("Please enter your full name: ")
    age = input("Enter your age: ")

    for i, image_link in enumerate(image_links, start=1):  # Display each grid
        display_grids(image_link)
        grid_duration, correct_answers = ask_questions(i)  # Return total time and total correct answers 
        total_time += grid_duration
        total_correct_answers += correct_answers
        print("\nYour answers for Grid", i, "have been recorded.")

    print_results(total_correct_answers, total_time)

    # Generate data dict from user results 
    data_dict = {"Name": name,
    "Age": age,
    "Time Taken": total_time,
    "Number of Correct Answers": total_correct_answers
            }

    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfF0rw3RgRsEJrVpnjPqf6kV1DEUInOyP5Hy_6tIZ9rCPJvVQ/viewform?usp=sf_link'
    result = send_to_google_form(data_dict, form_url)
    if result:
        print("Data uploaded successfully!")
    else:
        print("Failed to upload data.")
