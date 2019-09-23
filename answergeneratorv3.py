import csv

#set defaults
assignID = ""
studentID = ""
currentStudent = ""
studentIDs = []
studentNames = []

def importStudentIDs():
    print("Statring StudentID and name import.....")
    with open('studinfo.csv') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')

        for row in readCSV:
            studentIDs.append(row[0])
            studentNames.append(row[2]+" "+row[1])

#Open IDIndexfile
print('Starting answer sheet generator.......')
importStudentIDs()
print("Finished studentIDs and studentNames import.....")
print ('Student Name[1]: ' + studentNames[1])

with open("output/AssignmentIDIndex.csv") as indexFile:
    
    indexReader = csv.reader(indexFile,delimiter=',')
    for row in indexReader:
        currentStudent = row[0]
        currentExamID = row[1]
        print ('CurrentStudent from Assingment index: ' + currentStudent)
        print ('CurrentExamID: '+ currentExamID)
        #Open file and create 1st section
        print ('Starting Answer Sheet Creation..............')
        file = open("output/ANSWERSHEET_" + currentStudent + "_Assignment193.html","w")
        file.write("<!DOCTYPE html><html><head><style type='text/css'>body {font-family: 'Arial', Arial;}</style></head><body>   <div id='header' style='border-style: solid; border-width: 2px'><header><h1 style='margin-left: 5px'>SSUD71-308-191: Project Contract Administration</h1><h2 style='margin-left: 5px'>ASSIGNMENT ANSWER SHEET - DO NOT DISTRIBUTE</h2><h3>Student: "+ studentNames[studentIDs.index(currentStudent)] + " (" + currentStudent +")</h3> "+"<div id='examid' style='color:gray'></div></header></div><br /><div id='instructions' style='border-style: solid; border-width: 1px'><h3 style='margin-left: 5px'>Due Dates GROUP 1</h3><p style='margin-left: 5px'><strong>Part 2:</strong> 19/06/18</p><p style='margin-left: 5px'><strong>Part 3:</strong> 10/07/18</p><br /><h3 style='margin-left: 5px'>Due Dates GROUP 2</h3><p style='margin-left: 5px'><strong>Part 2:</strong> 22/06/18</p><p style='margin-left: 5px'><strong>Part 3:</strong> 13/07/18</p><br /><h3 style='margin-left: 5px'>Lodgement:</h3><p style='margin-left: 5px'>Answers to Parts 2 &amp; Part 3 are both to be submitted:</p><ol type='a' ><li>as &#39;Word&#39; documents (.doc format) via the &#39;Assessment&#39; tab iLearn;</li><li>in hard copy to the Level 2 Assignment Drop Box in Building 3; and</li><li>with a cover sheet detailing your name and SID.</li></ol><p style='margin-left: 5px'>You must also:</p><ol><li>Save this page as a PDF, including your student number in the file name.</li><li>Change your internet browser tab or window back to iLearn</li><li>Use the Assignment Parts 2 &amp; 3 link to upload a copy of your PDF Assignment Questions without answers.<li>Keep a copy of these Assignment Questions on your computer.</li><li>Submit your answers, and a copy of the Assignment Questions as part of your submission by the due date.</li></ol><p style='margin-left: 5px'>It is the student&#39;s responsibility to submit each part of the assignment as detailed above - no exceptions will be made, other than in strict accordance with university policy. <p><p style='color: red; margin-left: 5px'><strong>Late submissions will be penalized by 10% for every day that the submission is late.</strong></p><h3 style='margin-left: 5px'>Scope</h3><p style='margin-left: 5px'>Respond to all nine tasks</p><br /> <h3 style='margin-left: 5px'>Value</h3><p style='margin-left: 5px'>Part 2: 15% of the subject total.</p><p style='margin-left: 5px'>Part 3: 75% of the subject total.</p><br /><h3 style='margin-left: 5px'>Approach</h3><p style='margin-left: 5px'>Follow the 5 point list of instructions above very carefully to your assignment for safe keeping. Report any problems immediately.</p><p style='margin-left: 5px'>Take time to read all parts of this assignment document thoroughly and carefully to ensure you <strong>understand the tasks fully.</strong></p><p style='margin-left: 5px'>You are encouraged to refer to other sources, however your responses must represent your interpretation and be written in your own words.</p><p style='margin-left: 5px'>Respond to each task strictly in accordance with the request and keep your responses precise.</p><p style='margin-left: 5px'>List <em>all</em> relevant contract references wherever applicable, and provide <em>full</em> APA Standard in-text citations and reference list.</p><p style='margin-left: 5px'><em>(Remember that precision in reading and interpretation is a cornerstone of contract administration).	</em></p><br /><h3 style='margin-left: 5px'>Assessment</h3><p style='margin-left: 5px'>Grading will be in accordance with the Assessment Rubric. </p><p style='margin-left: 5px; color:red'><em>(Comprehensive responses addressing each task are required to achieve full marks). </em></p></div><br /> <hr><h3>All parts of this assignment are based on one lump sum building contract as described in the Scenario.</h3><!--SCENARIO 1--><h2>Scenario (Part 1)</h2>  <p>You have been given a copy of the lump sum contract which is comprised of the following component documents:</p> <ol><li>Formal instrument</li><li>AS4000-1997 - General conditions of contract</li><li>AS4000-1997 - Annexure Part A</li><li>AS4000-1997 - Annexure Part B</li><li>Scope of Works</li><li>Tender Program</li><li>Bill of quantities</li><li>Technical specifications</li><li>Construction drawings</li></ol><!--QUESTION 1--><h3 style='color:red'>Task 1 (15 marks)</h3><div id='q1'><p>For each of the three component documents listed below, describe in your own words its:<ol type='a' style='margin-left: -20px'><li>appearance and contents, and </li><li>purpose and role.</li></ol><div id='q1list'>")
        
