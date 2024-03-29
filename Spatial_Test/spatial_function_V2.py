#Imports
import re
import json 
import time
import requests
import threading
import numpy as np
import pandas as pd
import ipywidgets as widgets
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from ipywidgets import widgets, Layout
from jupyter_ui_poll import ui_events
from IPython.display import display, Image, clear_output, HTML

#define the send_to_google_form function
def send_to_google_form(data_dict, form_url):
    ''' 
    Uploads data to a Google Form.
    This function takes a dictionary of data and a Google Form URL, then submits the data to the form. 
    
    Parameters
    ----------
    data_dict : dict
        A dictionary contains the data to be submitted for those fields.
    form_url : str
        The URL of the Google Form where data is to be submitted.
    
    Returns
    -------
    bool
        Returns True if the data was successfully submitted (HTTP response OK), False otherwise. 
    
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

#define the buttons
event_info = {
    'type': '',
    'description': '',
    'time': -1
}

def wait_for_event(timeout=-1, interval=0.001, max_rate=20, allow_interupt=True):    
    """
    Waits for an event to occur within a specified timeout.
    It allows for the specification of a timeout to limit the wait period.

    Parameters
    ----------
    timeout : float
        The maximum time to wait for in seconds. 
        Default is -1 indicating no timeout.
    interval : float, optional
        The time interval between checks for events. 
        Default is 0.001 seconds.
    max_rate : int
        The maximum number of events to process within interval. 
        Default is 20.
    allow_interrupt : bool
        "True" returens immediately when an event occurs. 
        "False" will return after timeout. 
        Default is True.

    Returns
    -------
    dict
        A dictionary containing information about the event that occurred. Default for no event:
        - 'type': The type of the event (empty string if no event).
        - 'description': A description of the event (empty string if no event).
        - 'time': The time the event occurred (-1 if no event).

    """
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

#Function for button clicking
def register_event(btn):
    """
    Waits for an event to occur within a specified timeout.
    
    Parameters
    ----------
    timeout : float
        The maximum time to wait for an event in seconds. 
        Default is -1 indicating no timeout
   interval : float, optional
        The time interval between checks for events. 
        Default is 0.001 seconds.
    max_rate : int
        The maximum number of events to process within interval. 
        Default is 20.
    allow_interrupt : bool
        "True" returens immediately when an event occurs. 
        "False" will return after timeout. 
        Default is True.

    Returns
    -------
    dict
       A dictionary containing information about the event that occurred. Default for no event:
        - 'type': The type of the event (empty string if no event).
        - 'description': A description of the event (empty string if no event).
        - 'time': The time the event occurred (-1 if no event).
          
    """
    # display button description in output area
    event_info['type'] = "click"
    event_info['description'] = btn.description
    event_info['time'] = time.time()
    return

# Function to validate the user ID
def is_valid_id(user_id):
    """
    Validates the provided user ID.

    This function checks whether the supplied user ID is a string 
    consisting of exactly four alphabetic letters. It uses a regular 
    expression to ensure the user ID contains only alphabetic characters 
    and is of the required length.

    Parameters
    ----------
    user_id : str
        The user ID string to be validated.

    Returns
    -------
    bool
        Returns True if the user ID is valid (exactly four alphabetic 
        characters), False otherwise.
    """
    # Check if the user ID has exactly 4 letters (not digits or other characters)
    return bool(re.match(r'^[A-Za-z]{4}$', user_id))

