# Memory Test

This folder contains code developed to run the Memory Test written by Group 1 as part of the BIOS0030 course.

It will test your memory skills and upload your result to an online spreadsheet for data analysis and comparison.

## Contents
- [Test Instruction](#test-instruction)
- [Usage](#usage)
- [Update Log](#update-log)

## Test Instructions 

* This test last approximately 3 to 5 minutes, with variations on individuals.
* Your anonymous ID, group number, sex and age information is gathered only for teaching and training purpose. More information please see the "Data Consent" session in the test.
* The difficulty of questions is evenly distributted, and every question values the same.
* There are thirty questions in total.
* Each question is based on the colour or position of a shape in a grid that was displayed.
* Your task is to memorize the grid and answer questions regarding its contents 
* There is no time limit on observation, so please do not rush to the next question.

## Usage

Access this test through mybinder:

https://mybinder.org/v2/gh/Q-OvO-Q/cognitive_test_group_1/HEAD

Click the link, then enter the Memory_Test folder, finally open MemoryTest.ipynb. 

Run the code. After the second to last code cell runs, a panel of answers will show up. Click on any button until it goes away. Then run the last cell containing the function memory_test(). This will start the final memory test. 

## Update Log

### v1.0

#### Initial Release Features
- The first stable release of the project, featuring basic functionality.
- User-friendly interface for efficient navigation and operation.

#### Known Issues
- Poor code readability.
- Issues exporting to the spreadsheet. 

### v2.0

#### Major Enhancements 

##### Improved User Interaction 
- Anonymized ID Collection: Introduced validation for the anonymized ID input to ensure it follows the specified format (4 alphabetic characters).
- Made Images and Text bigger so that it was more easily viewed on a screen.

##### Enhanced Test Functionality 
- Recorded the accuracy for each question. Recorded the time taken by the user to answer a question after each grid was displayed instead of the whole test which more accurately measures the time taken for each question.

##### User Interface and Experience 
- Labelled the grid with the names of the shapes to make it friendly for non-native english speakers.
- Reported to the user whether they correctly or incorrectly answered a question after each question. 

##### Enhanced Data Structure 
- Introduced a more comprehensive data structure for storing test questions, answers, correctness, and time taken.
