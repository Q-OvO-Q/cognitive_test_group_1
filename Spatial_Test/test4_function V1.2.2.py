#define the function to draw cubes 
#general import
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



def draw_cubes(cubes, ticks=False, grid=True, view='', flip='', rot=0, ax3d=None):
    """
    Draws a 3D plot of cubes with specified properties.

    This function creates a 3D visualization of cubes based on the input array, with options to adjust the view, rotation, and other visual elements. 
    If an existing matplotlib 3D axis is not provided, it creates a new figure and axis for the plot.
 
    
    Parameters:
    -----------
    cubes: numpy.ndarray
        Array-like structure where each element represents a cube's position and color.
    ticks: bool
        Boolean indicating whether to display axis ticks. Default is False.
        tick = "True" returns a grid with numbered coordinates. 
        tick = "False" returns a grid without numbered coordinates.
    grid: bool
        Boolean indicating whether to display the grid. Default is True.
        grid = "True" returns cubes built on lined grids. 
        grid = "False" grid returns cubes built on lined grids. 
    view: str
        String specifying the initial view of the plot ('xy', '-xy', 'xz', '-xz', 'yz', '-yz'). An empty string uses the default view.
        view = "xy" retunrs the front view of the cubes. 
        view = "-xy" retunrs the mirror image of top view of the cubes. 
        view = "xz" retunrs the front view of the cubes. 
        view = "-xz" retunrs the mirror image of front view of the cubes. 
        view = "yz" retunrs the right view of the cubes. 
        view = "-yz" retunrs the mirror image of right view of the cubes. 
    flip: str
        String specifying axis along which to mirror the plot ('x', 'y', 'z'). Can combine multiple axes.
        flip = "x" returns the mirror image with respect to x-axis as axis of symmetry.
        flip = "y" returns the mirror image with respect to y-axis as axis of symmetry.
        flip = "z" returns the mirror image with respect to z-axis as axis of symmetry.
    rot: int
        The cubes will rotate around its vertical central axis by a set angle (in degree) in a clockwise manner. 
    ax3d: class
        An existing matplotlib 3D axis object to draw the cubes on. If None, a new figure and axis are created.
    
    Returns:
    -------
    Nothing explicitly, but displays or updates a 3D plot of the cubes. If ax3d is provided, the plot is drawn on this existing axis without creating a new figure.
            
        
    Raises
    ------
    ValueError
          If the parameter "ax3d" is empty.
          matplotlib must be installed and working in the execution environment in order to display the plot. 


    """


    # create empty cube
    cubes_to_draw = np.zeros(cubes.shape)
    
    # set elements to 1 where colour is not empty
    cubes_to_draw[cubes!=''] = 1

    # make figure and 3d axes for plotting
    if ax3d is None:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d', proj_type='ortho', box_aspect=(4,4,4))
    else:
        ax = ax3d
        
    nx, ny, nz = cubes.shape

    ax.axes.set_xlim3d(0, nx) 
    ax.axes.set_ylim3d(0, ny) 
    ax.axes.set_zlim3d(0, nz) 

    # The cubes can be plotted using a 3D voxels plot
    ax.voxels(cubes_to_draw, facecolors=cubes, edgecolors='k', shade=False);

    # view argument allows users to set a 2D projection
    if view == 'xy': ax.view_init(90, -90, 0+rot)
    elif view == '-xy': ax.view_init(-90, 90, 0-rot)
    elif view == 'xz': ax.view_init(0, -90, 0+rot)
    elif view == '-xz': ax.view_init(0, 90, 0-rot)
    elif view == 'yz': ax.view_init(0, 0, 0+rot)
    elif view == '-yz': ax.view_init(0, 180, 0-rot)
    else:   ax.view_init(azim=ax.azim+rot)

    # flip argument allows user to show a mirror image
    # flip='x' reverses image in x direction etc.
    if 'x' in flip: ax.axes.set_xlim3d(nx, 0) 
    if 'y' in flip: ax.axes.set_ylim3d(ny, 0) 
    if 'z' in flip: ax.axes.set_zlim3d(nz, 0) 

    # style figure ticks and grid lines
    if ticks==False: 
        for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
            axis.set_ticklabels([])
            axis.line.set_linestyle('')
            axis._axinfo['tick']['inward_factor'] = 0.0
            axis._axinfo['tick']['outward_factor'] = 0.0
            
    if grid==False and ticks==False: ax.set_axis_off()
    
    if ax3d is not None:
        # return axes with result
        return
    else:
        # show image
        display(fig)

        # delete figure
        plt.close(fig)

    return 







#define the send_to_google_form function 
def send_to_google_form(data_dict, form_url):
    ''' 
    Uploads information to a specified Google Form.

    This helper function takes a dictionary of data and a Google Form URL, then programmatically submits the data to the form. 
    It extracts the form ID from the given URL, constructs the form submission URL, and posts the data. 
    Note that the function checks if all required form fields are provided in `data_dict`.
    
    Parameters
    ----------
    data_dict : dict
        A dictionary where keys correspond to form field names and values are the data to be submitted for those fields.
    form_url : str
        The URL of the Google Form where data is to be submitted. This URL is used to extract the form ID and construct the submission endpoint.
    
    
    Returns
    -------
    bool
        Returns True if the data was successfully submitted (HTTP response OK), False otherwise. If any required form item is missing in `data_dict`, the function prints a message and returns False without attempting to submit.
    
    Notes
    -----
    This function requires the `requests` library for sending HTTP requests and the `BeautifulSoup` library from `bs4` for parsing HTML content to extract form fields dynamically. Ensure these libraries are installed and imported in your script.
    The data headings of the google form must match exactly with the titles of data_dict.
    

    Examples
    --------
    >>> data_dict = {'Name': 'John Doe', 'Email': 'john.doe@example.com', 'Feedback': 'Great work!'}
    >>> form_url = 'https://docs.google.com/forms/d/e/some_form_id/viewform'
    >>> send_to_google_form(data_dict, form_url)
    True
    
    
    Helper function to upload information to a corresponding google form 
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







#define the buttons
event_info = {
    'type': '',
    'description': '',
    'time': -1
}

def wait_for_event(timeout=-1, interval=0.001, max_rate=20, allow_interupt=True):    
    """
    Waits for an event to occur within a specified timeout, polling at defined intervals.

    This function listens for UI events, updating a global `event_info` dictionary with the event's type, description, and time when an event occurs. It allows for the specification of a timeout to limit the wait period and can be configured to allow interruptions based on incoming events.

    Parameters
    ----------
    timeout : float, optional
        The maximum time to wait for an event in seconds. A negative value indicates no timeout. Default is -1.
    interval : float, optional
        The time interval in seconds between checks for UI events. Default is 0.001 seconds.
    max_rate : int, optional
        The maximum number of events to process within each interval. Default is 20.
    allow_interrupt : bool, optional
        If True, the function will return immediately when an event occurs. If False, it waits until the timeout expires. Default is True.

    Returns
    -------
    dict
        A dictionary containing information about the event that occurred. If no event occurs within the timeout period, the dictionary will contain default values indicating no event:
        - 'type': The type of the event (empty string if no event).
        - 'description': A description of the event (empty string if no event).
        - 'time': The time the event occurred (-1 if no event).

    Notes
    -----
    This function uses a global dictionary `event_info` to store and return event information. It is designed to be used within environments that support UI events and requires access to specific UI polling functions (`ui_events` in this context) to function correctly.
    
    
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

# this function lets buttons 
# register events when clicked







def register_event(btn):
    """
    Waits for an event to occur within a specified timeout, polling at defined intervals.

    This function listens for UI events, updating a global `event_info` dictionary with the event's type, description, and time when an event occurs. It allows for the specification of a timeout to limit the wait period and can be configured to allow interruptions based on incoming events.

    Parameters
    ----------
    timeout : float, optional
        The maximum time to wait for an event in seconds. A negative value indicates no timeout. Default is -1.
    interval : float, optional
        The time interval in seconds between checks for UI events. Default is 0.001 seconds.
    max_rate : int, optional
        The maximum number of events to process within each interval. Default is 20.
    allow_interrupt : bool, optional
        If True, the function will return immediately when an event occurs. If False, it waits until the timeout expires. Default is True.

    Returns
    -------
    dict
        A dictionary containing information about the event that occurred. If no event occurs within the timeout period, the dictionary will contain default values indicating no event:
        - 'type': The type of the event (empty string if no event).
        - 'description': A description of the event (empty string if no event).
        - 'time': The time the event occurred (-1 if no event).

    Notes
    -----
    This function uses a global dictionary `event_info` to store and return event information. It is designed to be used within environments that support UI events and requires access to specific UI polling functions (`ui_events` in this context) to function correctly.
    
    
    """
    # display button description in output area
    event_info['type'] = "click"
    event_info['description'] = btn.description
    event_info['time'] = time.time()
    return





def register_btn_event(btn):
    """
    Records an event when a button is clicked, by updating a global `event_info` dictionary.

    This function is designed to be called upon a button click event. It updates the global
    `event_info` dictionary with the event's type, description, and the time it occurred. The
    event type is set to "button click", and the description and time are taken from the button
    object and the current time, respectively.

    Parameters
    ----------
    btn : object
        The button instance that was clicked. It must have a `description` attribute, which is
        used to populate the event's description in the `event_info` dictionary.

    Returns
    -------
    None
        Does not return any value. It modifies the global `event_info` dictionary in place.

    Notes
    -----
    The function operates by side-effect, modifying the global `event_info` dictionary. This
    dictionary is expected to have 'type', 'description', and 'time' keys. The function is
    intended for use within a user interface framework that can detect and respond to button
    click events.
    
    
    """
    event_info['type'] = "button click"
    event_info['description'] = btn.description
    event_info['time'] = time.time()
    return







def register_text_input_event(text_input):
    """
    Updates the global event information to record a text input event.

    This function is called when a text input event occurs. It captures the event by updating
    the global `event_info` dictionary with the event type as "text_entry", the content of the
    text input, and the timestamp of the event. This is useful for logging and handling user
    input within a user interface.

    Parameters
    ----------
    text_input : object
        The text input instance from which the event originated. This object should have a
        `value` attribute, which contains the text entered by the user.

    Returns
    -------
    None
        This function does not return a value. Instead, it modifies the global `event_info`
        dictionary in place, adding details about the text input event.

    Notes
    -----
    - The `event_info` dictionary is expected to be globally accessible and to have 'type',
      'description', and 'time' keys.
    - The function sets the 'type' key to "text_entry", uses the `value` attribute of the
      `text_input` parameter for the 'description', and sets the 'time' to the current time.
    - This function is designed for use within a GUI framework that supports text input events.
    
    
    """
    event_info['type'] = "text_entry"
    event_info['description'] = text_input.value
    event_info['time'] = time.time()
    return





def text_input(prompt=None):
    """
    Presents a text input field to the user and waits for input or a timeout.

    This function displays a text input widget with an optional prompt. It then waits for the user
    to submit text input or for a timeout period to elapse. Once text is submitted, the input field
    is disabled, and the submitted text is returned. If the timeout period elapses before any text
    is submitted, an empty string is returned.

    Parameters
    ----------
    prompt : str, optional
        A prompt or description to display alongside the text input field. Helps guide the user
        on what information to enter. If None, no prompt is displayed.

    Returns
    -------
    str
        The text entered by the user. Returns an empty string if the timeout period elapses
        before any input is submitted.

    Notes
    -----
    - This function uses global event handling through the `register_text_input_event` function
      to capture the text submitted by the user.
    - A timeout of 10 seconds is enforced; if no input is received within this period, the
      function returns an empty string.
    - The text input widget is displayed using the `widgets.Text` class from the `ipywidgets`
      library. The widget is configured to ignore deprecation warnings.
    - This function is designed to be used in interactive Python environments that support
      IPython widgets, such as Jupyter notebooks.

    Examples
    --------
    >>> user_input = text_input(prompt="Enter your name:")
    >>> print(user_input)
    
    
    """
    text_input = widgets.Text(description=prompt, style= {'description_width': 'initial'})
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    text_input.on_submit(register_text_input_event)
    display(text_input)
    event = wait_for_event(timeout=10)
    text_input.disabled = True
    return event['description']






