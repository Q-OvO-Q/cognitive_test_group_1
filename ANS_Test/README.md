
# Approximate Number Sense (ANS) test

This folder contains code developed to run the ANS test written by Group 1 as part of the BIOS0030 course.

The Approximate Number Sense (ANS) test tests the users ability to distinguish which side of an image has a higher number of dots.

## Contents
- [Test Instruction](#test-instruction)
- [ANS_test Directory Contents](#ANS_test-Directory-Contents)
- [Usage](#usage)
- [Update Log](#update-log)

## ANS_test Directory Contents
- images used in the test
- ans_test_code.ipynb version 2.0
- run_ans.ipynb version 2.0
  
## Test Instruction

* A series of images with dots will be displayed (followed by an empty image if you need more time to answer).
* You must decide which side has more dots (left or right) within 3 seconds.
* To submit your answer use the left and right keys ON THE KEYBOARD (not the mouse).
* FROM THE MOMENT THE IMAGE APPEARS ON THE SCREEN you may enter your answer.
* Good luck!
  
## Usage

Download ANS_Test folder and open run_ans.ipynb to start the test.

This test is not compatible with mybinder.

## Update Log

### v1.0

#### Initial Release Features
- The first stable release of the project, featuring basic functionality.
- User-friendly interface for efficient navigation and operation.

#### Known Issues
- Unclear instructions.
- Poor code readability.

### v2.0

#### Major Enhancements

##### Improved User Interaction
- Anonymized ID Collection: Introduced validation for the anonymized ID input to ensure it follows the specified format (4 alphabetic characters).

##### User Interface and Experience
- Clearer Test Instructions: Revised the test instructions to provide clearer guidelines on how to submit answers and how long the participant has for each question.
- Improved Feedback: Allows users to see their score on completion of the test.
- Progress Tracking: Allows users to see their progress though the test.
- Hidden code: The code is hidden from the user while taking the test.

#### Minor Updates
- Minor text and display adjustments.
- Optimized code for performance improvements.
- Included more comments and docstrings for improved code readability.
