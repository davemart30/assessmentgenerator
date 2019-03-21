import secrets
import random 
import csv
import datetime
from ql import setupLists
import ql


#set defaults
assignID = ""
q1list=[]
q2list=[]
s2alist=[]
s2blist=[]
s2clist=[]
q4alist=[]
q4blist=[]
q5list=[]
q6list=[]
q7list=[]
q8list=[]
q9list=[]

studentID = ""




def RandomList(items): 
    #if type(items) != 'list':
    #     return
    #print (items)
    global assignID
    llength = len(items)
    randomitem = random.randint(0,llength-1)
    newItem = items[randomitem]
    items.pop(randomitem)
    assignID = newItem[0:2] + assignID
    newItem = newItem[3:]
    return newItem




def main():
    global q1list
    global q2list
    global s2alist
    global s2blist
    global s2clist
    global q4alist
    global q4blist
    global q5list
    global q6list
    global q7list
    global q8list
    global q9list
    global assignID
    #setup list
    print("starting creation...")
    setupLists()
    print ("created")
    #import studentinfo
    
    with open('studinfo.csv') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        studentIDs = []
        studentNames = []
        for row in readCSV:
            studentIDs.append(row[0])
            studentNames.append(row[2]+" "+row[1])

    print ("number of students completed = " + str(len(studentIDs)))
    #Open IDIndexfile
    indexFile = open("output/AssignmentIDIndex.csv","w")
    indexWriter = csv.writer(indexFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    nameIndex=0
    for currentStudent in studentIDs:
        assignID=""
        #Open file and create 1st section
        file = open("output/" + currentStudent + "_" + studentNames[nameIndex] + "_AssignmentQuestions191.html","w", encoding="utf-8")
        nameIndex += 1
        file.write("<!DOCTYPE html><html><head><style>body {font-family: 'Arial', Arial}table.boq {border-collapse: collapse;border: solid 3px black; }table.boq td {border:solid 1px black}</style></head><body><div id='header' style='border-style: solid; border-width: 2px'><header><h1 style='margin-left: 5px'>SSUD71-308-191:</h1><h1 style='margin-left: 5px'>Project Contract Administration</h1><h2 style='margin-left: 5px'>Assignment Part B</h2><h3 style='margin-left: 5px'>Student:   "+currentStudent +" ("+studentNames[studentIDs.index(currentStudent)] +")</h3> "+"<div id='examid' style='color:gray'></div></header></div><div id='instructions' style='border-style: solid; border-width: 1px'><h3 style='margin-left: 5px'>DUE DATE: 4pm Wednesday 20/03/2019</h3><h3 style='margin-left: 5px'>Submission Requirements</h3><ol type='a'><p style='margin-left: 5px'><li>Assignment  submissions must be uploaded via iLearn - <strong>no</strong> hard copy is required</li><li><strong>UPLOAD</strong> as a 'Word' document (.doc format) and in PDF (.pdf format) via the 'Assessment' tab in iLearn;</li><li>It is the student&#39;s responsibility to submit each part of the assignment as detailed above - no exceptions will be made, other than in strict accordance with university policy</ol><p style='color: red; margin-left: 5px'><strong>Late submissions will be penalized by 10% for every day that the submission is late.</strong></p><h3 style='margin-left: 5px'>Scope</h3><p style='margin-left: 5px'>Respond to all nine tasks</p><h3 style='margin-left: 5px'>Value</h3><p style='margin-left: 5px'>Part A: 10% of the assignment.</p><p style='margin-left: 5px'><strong>Part B: 90% of the assignment total.</strong></p><h3 style='margin-left: 5px'>Approach</h3><ul style='margin-left: 5px'><li>Take time to read all parts of this assignment document thoroughly before you start and carefully to ensure you <strong>understand the requirements of each task fully.</strong></li><li>You are encouraged to refer to external sources, however your responses must represent <strong>your interpretation</strong> and be written <strong>in your own words.</strong></li><li>Respond to each task strictly in accordance with the task requirements and keep your responses precise.</li><li>Quote <strong><em>all</em> contract references</strong> wherever directly relevant to any part of the task.</li><li>Provide full APA Standard in-text citations and reference list for Tasks 8 and 9 only (<strong>not required</strong> for other tasks).</li></ul><br><h3 style='margin-left: 5px'>Assessment</h3><p style='margin-left: 5px'>Grading will be in accordance with the Assessment Rubric in iLearn. Review the rubric carefully to understand the way in which the assignment will be assessed.</p><p style='margin-left: 5px; color:red'><em><strong>(Note that comprehensive responses to each task are required for full marks).</strong></em></p></div><p align='center' style='color:red'><strong>Your responses to all tasks are to be based on the lump sum building contract described in the assignment &quot;Scenario&quot;.</strong></p><hr><!--SCENARIO PART A--><h2>Scenario - Part A</h2><p>Assume that you are employed by a builder as his Contract Administrator for a commercial building project. You have just been given a copy of the executed lump sum contract for construction of the project.</p><p>The contract is comprised of the following component documents:</p><ol><li>Formal instrument</li><li>AS4000-1997 - General conditions of contract</li><li>AS4000-1997 - Annexure Part A</li><li>AS4000-1997 - Annexure Part B</li><li>Scope of works</li><li>Tender program</li><li>Bill of quantities</li><li>Technical specifications</li><li>Tender drawings</li></ol><p style='margin-left: 5px; color:red'><em><strong>Instructions: </strong>Respond to <strong>Tasks 1 and 2</strong> based on Scenario - Part A above.</em></p><hr><!--QUESTION 1--><h3 style='color:red'>Task 1 (11.25 marks)</h3><div id='q1'><p>Three component documents have been selected from the nine listed above:</p><div id='q1list'>")
        

        #Add 3 x q1 elements
        qlist=ql.q1list
        
        file.write("<ol><li>" + RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li></ol></div><p>By reviewing and analysing &#39;real&#39; examples of these three documents <strong>describe in your own words the:</strong></p><ol type='a'><li>appearance of the document;</li><li>contents of the document;</li><li>purpose for which the document was created; and</li><li>role that the document plays in administering the Contract.</li></ol><p>You will need to use your initiative to find suitable example documents. Specify the source of each of the example documents reviewed.</p><p><em>(200-250 words in total for each of the three documents)</em></p><hr></div><!--QUESTION 2--><h3 style='color:red'>Task 2 (6.25 marks)</h3><div id='q2'><p>From the nine documents listed in Scenario-Part A, nominate one that is certain to contain:</p><div id='q2list'>")

        #Add q2 elements
        qlist = ql.q2list
        file.write("<ol><li>" + RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li><li>"+ RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li></ol></div><p> Explain briefly why you selected the document in each case.</p><p><em><strong>Note: </strong>List clause references for any item that is found in AS4000-1997.</em></p><hr></div><!-- SCENARIO PART 2--><!--SCENARIO Part B--><h2>Scenario - Part B</h2><h3 style='margin-left: 5px'>ADDITIONAL DOCUMENTS</h3><p>Two of the nine component documents listed in Scenario-Part A are have been issued seperately:</p><div id='s2a'>")

        #Add Scenario part 2 elements. Record them so that appendix can be added at the end.
        s2aItem = RandomList(ql.s2alist)
        s2bItem = RandomList(ql.s2blist)
        s2cItem = RandomList(ql.s2clist)
        file.write("<ul><li>" + s2aItem + "</li><li>" + s2bItem + "</li></ul></div><div id='s2c'><p><strong>ADDITIONAL DETAILS</strong></p><ol type='A'>" + s2cItem + "</li></ol></div>")

        #Add task 3 elements and question 4
        file.write("<p style='margin-left: 5px; color:red'><em><strong>Instructions: </strong>Respond to <strong>Tasks 3 to 6</strong> based on:</p><ul><li style='color:red'>Scenario Part A, Scenario Part B and</li><li style='color:red'>the additional details above</em></li></ul><hr><br /><br /><h3 style='color:red'>Task 3 (12.5 marks)</h3><div id='q3'><ol type='a'><li>By what date should the Principal have given the Contractor possession of site?</li><li>How many days late was the date of practical completion?</li><li>How much is the contract sum?</li><li>How long did the Principal have to rectify inadequate Contractor &#39;s possession of the site?</li><li>How long is the defects liability period?</li><li>What is the value of the security that should have been provided by the Contractor soon after the start of the project?</li><li>In what form should the Contractor have provided security at the start of the project?</li><li>Who is responsible for nominating the arbitrator to resolve the ongoing dispute?</li><li>The units of measure used in the bill of quantities are in the legal units of what jurisdiction?</li><li>At practical completion only 85% of the materials referenced in Item 20 d) of Annexure Part A were consumed; 15% still remains on site as surplus. The Principal wishes to leave this material on site. Who is responsible for protection of the surplus material?</li></ol><p style='margin-left: 5px'><em><strong>Note:</strong> Explain your logic, show any workings, and list all relevant references from AS4000-1997.</em></p></div> \
        <hr><!-- TASK 4--><div id='q4'><h3 style='color:red'>Task 4 (11.25 marks)</h3><div id='q4a'><ol><li>" + RandomList(ql.q4alist) + "</li><li>What is the total amount of security  the Principal is entitled to be holding now (one week after practical completion was achieved). Explain your logic.</li><li>To update the Bill of Quantities to include the amount of work measured as &#39;actually&#39; completed by the Contractor, the quantities for the B/Q items listed must be adjusted to those shown below:</li></ol>" + RandomList(ql.q4blist) + " <p style='margin-left: 5px'>What amount should be added to or deducted from the contract sum as a result of the adjustments made for the work  &#39;actually&#39; completed?<br><p><em><strong>Note:</strong> List all relevant references</strong> from AS4000-1997 <strong>and</strong> show your workings for items 2 and 4.</em></p><hr>")

        
        #Task 5
        file.write("<h3 style='color:red'>Task 5 (10 marks)</h3><div id='task5'><p>Calculate the adjustment required to the contract sum if:</p><div id='q5'>" + RandomList(ql.q5list) + "</div><p><em><strong>Note:</strong> Show your workings <strong>and</strong> any relevant references from AS4000-1997</em></p></div><hr>")

        #Task 6
        file.write("<!-- TASK 6--><div id='task6'><h3 style='color:red'>Task 6 (6.25 marks)</h3><p>Make the following assumptions in relation to the assignment scenario:</p><div id='q6'>" + RandomList(ql.q6list) + "</div></div><hr>")

        #Task 7
        file.write ("<h3 style='color:red'>Task 7 (7.5 marks)</h3><div id='task7'><p>Specify where in AS4000-1997 the following can be found:</p><div id='q7'><ol type='a'><li>" + RandomList(ql.q7list) + "</li><li>" + RandomList(ql.q7list) + "</li><li>" + RandomList(ql.q7list) + "</li><li>"+ RandomList(ql.q7list) + "</li><li>" + RandomList(ql.q7list) + "</li><li>"+ RandomList(ql.q7list) + "</li></ol></div><p><em><strong>Note: </strong>Nominate supporting contract references that confirm the validity of each of your responses.</em></div><hr>")
        
        
        #TASK 8
        file.write("<div id='task8'><h3 style='color:red'>Task 8 (10 marks)</h3><p><strong><em>In your own words</em></strong> describe the purpose of each of the following <strong>and</strong> their impacts on the parties to the Contract:</p><div id='q8'><ol type='a'><li>" + RandomList(ql.q8list) + "</li><li>" + RandomList(ql.q8list) + "</div><p><em><strong>Note:</strong> Use APA Style referencing (including In-text citations and Reference list).</em></p><p><em>(100-200 words for each item excluding referencing)</em></p></div><hr>")

        
        # TASK 9
        file.write("<h3 style='color:red'>Task 9 (15 marks)</h3><div id='q9'><p>This task requires <strong>in-depth</strong> research <strong>and</strong> analysis. Your response should draw from at least two recognised external sources (excluding Goldfayl).</p><p>Investigate " + RandomList(ql.q9list) + "</strong> and then describe <strong><em>in your own words:</em></strong></div><ol type='i'><li>what it means when used in AS4000-1997,</li><li>under what circumstances in AS4000-1997 is it applied,</strong> and<li>any differences in meaning and/or application when used in AS4000-1997 compared with the equivalent phrase(s) in AS2124-1992</li></ol><p><em><strong>Note: </strong>Use APA Style referencing (including In-text citations and Reference list).</em></p><p><em>(200-300 words excluding referencing)</em></p></div><hr>")

        file.write("<h2 style='color:red' align='center'>END OF ASSIGNMENT TASKS</h3><hr>")
        
        now = datetime.datetime.now()
        file.write("<p style='font-size: 9px'>Generated: " + now.strftime("%Y-%m-%d %H:%M"))         
        file.write("<p style='font-size: 9px; color:white'>ID: "+assignID)
        indexWriter.writerow([currentStudent,assignID])

        #close the file
        file.close()
        setupLists()
    indexFile.close()

main()