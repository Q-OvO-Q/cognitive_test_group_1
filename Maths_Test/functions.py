import time
import random
import requests
import json
import ipywidgets as widgets
from jupyter_ui_poll import ui_events
from IPython.display import display, clear_output, HTML
from bs4 import BeautifulSoup

# Initialize Variables
# Dictionary for storing event information such as type, description, and timestamp
event_info_dict = {'type': ["test", ], 'description': ["program started", ],
                   'time': [time.asctime(time.localtime(time.time())), ]}

# Dictionary for tracking accuracy across different difficulty levels
accuracy_dict = {'easy_correct': 0, 'easy_total': 0, 'medium_correct': 0, 'medium_total': 0, 'hard_correct': 0,
                 'hard_total': 0}
# Dictionary for storing questions, answers, correctness, and time taken for each question
qas_dict = {'question': [], 'answer': [], 'is_correct': [], 'time_taken': []}
# Dictionary for storing the description of the button pressed, used for feedback collection
button_description = {'description': ''}
DIFFICULTY = ""
# Global variables to track response states
RESPONDED = False
PAUSED = False


def wait_for(wait_type, timeout=-1.0, interval=0.001, max_rate=20.0, allow_interrupt=True):
    """
        Waits for a specified event type to occur, with optional timeout.

        Parameters:
            wait_type (str): The type of event to wait for ('response' or 'pause').
            timeout (float): How long to wait before timing out. A value of -1 means no timeout.
            interval (float): How often to check for the event.
            max_rate (float): Maximum processing rate.
            allow_interrupt (bool): If True, allows the waiting to be interrupted by the event.

        Returns:
            None
    """
    global RESPONDED, PAUSED
    start_wait = time.time()
    button_description = {'description': ''}
    n_proc = int(max_rate * interval) + 1
    with ui_events() as ui_poll:
        keep_looping = True
        while keep_looping:
            ui_poll(n_proc)
            if (timeout != -1.0) and (time.time() > start_wait + timeout):
                keep_looping = False
            if allow_interrupt == True and wait_type == "response" and RESPONDED:
                keep_looping = False
                # Reset the RESPONDED flag for future use
                RESPONDED = False
            if allow_interrupt == True and wait_type == "pause" and PAUSED == False:
                keep_looping = False
            time.sleep(interval)
    return


def change_dict_data(dict_name, key_list, value_list, change_type):
    """
        Modifies the data within a dictionary either by appending or overwriting.

        Parameters:
            dict_name (dict): The dictionary to modify.
            key_list (list): A list of keys within the dictionary to be modified.
            value_list (list): Values corresponding to the keys that will be used for modification.
            change_type (str): Specifies the type of modification ('append' or 'overwrite').

        Returns:
            None
    """
    if len(key_list) != len(value_list):
        # Ensure the keys and values lists are of equal length
        print("list length doesn't match")
    if change_type == "append":
        # Append new values to each corresponding key
        for i in range(len(key_list)):
            dict_name[key_list[i]].append(value_list[i])
    elif change_type == "overwrite":
        # Overwrite existing values with new values for each key
        for i in range(len(key_list)):
            dict_name[key_list[i]] = value_list[i]
    return


def universal_callback(change):
    """
        A universal callback function to handle various widget events.

        Parameters:
            change: The returned event object containing event details.

        Returns:
            None
    """
    # Flag to indicate that a response has been made
    global RESPONDED
    event_type = ''
    description = ''
    if change == "force":
        # Handle forced events (e.g., timeout)
        event_type = "force"
        description = "time_out"
    elif isinstance(change, widgets.Button):
        # Handle button click events
        event_type = "button_click"
        description = change.description
        button_description['description'] = change.description
    elif isinstance(change['owner'], widgets.Text):
        # Handle text input events
        event_type = "text_input"
        description = change['new']
    elif isinstance(change['owner'], widgets.Dropdown):
        # Handle dropdown selection events
        event_type = "dropdown_select"
        description = change['new']
    # Record the event in the global event information dictionary
    change_dict_data(event_info_dict, ["type", "description", "time"],
                     [event_type, description, time.asctime(time.localtime(time.time()))],
                     "append")
    # Set the response flag
    RESPONDED = True
    return


def pause_display(section, difficulty, time_allowed, time_remaining, test_output, info_output):
    """
        Displays a pause message between test sections, indicating the start of a new difficulty level.

        Parameters:
            section (int): The current test section number.
            difficulty (str): The current difficulty level of the test.
            time_allowed (int): The total time allowed for this section.
            time_remaining (int): The remaining time for the test.
            test_output (Output widget): The widget used to display test questions.
            info_output (Output widget): The widget used to display information messages.

        Returns:
            int: The updated time remaining after the pause.
    """
    global RESPONDED, PAUSED
    # Hide test output during the pause
    test_output.layout.display = 'none'
    # Make information output visible
    info_output.layout.visibility = 'visible'
    # Display the pause message with section details
    info_output.append_stdout(f"Section {section}       Difficulty: {difficulty.title()}      Time allowed: {time_allowed}s")
    # Pause for 4 seconds to allow the user to read the message
    time.sleep(4)
    # Clear test output
    test_output.outputs = []
    # Hide information output after displaying the message
    info_output.layout.visibility = 'hidden'
    # Show the test output again for the next section
    test_output.layout.display = 'block'
    # Clear the pause message from the info output
    info_output.outputs = []
    # Reset the response flag for the next section
    RESPONDED = False
    # Indicate the pause is over
    PAUSED = False
    # Update the remaining time
    time_remaining -= 1
    # Record the event in the global event information dictionary
    change_dict_data(qas_dict, ['question', 'answer', 'is_correct', 'time_taken'],
                     [difficulty, difficulty, difficulty, difficulty], 'append')
    change_dict_data(event_info_dict, ["type", "description", "time"],
                     ['test', difficulty, time.asctime(time.localtime(time.time()))], "append")
    return time_remaining


def metrics(time_output, difficulty_output, accuracy_output, test_output, info_output, allowed_time=180):
    """
    Monitors and updates the test's metrics in real-time, including the remaining time,
    current difficulty, and accuracy. It also handles the transition between test sections.

    Parameters:
        time_output (Output widget): Widget for displaying the remaining time.
        difficulty_output (Output widget): Widget for indicating the current difficulty level.
        accuracy_output (Output widget): Widget for showing the user's accuracy.
        test_output (Output widget): Main widget for test content.
        info_output (Output widget): Widget for displaying informational messages.
        allowed_time (int): Total time allowed for the test. Please use an allowed_time that is divisible by 3.

    Returns:
        None
    """
    global DIFFICULTY, PAUSED, RESPONDED
    time_remaining = allowed_time
    # Continuously update and display test metrics until time runs out
    while time_remaining > 0:
        # Difficulty Adjustment & Display
        if time_remaining == allowed_time:
            PAUSED = True
            DIFFICULTY = "easy"
            difficulty_output.append_stdout("\rDifficulty:" + " " + DIFFICULTY.title())
        elif time_remaining == 2 * allowed_time / 3:
            PAUSED = True
            DIFFICULTY = "medium"
            universal_callback("force")
            accuracy_output.outputs = []
            difficulty_output.append_stdout("\rDifficulty:" + " " + DIFFICULTY.title())
        elif time_remaining == allowed_time / 3:
            PAUSED = True
            DIFFICULTY = "hard"
            universal_callback('force')
            accuracy_output.outputs = []
            difficulty_output.outputs = []
            difficulty_output.append_stdout("\rDifficulty:" + " " + DIFFICULTY.title())

        # Timer & Accuracy Display
        if DIFFICULTY == "easy":
            easy_time_left = time_remaining - 2 * allowed_time / 3
            time_output.append_stdout("\rTime Left:" + " " + str(int(easy_time_left)) + " " + "seconds")
            accuracy_output.append_stdout(
                f"\rAccuracy: {accuracy_dict['easy_correct']} / {accuracy_dict['easy_total']}")
        elif DIFFICULTY == "medium":
            medium_time_left = time_remaining - 1 * allowed_time / 3
            time_output.append_stdout("\rTime Left:" + " " + str(int(medium_time_left)) + " " + "seconds")
            accuracy_output.append_stdout(
                f"\rAccuracy: {accuracy_dict['medium_correct']} / {accuracy_dict['medium_total']}")
        elif DIFFICULTY == "hard":
            time_output.append_stdout("\rTime Left:" + " " + str(int(time_remaining)) + " " + "seconds")
            accuracy_output.append_stdout(
                f"\rAccuracy: {accuracy_dict['hard_correct']} / {accuracy_dict['hard_total']}")

        # Between-Section Pause
        if PAUSED and DIFFICULTY == "easy":
            time_remaining = pause_display(1, 'easy', 60, time_remaining, test_output, info_output)
        elif PAUSED and DIFFICULTY == "medium":
            time_remaining = pause_display(2, 'medium', 60, time_remaining, test_output, info_output)
        elif PAUSED and DIFFICULTY == "hard":
            time_remaining = pause_display(3, 'hard', 60, time_remaining, test_output, info_output)
        else:
            time.sleep(1)
            time_remaining -= 1
    # Clear outputs and force submit to end the test when time runs out
    DIFFICULTY = "end"
    universal_callback('force')
    info_output.layout.display = 'none'
    test_output.layout.display = 'none'
    difficulty_output.layout.display = 'none'
    time_output.outputs = []
    time_output.layout.display = 'none'
    accuracy_output.outputs = []
    accuracy_output.layout.display = 'none'
    return


def generate_question_parts(previous_parts, lower_limit, upper_limit, symbols_dict):
    """
        Generates a unique part of a mathematical question to avoid repetition.

        Parameters:
            previous_parts (list): A list of question parts already generated.
            lower_limit (int): The minimum value for the generated number.
            upper_limit (int): The maximum value for the generated number.
            symbols_dict (list): A list of symbols to use in generating question parts.

        Returns:
            tuple: A tuple containing the generated expression part, symbol, and number.
    """
    while True:
        # Generate a random number within the limits
        number = random.randint(lower_limit, upper_limit)
        # Randomly choose a symbol from the list
        symbol = random.choice(symbols_dict)
        if symbol == "×":
            # Use '*' for multiplication in the expression
            real_symbol = "*"
        elif symbol == "÷":
            # Use '/' for division in the expression
            real_symbol = "/"
        else:
            real_symbol = symbol
        # Form the expression part
        expression_part = real_symbol + str(number)
        # Ensure uniqueness
        if expression_part not in previous_parts:
            # Return the new unique expression part
            return expression_part, symbol, number


def answer_checker(current_expression, text_input, difficulty):
    """
        Checks the user's answer against the correct answer and updates accuracy metrics.

        Parameters:
            current_expression (str): The mathematical expression to evaluate for the correct answer.
            text_input (Text widget): The widget where the user enters their answer.
            difficulty (str): The current difficulty level of the question.

        Returns:
            None
    """
    if difficulty == 'easy':
        correct = 'easy_correct'
        total = 'easy_total'
    elif difficulty == 'medium':
        correct = 'medium_correct'
        total = 'medium_total'
    elif difficulty == 'hard':
        correct = 'hard_correct'
        total = 'hard_total'
    # Evaluate the expression to get the correct answer
    current_answer = eval(current_expression)
    start_time = time.time()
    wait_for("response")
    end_time = time.time()
    # Calculate the time taken to answer
    time_taken = end_time - start_time
    accuracy_dict[total] += 1
    # Fixes the issue when there is a non-int input/force submit
    try:
        # Attempt to convert the answer to an integer
        answer_value = int(text_input.value)
    except ValueError:
        # Keep the answer as-is if conversion fails
        answer_value = text_input.value
    if int(current_answer) == answer_value:
        is_correct = True
        accuracy_dict[correct] += 1
    else:
        is_correct = False
    # Store the question, answer, correctness, and time taken in the qas_dict
    change_dict_data(qas_dict, ['question', 'answer', 'is_correct', 'time_taken'],
                     [current_expression, answer_value, is_correct, time_taken], 'append')
    return


def test(difficulty, test_output, n_loop, sleep_time, lower_limit, upper_limit, symbols_dict):
    """
        Executes the test logic for a specific difficulty level. It dynamically generates
        questions, displays them to the user, and evaluates the answers provided.

        Parameters:
            difficulty (str): The current difficulty level ('easy', 'medium', 'hard').
            test_output (Output widget): Widget for displaying the questions and collecting answers.
            n_loop (int): Number of operations/questions per test section.
            sleep_time (int): Time in seconds to wait before showing the next part of the question.
            lower_limit (int): Lower bound for the numbers used in questions.
            upper_limit (int): Upper bound for the numbers used in questions.
            symbols_dict (list): Mathematical operators used in the current difficulty level.

        Returns:
            None
    """
    global DIFFICULTY, PAUSED, RESPONDED
    # Ensure the test runs only for the current difficulty level and is not paused
    while DIFFICULTY == difficulty and PAUSED == False:
        with test_output:
            number_0 = random.randint(lower_limit, upper_limit)
            clear_output(wait=False)
            display(HTML(f"<h1 align='center'>{number_0}</h1>"))
            # Initialize an expression for the current question
            current_expression = str(number_0)
        previous_parts = []
        # Loop to construct a multi-part question
        for i in range(n_loop):
            expression_part, symbol, number = generate_question_parts(previous_parts, lower_limit, upper_limit, symbols_dict)
            previous_parts.append(expression_part)
            current_expression = "(" + current_expression + ")" + expression_part
            if RESPONDED:
                break
            time.sleep(sleep_time)
            with test_output:
                clear_output(wait=False)
                display(HTML(f"<h1 align='center'>{symbol}{number}</h1>"))
        if RESPONDED:
            break
        # After displaying all parts, collect and evaluate the user's answer
        with test_output:
            text_input = widgets.Text(description="Answer:", placeholder="Press Enter to submit",
                                      continuous_update=False)
            text_box = widgets.HBox([text_input], layout=widgets.Layout(justify_content='center'))
            text_input.observe(universal_callback, names='value')
            display(text_box)
        answer_checker(current_expression, text_input, difficulty)
    return


def main_test(test_output):
    """
    Executes the main test logic, presenting questions and collecting answers across different difficulty levels.

    Parameters:
        test_output (Output widget): The widget used to display test questions and collect answers.

    Returns:
        None
    """
    global DIFFICULTY, PAUSED, RESPONDED

    # Wait for the initial pause to end before starting
    wait_for("pause")
    random.seed(1)  # Setting Seed
    # Execute the test for each difficulty level with specified parameters
    test('easy', test_output, 3, 1, 1, 10, ["+", "-"])
    # Wait between difficulty levels
    wait_for("pause")
    random.seed(2)  # Re-seed for the medium difficulty
    test('medium', test_output, 2, 2, 5, 15, ["+", "-", "×"])
    # Final wait before the hard section
    wait_for("pause")
    random.seed(3)  # Re-seed for the hard difficulty
    test('hard', test_output, 2, 3, 10, 20, ["+", "-", "×"])
    # Reset the responded flag after the test is complete
    RESPONDED = False
    return


def score(accuracy_dict):
    """
    Calculates the weighted score based on the accuracy of answers across different difficulty levels.

    Parameters:
        accuracy_dict (dict): A dictionary containing the correct counts and total questions for each difficulty level.

    Returns:
        int: The calculated weighted score.
    """
    # Calculate the score with weights: 1 for easy, 3 for medium, and 5 for hard questions
    score = accuracy_dict['easy_correct'] + 3 * accuracy_dict['medium_correct'] + 5 * accuracy_dict['hard_correct']
    return score


# DATA UPLOAD
def send_to_google_form(data_dict, form_url):
    """
    Uploads the collected test data to a specified Google Form.

    Parameters:
        data_dict (dict): The dictionary containing test data and user responses.
        form_url (str): The URL of the Google Form where data will be uploaded.

    Returns:
        bool: True if the upload was successful, False otherwise.
    """
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
