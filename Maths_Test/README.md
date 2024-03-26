# Math Ability Test

This folder contains code developed to run math test written by Group 1 as part of the BIOS0030 course.

It will test your mathematical skills and upload your result to an online spreadsheet for data analysis and comparison.

## Contents
- [Test Instruction](#test-instruction)
- [Usage](#usage)
- [Update Log](#update-log)
  
## Test Instruction

* The test will last for 3 minutes with 1 minute for each section.
* The difficulty of questions will be different in each section, from easy to hard.
* You will need to perform a sequence of calculations and provide the answer.
* Each part of the calculation is only shown for a short period of time and then hidden.
* Perform calculations SEQUENTIALLY rather than following standard arithmetic precedence rules.
* There is no upper limit for the score. The more correct ones, the higher the score.
* DO NOT USE CALCULATORS FOR HELP.

## Usage

Access this test through mybinder:

https://mybinder.org/v2/gh/Q-OvO-Q/cognitive_test_group_1/Maths_Test

## Update Log

### v2.0

#### Major Enhancements

##### Improved User Interaction and Validation
- Anonymized ID Collection: Introduced validation for the anonymized ID input to ensure it follows the specified format (4 alphabetic characters).
- Dynamic Age Verification: Added a check to ensure the age input is a valid number within a reasonable range (0-120 years).

##### Enhanced Test Functionality
- Randomized Question Generation: Enhanced the question generation mechanism to avoid repeating the same question within a test session.
- Improved Answer Verification: Streamlined the process for verifying answers, including time tracking for each question.

##### User Interface and Experience
- Clearer Test Instructions: Revised the test instructions to provide clearer guidelines on how calculations should be performed.
- Feedback Mechanism: Simplified the feedback collection process by directly mapping user feedback to the upload dictionary.

##### Data Handling and Upload
- Enhanced Data Structure: Introduced a more comprehensive data structure for storing test questions, answers, correctness, and time taken.
- Improved Upload Mechanism: Streamlined the data upload process to handle errors more gracefully.

##### System Operations and Efficiency
- Module Management: Added functionality to dynamically reload the `functions` module.
- Event Logging: Introduced detailed event logging, capturing user interactions and system events throughout the test.

#### Minor Updates
- Updated external links for data upload.
- Minor text and display adjustments.
- Optimized code for performance improvements.
- Included more comments and docstrings for improved code readability.

#### Bug Fixes
- Addressed issues related to user inputs and data formatting.

### v1.0

#### Initial Release Features
- The first stable release of the project, featuring basic functionality.
- User-friendly interface for efficient navigation and operation.

#### Known Issues
- Display issues when the question parts repeat.
- Poor code readability.
