import sys
if 'functions' in sys.modules:
    del sys.modules['functions']

from functions import *
import pandas as pd
from pathlib import Path
import threading

# Variables
upload_dict = {
    'id': '',
    'gender': '',
    'age': '',
    'rating': '',
    'score': '',
    'accuracy_json': '',
    'qas_json': '',
    'event_info_json': '',
}

form_url = ('https://docs.google.com/forms/d/e/1FAIpQLSdTEaRV3qHAUx93GQDgvkBdkrO0zCMzn__yAbDKd1vaKYE0Lg/viewform?usp'
            '=sf_link')
gsheetkey = "1fMYFR8SSEZxlaJX6QW5qPwJbHzlCacz3vQKX6ioHU6w"
sheet_url = f"https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx"

# Data Consent Information
display(HTML("<h1 align='center'>Data Consent Information</h1>"))
display(HTML("""
<p style="text-align: center; font-size: 18px">
We wish to record your response data to an anonymized public data repository.<br>
Your data will be used for educational teaching purposes practising data analysis and visualisation.<br>
If you do not want your data to be used, please close this program immediately.<br>
Otherwise, press "Agree Statement" to continue.
</p>
"""))

agree_button = widgets.Button(description="Agree Statement")
agree_button_box = widgets.HBox([agree_button], layout=widgets.Layout(justify_content='center'))
agree_button.on_click(register_button)
display(agree_button_box)
wait_for_response()

clear_output(wait=False)

# Info Collection
display(HTML("""
<h1 align='center'>
To start, we need to collect a few information from you.
</h1>
"""))
display(HTML("""
<p style="text-align: center; font-size: 22px">
First is your anonymized id. Look at the guidance below.
</p>
"""))
display(HTML("""
<div style='display: flex; justify-content: center;'>
  <ul style='text-align: left; font-size: 18px; list-style-position: inside;'>
    <li>first two letters base on the initials (first and last name) of a childhood friend</li>
    <li>last two letters base on the initials (first and last name) of a favourite actor / actress</li>
    <li>if your friend was called Charlie Brown and film star was Tom Cruise, then your ID would be CBTC
  </ul>
</div>
"""))
id_input = widgets.Text(description="ID: ", placeholder="Please enter your anonymized id", continuous_update=False)
id_box = widgets.HBox([id_input], layout=widgets.Layout(justify_content='center'))
id_input.observe(register_text, names='value')
display(id_box)
wait_for_response()
userid = id_input.value
upload_dict['id'] = userid
clear_output(wait=False)
display(HTML("""
<p style="text-align: center; font-size: 22px">
Then your gender.
</p>
"""))
gender_dropdown = widgets.Dropdown(options=['Male', 'Female', 'Other'], description="Gender: ", value=None)
gender_box = widgets.HBox([gender_dropdown], layout=widgets.Layout(justify_content='center'))
gender_dropdown.observe(register_dropdown, names='value')
display(gender_box)
wait_for_response()
gender = gender_dropdown.value
upload_dict['gender'] = gender
clear_output(wait=False)
display(HTML("""
<p style="text-align: center; font-size: 22px">
Finally your age.
</p>
"""))
age_input = widgets.Text(description="Age: ", placeholder="Please enter your age", continuous_update=False)
age_box = widgets.HBox([age_input], layout=widgets.Layout(justify_content='center'))
age_input.observe(register_text, names='value')
display(age_box)
wait_for_response()
age = age_input.value
upload_dict['age'] = age
clear_output(wait=False)
display(HTML("""
<p style="text-align: center; font-size: 22px">
Thanks for providing the information. Now let's start the test.
</p>
"""))
time.sleep(3)
clear_output(wait=False)

# Start
display(HTML("<h1 align='center'>Welcome to Math Ability Test</h1>"))
display(HTML("""
<div style='display: flex; justify-content: center;'>
  <ul style='text-align: left; font-size: 18px; list-style-position: inside;'>
    <li>The test will last for 3 minutes with 1 minute for each section.</li>
    <li>The difficulty of questions will be different in each section, from easy to hard.</li>
    <li>You will need to perform a sequence of calculations and provide the answer.</li>
    <li>Each part of the calculation is only shown for a short period of time and then hidden.</li>
    <li>Perform calculations SEQUENTIALLY rather than following standard arithmetic precedence rules.</li>
    <li>There is no upper limit for the score. The more correct ones, the higher the score.</li>
    <li>DO NOT USE CALCULATORS FOR HELP.</li>
  </ul>
</div>
"""))
display(HTML("""<h3 align='center'>When you are ready, click "Start Test" to continue!</h3>"""))

start_button = widgets.Button(description="Start Test")
start_button_box = widgets.HBox([start_button], layout=widgets.Layout(justify_content='center'))
start_button.on_click(register_button)
display(start_button_box)
wait_for_response()

clear_output(wait=False)

# Test
test_output = widgets.Output()
time_output = widgets.Output()
difficulty_output = widgets.Output()
accuracy_output = widgets.Output()
info_output = widgets.Output()
display(time_output, difficulty_output, accuracy_output, test_output, info_output)

metrics_thread = threading.Thread(target=metrics,
                                  args=(time_output, difficulty_output, accuracy_output, test_output, info_output))
metrics_thread.start()
test(test_output)

# End of Test
clear_output(wait=False)
display(HTML("<h1 align='center'>Congratulations on finishing your test!</h1>"))
time.sleep(1)
display(HTML("""
<p style="text-align: center; font-size: 22px">
How do you feel about the test?
</p>
"""))
time.sleep(1)
rating_btn1 = widgets.Button(description="Too Hard")
rating_btn2 = widgets.Button(description="Just Right")
rating_btn3 = widgets.Button(description="Too Easy")
rating_buttons_box = widgets.HBox([rating_btn1, rating_btn2, rating_btn3],
                                  layout=widgets.Layout(justify_content='center'))
rating_btn1.on_click(register_button)
rating_btn2.on_click(register_button)
rating_btn3.on_click(register_button)
display(rating_buttons_box)
wait_for_response()
rating = event_info_dict['description'][-1]
upload_dict['rating'] = rating

clear_output(wait=False)
display(HTML("<h1 align='center'>Thanks for your feedback!</h1>"))
time.sleep(1)

clear_output(wait=False)
display(
    HTML('<p style="text-align: center; font-size: 22px">Calculating and uploading your result, please wait......</p>'))
score = score()
upload_dict['score'] = score
accuracy_df = pd.DataFrame([accuracy_dict])
upload_dict['accuracy_json'] = accuracy_df.to_json()
qas_df = pd.DataFrame(qas_dict)
upload_dict['qas_json'] = qas_df.to_json()
event_info_df = pd.DataFrame(event_info_dict)
upload_dict['event_info_json'] = event_info_df.to_json()
try:
    upload_status = send_to_google_form(upload_dict, form_url)
except Exception:
    clear_output(wait=False)
    display(HTML('<p style="text-align: center; font-size: 22px">Sorry, an error occurred. Trying to upload '
                 'again......</p>'))
    try:
        upload_status = send_to_google_form(upload_dict, form_url)
    except Exception:
        clear_output(wait=False)
        display(HTML('<p style="text-align: center; font-size: 22px">Upload unsuccessful. Check your internet '
                     'connection.</p>'))
        display(HTML(f"<p style='text-align: center; font-size: 18px'>Your score in this test is {score}.</p>"))
        path = Path('upload.json')
        contents = json.dumps(upload_dict)
        path.write_text(contents)
        display(HTML('<p style="text-align: center; font-size: 18px">Please manually send the generated upload.json '
                     'within the same directory to zcbtdc5@ucl.ac.uk. Thank you.</p>'))
        raise (Exception("Upload Error"))

display(HTML('<p style="text-align: center; font-size: 22px">Upload successful!</p>'))
display(HTML('<p style="text-align: center; font-size: 22px">Ranking you with other people......</p>'))

ranking_df = pd.read_excel(sheet_url, usecols='B, F')
rankings = ranking_df['score'].rank(method='min', ascending=False)
ranking = rankings[ranking_df['score'] == score].iloc[0]
total_entries = len(ranking_df)
max_value = ranking_df['score'].max()

time.sleep(2)
clear_output(wait=False)
display(HTML(f"<h1 align='center'>Well done, {userid}!</h1>"))
display(HTML(f"<p style='text-align: center; font-size: 18px'>Your score in this test is {score}.<br>You are ranked "
             f"{ranking:.0f} out of {total_entries} testees.<br>Currently the highest score is {max_value}.<br>"
             f"Feel free to try the test again for a better result!</p>"))
