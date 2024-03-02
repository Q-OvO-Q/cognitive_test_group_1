import time
import random
import requests
import json
import ipywidgets as widgets
from jupyter_ui_poll import ui_events
from IPython.display import display, clear_output, HTML
from bs4 import BeautifulSoup

# Setting Seed
random.seed(2)

# VARIABLES
event_info_dict = {'type': ["start", ], 'description': ["program started", ],
                   'time': [time.asctime(time.localtime(time.time())), ]}
accuracy_dict = {'easy_correct': 0, 'easy_total': 0, 'medium_correct': 0, 'medium_total': 0, 'hard_correct': 0,
                 'hard_total': 0}
qas_dict = {'question': [], 'answer': [], 'is_correct': [], 'time_taken': []}
RESPONDED = False
PAUSED = False
DIFFICULTY = ""


# INTERACTIONS
def wait_for_response(timeout=-1.0, interval=0.001, max_rate=20.0, allow_interrupt=True):
    global RESPONDED
    start_wait = time.time()
    n_proc = int(max_rate * interval) + 1
    with ui_events() as ui_poll:
        keep_looping = True
        while keep_looping == True:
            ui_poll(n_proc)
            if (timeout != -1.0) and (time.time() > start_wait + timeout):
                keep_looping = False
            if allow_interrupt == True and RESPONDED == True:
                keep_looping = False
            time.sleep(interval)
    RESPONDED = False
    return


def register_button(btn):
    """Callback function for button widget click event"""
    global RESPONDED
    event_info_dict['type'].append("button_click")
    event_info_dict['description'].append(btn.description)
    event_info_dict['time'].append(time.asctime(time.localtime(time.time())))
    RESPONDED = True
    return


def register_text(change):
    """Callback function for text widget change event"""
    global RESPONDED
    event_info_dict['type'].append("text_submit")
    event_info_dict['description'].append(change['new'])
    event_info_dict['time'].append(time.asctime(time.localtime(time.time())))
    RESPONDED = True
    return


def register_dropdown(change):
    """Callback function for dropdown widget change event"""
    global RESPONDED
    event_info_dict['type'].append("dropdown_select")
    event_info_dict['description'].append(change['new'])
    event_info_dict['time'].append(time.asctime(time.localtime(time.time())))
    RESPONDED = True
    return


def force_submit():
    """Stop wait_for_response function"""
    global RESPONDED
    event_info_dict['type'].append("force_submit")
    event_info_dict['description'].append("time out")
    event_info_dict['time'].append(time.asctime(time.localtime(time.time())))
    RESPONDED = True
    return


# TEST
def wait_for_pause(timeout=-1.0, interval=0.001, max_rate=20.0, allow_interrupt=True):
    global PAUSED
    start_wait = time.time()
    n_proc = int(max_rate * interval) + 1
    with ui_events() as ui_poll:
        keep_looping = True
        while keep_looping == True:
            ui_poll(n_proc)
            if (timeout != -1.0) and (time.time() > start_wait + timeout):
                keep_looping = False
            if allow_interrupt == True and PAUSED == False:
                keep_looping = False
            time.sleep(interval)
    return


def metrics(time_output, difficulty_output, accuracy_output, test_output, info_output, allowed_time=180):
    """Display & update test metrics in real-time"""
    # Please use an allowed_time that is divisible by 3
    global DIFFICULTY, PAUSED, RESPONDED
    time_remaining = allowed_time

    while time_remaining > 0:
        # Difficulty Adjustment & Display
        if time_remaining == allowed_time:
            PAUSED = True
            DIFFICULTY = "Easy"
            difficulty_output.append_stdout("\rDifficulty:" + " " + DIFFICULTY)
        elif time_remaining == 2 * allowed_time / 3:
            PAUSED = True
            DIFFICULTY = "Medium"
            force_submit()
            difficulty_output.append_stdout("\rDifficulty:" + " " + DIFFICULTY)
        elif time_remaining == allowed_time / 3:
            PAUSED = True
            DIFFICULTY = "Hard"
            force_submit()
            difficulty_output.outputs = []
            difficulty_output.append_stdout("\rDifficulty:" + " " + DIFFICULTY)

        # Timer & Accuracy Display
        if DIFFICULTY == "Easy":
            easy_time_left = time_remaining - 2 * allowed_time / 3
            time_output.append_stdout("\rTime Left:" + " " + str(int(easy_time_left)) + " " + "seconds")
            accuracy_output.append_stdout(
                f"\rAccuracy: {accuracy_dict['easy_correct']} / {accuracy_dict['easy_total']}")
        elif DIFFICULTY == "Medium":
            medium_time_left = time_remaining - 1 * allowed_time / 3
            time_output.append_stdout("\rTime Left:" + " " + str(int(medium_time_left)) + " " + "seconds")
            accuracy_output.append_stdout(
                f"\rAccuracy: {accuracy_dict['medium_correct']} / {accuracy_dict['medium_total']}")
        elif DIFFICULTY == "Hard":
            time_output.append_stdout("\rTime Left:" + " " + str(int(time_remaining)) + " " + "seconds")
            accuracy_output.append_stdout(
                f"\rAccuracy: {accuracy_dict['hard_correct']} / {accuracy_dict['hard_total']}")

        # Between-Section Pause
        if PAUSED and DIFFICULTY == "Easy":
            info_output.append_stdout("Section 1       Difficulty: Easy      Time allowed: 60s")
            time.sleep(4)
            info_output.layout.visibility = 'hidden'
            info_output.outputs = []
            RESPONDED = False
            PAUSED = False
            time_remaining -= 1
            event_info_dict['type'].append("start")
            event_info_dict['description'].append("easy")
            event_info_dict['time'].append(time.asctime(time.localtime(time.time())))
            qas_dict['question'].append('easy')
            qas_dict['answer'].append('easy')
            qas_dict['is_correct'].append('easy')
            qas_dict['time_taken'].append('easy')
        elif PAUSED and DIFFICULTY == "Medium":
            test_output.layout.display = 'none'
            info_output.layout.visibility = 'visible'
            info_output.append_stdout("Section 2       Difficulty: Medium      Time allowed: 60s")
            time.sleep(4)
            test_output.outputs = []
            info_output.layout.visibility = 'hidden'
            test_output.layout.display = 'block'
            info_output.outputs = []
            RESPONDED = False
            PAUSED = False
            time_remaining -= 1
            event_info_dict['type'].append("start")
            event_info_dict['description'].append("medium")
            event_info_dict['time'].append(time.asctime(time.localtime(time.time())))
            qas_dict['question'].append('medium')
            qas_dict['answer'].append('medium')
            qas_dict['is_correct'].append('medium')
            qas_dict['time_taken'].append('medium')
        elif PAUSED and DIFFICULTY == "Hard":
            test_output.layout.display = 'none'
            info_output.layout.visibility = 'visible'
            info_output.append_stdout("Section 3       Difficulty: Hard      Time allowed: 60s")
            time.sleep(4)
            test_output.outputs = []
            info_output.layout.display = 'hidden'
            test_output.layout.display = 'block'
            info_output.outputs = []
            RESPONDED = False
            PAUSED = False
            time_remaining -= 1
            event_info_dict['type'].append("start")
            event_info_dict['description'].append("hard")
            event_info_dict['time'].append(time.asctime(time.localtime(time.time())))
            qas_dict['question'].append('hard')
            qas_dict['answer'].append('hard')
            qas_dict['is_correct'].append('hard')
            qas_dict['time_taken'].append('hard')
        else:
            time.sleep(1)
            time_remaining -= 1
    DIFFICULTY = "End"
    force_submit()
    info_output.layout.display = 'none'
    test_output.layout.display = 'none'
    time.sleep(2)
    event_info_dict['type'].append("end")
    event_info_dict['description'].append("end")
    event_info_dict['time'].append(time.asctime(time.localtime(time.time())))
    qas_dict['question'].append('end')
    qas_dict['answer'].append('end')
    qas_dict['is_correct'].append('end')
    qas_dict['time_taken'].append('end')
    difficulty_output.layout.display = 'none'
    time_output.outputs = []
    time_output.layout.display = 'none'
    accuracy_output.outputs = []
    accuracy_output.layout.display = 'none'
    return


def test(test_output):
    """Carrying out test with 3 difficulties and answer checking"""
    global DIFFICULTY, PAUSED, RESPONDED
    wait_for_pause()

    while DIFFICULTY == "Easy" and PAUSED == False:
        with test_output:
            number_0 = random.randint(1, 10)
            clear_output(wait=False)
            display(HTML(f"<h1 align='center'>{number_0}</h1>"))
            current_expression = str(number_0)
        for i in range(3):
            number = random.randint(1, 10)
            symbol = random.choice(["+", "-"])
            if RESPONDED:
                break
            if symbol == "×":
                real_symbol = "*"
            else:
                real_symbol = symbol
            current_expression = "(" + current_expression + ")" + real_symbol + str(number)
            time.sleep(1)
            with test_output:
                clear_output(wait=False)
                display(HTML(f"<h1 align='center'>{symbol}{number}</h1>"))
        if RESPONDED:
            break
        with test_output:
            text_input = widgets.Text(description="Answer:", placeholder="Press Enter to submit",
                                      continuous_update=False)
            text_box = widgets.HBox([text_input], layout=widgets.Layout(justify_content='center'))
            text_input.observe(register_text, names='value')
            display(text_box)
        current_answer = eval(current_expression)
        qas_dict['question'].append(current_expression)
        start_time = time.time()
        wait_for_response()
        end_time = time.time()
        time_taken = end_time - start_time
        qas_dict['time_taken'].append(time_taken)
        accuracy_dict['easy_total'] += 1
        # Fixes the issue when there is a non-int input/force submit
        try:
            answer_value = int(text_input.value)
        except ValueError:
            answer_value = 'error'
        if int(current_answer) == answer_value:
            qas_dict['answer'].append(answer_value)
            qas_dict['is_correct'].append(True)
            accuracy_dict['easy_correct'] += 1
        else:
            wrong_input = text_input.value
            qas_dict['answer'].append(wrong_input)
            qas_dict['is_correct'].append(False)

    wait_for_pause()

    while DIFFICULTY == "Medium" and PAUSED == False:
        with test_output:
            number_0 = random.randint(5, 15)
            clear_output(wait=False)
            display(HTML(f"<h1 align='center'>{number_0}</h1>"))
            current_expression = str(number_0)
        for i in range(2):
            number = random.randint(5, 15)
            symbol = random.choice(["+", "-", "×"])
            if RESPONDED:
                break
            if symbol == "×":
                real_symbol = "*"
            else:
                real_symbol = symbol
            current_expression = "(" + current_expression + ")" + real_symbol + str(number)
            time.sleep(2)
            with test_output:
                clear_output(wait=False)
                display(HTML(f"<h1 align='center'>{symbol}{number}</h1>"))
        if RESPONDED:
            break
        with test_output:
            text_input = widgets.Text(description="Answer:", placeholder="Press Enter to submit",
                                      continuous_update=False)
            text_box = widgets.HBox([text_input], layout=widgets.Layout(justify_content='center'))
            text_input.observe(register_text, names='value')
            display(text_box)
        current_answer = eval(current_expression)
        qas_dict['question'].append(current_expression)
        start_time = time.time()
        wait_for_response()
        end_time = time.time()
        time_taken = end_time - start_time
        qas_dict['time_taken'].append(time_taken)
        accuracy_dict['medium_total'] += 1
        # Fixes the issue when there is a non-int input/force submit
        try:
            answer_value = int(text_input.value)
        except ValueError:
            answer_value = 'error'
        if int(current_answer) == answer_value:
            qas_dict['answer'].append(answer_value)
            qas_dict['is_correct'].append(True)
            accuracy_dict['medium_correct'] += 1
        else:
            wrong_input = text_input.value
            qas_dict['answer'].append(wrong_input)
            qas_dict['is_correct'].append(False)

    wait_for_pause()

    while DIFFICULTY == "Hard" and PAUSED == False:
        with test_output:
            number_0 = random.randint(10, 20)
            clear_output(wait=False)
            display(HTML(f"<h1 align='center'>{number_0}</h1>"))
            current_expression = str(number_0)
        for i in range(2):
            number = random.randint(10, 20)
            symbol = random.choice(["+", "-", "×"])
            if RESPONDED:
                break
            if symbol == "×":
                real_symbol = "*"
            else:
                real_symbol = symbol
            current_expression = "(" + current_expression + ")" + real_symbol + str(number)
            time.sleep(3)
            with test_output:
                clear_output(wait=False)
                display(HTML(f"<h1 align='center'>{symbol}{number}</h1>"))
        if RESPONDED:
            break
        with test_output:
            text_input = widgets.Text(description="Answer:", placeholder="Press Enter to submit",
                                      continuous_update=False)
            text_box = widgets.HBox([text_input], layout=widgets.Layout(justify_content='center'))
            text_input.observe(register_text, names='value')
            display(text_box)
        current_answer = eval(current_expression)
        qas_dict['question'].append(current_expression)
        start_time = time.time()
        wait_for_response()
        end_time = time.time()
        time_taken = end_time - start_time
        qas_dict['time_taken'].append(time_taken)
        accuracy_dict['hard_total'] += 1
        # Fixes the issue when there is a non-int input/force submit
        try:
            answer_value = int(text_input.value)
        except ValueError:
            answer_value = 'error'
        if int(current_answer) == answer_value:
            qas_dict['answer'].append(answer_value)
            qas_dict['is_correct'].append(True)
            accuracy_dict['hard_correct'] += 1
        else:
            wrong_input = text_input.value
            qas_dict['answer'].append(wrong_input)
            qas_dict['is_correct'].append(False)
    RESPONDED = False
    return


def score():
    """Calculate weighted score"""
    score = accuracy_dict['easy_correct'] + 3 * accuracy_dict['medium_correct'] + 5 * accuracy_dict['hard_correct']
    return score


# DATA UPLOAD
def send_to_google_form(data_dict, form_url):
    """Upload information to a corresponding Google form"""
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
