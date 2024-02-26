display(HTML("<h1 align='center'>Data Consent Information</h1>"))
display(HTML("""
<p style="text-align: center; font-size: 18px">
We wish to record your response data to an anonymised public data repository.<br>
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
test_instructions("blue", "test")
memory_test() 
