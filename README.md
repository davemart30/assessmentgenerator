# assessmentgenerator
Generates random assignments and answers for a range of students. Some questions are static and others random.  Various combinations of variables are used to create what should be a unique assignment for each student.

## assessmentgeneratorv2.py
 - generates a folder called output
 - reads student names and numbers from studinfo.csv
 - creates a html page using the students details and random questions
 - includes a unique examid that represents the questions asked and makes an index file of this information

I then use a batch file I found to make a html file that lists all of the assignment files.  Then use an old internet explorer trick to print all files to the printer for manual handout.

**See the Issues section of this github to see what needs doing.**

## answergenerator.py
 - generates a unique answersheet for each student based on answers
 - should integrate into assessmentgeneratorv2.py so both questions and answers generatred at once
 - will be able to remove examID field, file and prefixes
 

## Documents
- **Model Answers** ready for answergenerator
  - Model Answers Task 1.xlsx
  - Model Answers Task 2.xlsx
  - Task 3 (version 2).xlsb.xlsx
  
**SSUD71-308 Assignment Review for 183**.docx
 - Shows questions and layout of original printed assignment

##Setup and running
Download and extract files to working folder
create an directory called _output_ and move css file into it
Use cmd to run command line
Change directy to working folder
type _assessmentgeneratorv2.py_
Check the output folder
