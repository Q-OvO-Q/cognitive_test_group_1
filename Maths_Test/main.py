import sys

# Remove 'functions' from sys.modules to allow for fresh imports without restarting the kernel
if 'functions' in sys.modules:
    del sys.modules['functions']
# Import other necessary libraries
from functions import *
import pandas as pd
from pathlib import Path
import threading

# Initialize variables for uploading results
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

# URLs for the Google Form and spreadsheet where data will be uploaded
form_url = ('https://docs.google.com/forms/d/e/1FAIpQLScaxcOPokvA1dnhVaPRZEsD7pcmEcRXx1aGRwr6djMedj1XOA/viewform?usp'
            '=sf_link')
gsheetkey = "1GkHgcYAcW2cWCCSbmS5_3iwq0FVxu5M__ZC-bSydgAY"
sheet_url = f"https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx"

# Display data consent information using HTML
display(HTML("<h1 align='center'>Data Consent Information</h1>"))
display(HTML("""
<p style="text-align: center; font-size: 18px">
We wish to record your response data to an anonymized public data repository.<br>
Your data will be used for educational teaching purposes practising data analysis and visualisation.<br>
If you do not want your data to be used, please close this program immediately.<br>
Otherwise, press "Agree Statement" to continue.
</p>
"""))

# Setup and display the 'Agree Statement' button
agree_button = widgets.Button(description="Agree Statement")
agree_button_box = widgets.HBox([agree_button], layout=widgets.Layout(justify_content='center'))
agree_button.on_click(universal_callback)
display(agree_button_box)
wait_for("response")
clear_output(wait=False)

# Collect personal information from the user with additional validations

# Personal Info Collection Information
display(HTML("""<h1 align='center'>To start, we need to collect a few information from you.</h1>"""))

display(HTML("""
<p style="text-align: center; font-size: 22px">
First is your anonymized id. Look at the guidance below.
</p>
"""))

# Collecting the user's anonymized ID with guidance displayed in HTML format
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
id_input.observe(universal_callback, names='value')
display(id_box)
# Loop until a valid ID is entered according to the specified criteria
while True:
    wait_for("response")
    if len(id_input.value) == 4 and id_input.value.isalpha():
        break
    else:
        display(HTML("""
        <p style="text-align: center; font-size: 18px">
        Invalid input. Please only enter 4-digit characters.
        </p>
        """))
upload_dict['id'] = id_input.value.upper()
clear_output(wait=False)

# Collecting user's gender
display(HTML("""<p style="text-align: center; font-size: 22px">Then your gender.</p>"""))
gender_dropdown = widgets.Dropdown(options=['Male', 'Female', 'Other'], description="Gender: ", value=None)
gender_box = widgets.HBox([gender_dropdown], layout=widgets.Layout(justify_content='center'))
gender_dropdown.observe(universal_callback, names='value')
display(gender_box)
wait_for("response")
upload_dict['gender'] = gender_dropdown.value
clear_output(wait=False)

# Collecting user's age with validation
display(HTML("""<p style="text-align: center; font-size: 22px">Finally your age.</p>"""))
age_input = widgets.Text(description="Age: ", placeholder="Please enter your age", continuous_update=False)
age_box = widgets.HBox([age_input], layout=widgets.Layout(justify_content='center'))
age_input.observe(universal_callback, names='value')
display(age_box)
while True:
    wait_for("response")
    try:
        age = int(age_input.value)
        if 0 <= age <= 120:
            break
        else:
            display(HTML("""<p style="text-align: center; font-size: 18px">Age out of valid range.</p>"""))
    except ValueError:
        display(HTML("""<p style="text-align: center; font-size: 18px">Invalid input: not a number.</p>"""))
upload_dict['age'] = age_input.value
clear_output(wait=False)

# Proceed to the test introduction and setup

# Thank the user for providing information and indicate the start of the test
display(HTML("""
<p style="text-align: center; font-size: 22px">
Thanks for providing the information. Now let's start the test.
</p>
"""))
# Short pause before clearing the output for the test introduction
time.sleep(3)
clear_output(wait=False)

# Display the test instructions
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

# Start Test Button
start_button = widgets.Button(description="Start Test")
start_button_box = widgets.HBox([start_button], layout=widgets.Layout(justify_content='center'))
start_button.on_click(universal_callback)
display(start_button_box)
# Wait for the user to click the "Start Test" button before proceeding
wait_for("response")
clear_output(wait=False)

# Set up the outputs for the test environment
test_output = widgets.Output()
time_output = widgets.Output()
difficulty_output = widgets.Output()
accuracy_output = widgets.Output()
info_output = widgets.Output()
display(time_output, difficulty_output, accuracy_output, test_output, info_output)

# Initialize and start a separate thread for test metrics to run alongside the test
metrics_thread = threading.Thread(target=metrics,
                                  args=(time_output, difficulty_output, accuracy_output, test_output, info_output))
# Begin the test metrics in parallel with the test itself
metrics_thread.start()
# Start the main test function, displaying questions and collecting answers
main_test(test_output)

# The section above initiates the test, providing users with instructions and a start button. Once started,
# it dynamically updates the display with the test progress, including time left, difficulty level and accuracy.

# Test End
change_dict_data(qas_dict, ['question', 'answer', 'is_correct', 'time_taken'],
                 ['end', 'end', 'end', 'end'], 'append')
change_dict_data(event_info_dict, ["type", "description", "time"],
                 ['test', 'end', time.asctime(time.localtime(time.time()))], "append")

# After completing the test, collect feedback and process the results

# Congratulating the user on completing the test
clear_output(wait=False)
display(HTML("<h1 align='center'>Congratulations on finishing your test!</h1>"))
time.sleep(1)
# Asking for the user's feedback on the test
display(HTML("""<p style="text-align: center; font-size: 22px">How do you feel about the test?</p>"""))
time.sleep(1)

# Setting up and displaying rating buttons for feedback collection
rating_btn1 = widgets.Button(description="Too Hard")
rating_btn2 = widgets.Button(description="Just Right")
rating_btn3 = widgets.Button(description="Too Easy")
rating_buttons_box = widgets.HBox([rating_btn1, rating_btn2, rating_btn3],
                                  layout=widgets.Layout(justify_content='center'))
rating_btn1.on_click(universal_callback)
rating_btn2.on_click(universal_callback)
rating_btn3.on_click(universal_callback)
display(rating_buttons_box)
# Waiting for the user to select their rating
wait_for("response")
# Storing the user's feedback
upload_dict['rating'] = button_description['description']
# Displaying a thank-you message and preparing to calculate and upload the results
clear_output(wait=False)
display(HTML("<h1 align='center'>Thanks for your feedback!</h1>"))
time.sleep(1)

clear_output(wait=False)
display(
    HTML('<p style="text-align: center; font-size: 22px">Calculating and uploading your result, please wait......</p>'))

# Calculating the score based on the user's performance in the test
upload_dict['score'] = score(accuracy_dict)
# Converting accuracy and question-answer data into JSON format for uploading
accuracy_df = pd.DataFrame([accuracy_dict])
upload_dict['accuracy_json'] = accuracy_df.to_json()
qas_df = pd.DataFrame(qas_dict)
upload_dict['qas_json'] = qas_df.to_json()
event_info_df = pd.DataFrame(event_info_dict)
upload_dict['event_info_json'] = event_info_df.to_json()

# Attempting to upload the test data to the specified Google Form
try:
    upload_status = send_to_google_form(upload_dict, form_url)
# Handling exceptions and retrying upload if necessary
except Exception:
    clear_output(wait=False)
    display(HTML('<p style="text-align: center; font-size: 22px">Sorry, an error occurred. Trying to upload '
                 'again......</p>'))
    try:
        upload_status = send_to_google_form(upload_dict, form_url)
    # If the upload fails again, prompt the user for manual action
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
        # Raising an exception to indicate upload failure
        raise (Exception("Upload Error"))

# If the upload is successful, display a confirmation message
display(HTML('<p style="text-align: center; font-size: 22px">Upload successful!</p>'))
time.sleep(1)
display(HTML('<p style="text-align: center; font-size: 22px">Ranking you with other people......</p>'))

# Final steps after attempting to upload the test results

# Fetching the existing scores from the Google Sheet to calculate the user's rank
ranking_df = pd.read_excel(sheet_url, usecols='B, F')
# Calculating ranks based on scores
rankings = ranking_df['score'].rank(method='min', ascending=False)
# Finding the user's rank
ranking = rankings[ranking_df['score'] == upload_dict['score']].iloc[0]
# Total number of entries for context
total_entries = len(ranking_df)
# The highest score for comparison
max_value = ranking_df['score'].max()

# Displaying the final message with the user's score, rank, and encouragement to try again for a better score
time.sleep(2)
clear_output(wait=False)
display(HTML(f"<h1 align='center'>Well done, {upload_dict['id']}!</h1>"))
display(HTML(f"<p style='text-align: center; font-size: 18px'>Your score in this test is {upload_dict['score']}.<br>"
             f"You are ranked {ranking:.0f} out of {total_entries} testees.<br>Currently the highest score is {max_value}.<br>"
             f"Feel free to try the test again for a better result!</p>"))
