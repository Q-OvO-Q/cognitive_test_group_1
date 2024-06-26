# Spatial Reasoning Test

This folder contains code developed to run spatial test written by Group 1 as part of the BIOS0030 course.

It will test your spatial imagination skills and upload your result to an online spreadsheet for data analysis and comparison.

## Contents
- [Test Instruction](#test-instruction)
- [Usage](#usage)
- [Update Log](#update-log)
  
## Test Instruction

* This test last approximately 3 to 5 minutes, with variations on individuals.
* Your anonymous ID, group number, sex and age information is gathered only for teaching and training purpose. More information please see the "Data Consent" session in the test. 
* The difficulty of questions is evenly distributted, and every question values the same.
* There are eight questions in total.
* Each question is composed of one 3D visualisation of cubes of different colours, and four pictures of 2D projections.
* Your task is to observe and identify one of the four 2D projections that CANNOT be obtained by rotating the 3D cubes.
* There is no time limit on observation, so please do not rush to the next question.

## Usage

Access this test through mybinder:

https://mybinder.org/v2/gh/Q-OvO-Q/cognitive_test_group_1/HEAD

Click the link, then enter the Spatial_Test folder, finally open spatial_ready_to_go_V2.ipynb.

## Update Log

### v1.0

#### Initial Release Features
- The first stable release of the project, featuring basic functionality.
- User-friendly interface for efficient navigation and operation.

#### Known Issues
- Users have to scroll down to see the whole question.
- Poor code readability.

### v2.0

#### Major Enhancements

##### Improved User Interaction and Validation
- Anonymized ID Collection: Introduced validation for the anonymized ID input to ensure it follows the specified format (4 alphabetic characters).

##### User Interface and Experience
- Clearer Test Instructions: Revised the test instructions to provide clearer guidelines on how to do the test. 
- Better display of questions: using pictures instead of drawing the cubes so that all the options can be seen in one screen.
- Hidden code chunks: put the functions and codes into separate files to run the test without showing participants the code chunks. 

##### Data Handling and Upload
- Enhanced Data Structure: Used JSON format for saving and uploading the data instead of dataframes.

#### Minor Updates
- Added a brief introduction at the very begining of the test.
- Used button for the confirmation of data consent instead of typing.
- Included more comments and docstrings for improved code readability.
