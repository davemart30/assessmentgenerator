import secrets
import random 
import csv
import datetime

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


def setupLists():
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
    q1list = [
        'H1.Formal instrument',
        '1Z.AS4000-1997 - General conditions of contract',
        '43.AS4000-1997 - Annexure Part A',
        'B4.AS4000-1997 - Annexure Part B',
        '15.Scope of Works',
        '6P.Program',
        'KL.Bill of quantities',
        'WK.Technical specifications',
        'G2.Construction drawings'
    ]

    q2list = [
        '27.the parties to the Contract',
        '8G.dimensions for the Works',
        '3R.the type and amount of security to be provided by the Contractor',
        'R4.the contract sum',
        'DD.the person nominated to act on behalf of the Principal',
        'QU.the scope of the Works',
        'HT.the conditions upon which the Contractor is to be given possession of site',
        'T8.details of the Contractor&#39;s obligation to notify of a delay', 
        '2Z.specific details of the materials to be used in the Works',
        '9H.the requirement for evidence of insurances',
        'BA.clauses that have been deleted from the General Conditions in AS4000',
        'AB.which party is required to insure against liability for death or injury to persons employed by the Contractor',
        'ZZ.which party is required to effect the public liability for the project',
        'U7.the sequence in which the Superintendent expects the Contractor to undertake the Works',
        'Q9.the agreed duration of the contract',
        '2G.a technical description of WUC',
        'HH.the geometric details of the Works',
        'IQ.the amounts of any provisional sums',
        '87.the extent to which the Contractor is responsible for provision of site amenities for the Superintendent',
        '29.how much information about the project that the Contractor can include in it&#39;s industry magazine advertising'
    ]

    s2alist = [
        '3G.Annexure Part A and B (Version 1)',
        '32.Annexure Part A and B (Version 2)'
    ]
    s2blist = [
        'PI.Bill of Quantities (Version A)',
        'IT.Bill of Quantities (Version B)'
    ]

    s2clist = [
        #1
        '51.<li>Date of acceptance of tender: 29/09/2017.</li><li>The Contractor&#39;s overheads and profit percentage has been agreed: 13%. \
        </li><li>The Contractor did not reach practical completion until one week ago: 28/09/2018. \
        </li><li>The Superintendent has certified that WUC is complete and that the parties have agreed the actual quantity of work actually carried out for under every item listed in the Bill of Quantities. \
        </li><li>Two months ago the Contractor issued a notice of dispute to the Principal. Despite three conferences between the parties during the first three weeks, the dispute has still not been resolved. (Until last week, the Principal insisted that the dispute would be resolved by negotiation beween the parties before the date of practical completion). The Contractor has taken no further action.',
        #2
        '8U.<li>Date of acceptance of tender: 09/10/2017.</li><li>The Contractor&#39;s overheads and profit percentage has been agreed: 13%. \
        </li><li>The Contractor did not reach practical completion until one week ago: 28/09/2018. \
        </li><li>The Superintendent has certified that WUC is complete and that the parties have agreed the quantity of work actually carried out for every item in the Bill of Quantities.  \
        </li><li>Two months ago the Contractor issued a notice of dispute to the Principal. Despite three conferences between the parties during the first three weeks, the dispute has still not been resolved. (Until last week, the Principal insisted that the dispute would be resolved before practical completion by negotiation between the parties). The Contractor has taken no further action.',
        #3
        'SQ.<li>Date of acceptance of tender: 29/09/2017.</li><li>The Contractor&#39;s overheads and profit percentage has been agreed: 15%. \
        </li><li>The Contractor did not reach practical completion until one week ago: 28/09/2018. \
        </li><li>The Superintendent has certified that WUC is complete and that the parties have agreed the quantity of work actually carried out for every item in the Bill of Quantities.  \
        </li><li>Two months ago the Contractor issued a notice of dispute to the Principal. Despite three conferences between the parties during the first three weeks, the dispute has still not been resolved. (Until last week, the Principal insisted that the dispute would be resolved before practical completion by negotiation between the parties). The Contractor has taken no further action.',
        #4
        '4M.<li>Date of acceptance of tender: 09/10/2017.</li><li>The Contractor&#39;s overheads and profit percentage has been agreed: 15%. \
        </li><li>The Contractor did not reach practical completion until one week ago: 28/09/2018. \
        </li><li>The Superintendent has certified that WUC is complete and that the parties have agreed the quantity of work actually carried out for every item in the Bill of Quantities.  \
        </li><li>Two months ago the Contractor issued a notice of dispute to the Principal. Despite three conferences between the parties during the first three weeks, the dispute has still not been resolved. (Until last week, the Principal insisted that the dispute would be resolved before practical completion by negotiation between the parties). The Contractor has taken no further action.'
    ]

    q4alist = [
        '1Y.According to AS4000 what actions should the Contractor have taken within 6 weeks of the date of acceptance of the tender (ie. contract date)?',
        'YY.According to AS4000 what actions should the Principal have taken within 6 weeks of the date of acceptance of the tender (ie. contract date)?'
    ]

    q4blist = [
        #1
        'CC.<p style="text-indent: 70px">BQ07 = 5,156.0 sq m</p> \
        <p style="text-indent: 70px">BQ11 = 2,497.2 sq m</p> \
        <p style="text-indent: 70px">BQ12 = 0</p> \
        <p style="text-indent: 70px">BQ16 = 4,856.5 sq m</p> \
        <p style="text-indent: 70px">BQ20 = 12,096.4 sq m</p> \
        <p style="text-indent: 70px">BQ21 = 3,618.0 sq m</p>',
        #2
        '72.<p style="text-indent: 70px">BQ07 = 5,130.2.0 sq m</p> \
        <p style="text-indent: 70px">BQ11 = 2,484.7 sq m</p> \
        <p style="text-indent: 70px">BQ12 = 0</p> \
        <p style="text-indent: 70px">BQ16 = 4,682.7 sq m</p> \
        <p style="text-indent: 70px">BQ20 = 12,097.6 sq m</p> \
        <p style="text-indent: 70px">BQ21 = 3,599.9 sq m</p>',
        #3
        '37.<p style="text-indent: 70px">BQ07 = 5181.5 sq m</p> \
        <p style="text-indent: 70px">BQ11 = 2,509.6 sq m</p> \
        <p style="text-indent: 70px">BQ12 = 0</p> \
        <p style="text-indent: 70px">BQ16 = 4,885.6 sq m</p> \
        <p style="text-indent: 70px">BQ20 = 12,218.6 sq m</p> \
        <p style="text-indent: 70px">BQ21 = 3,635.9 sq m</p>',
    ]

    q5list = [
        #1
        'G2.<ol type="i" style="margin-left: 70px"> \
            <li>the Contractor receives an invoice to the value of $94,501.00 for carrying out all the work associated with Bill of Quantities Item B/Q29. </li> \
            <li>all the work associated with Item B/Q12 of the Bill of Quantities is <strong><em>deleted</em></strong> from the Contract.</li> \
            <li>the <em><strong>total cost</strong></em> of the work carried out directly by the Contractor to complete all the work associated with Bill of Quantities Item B/Q28 was $99,210.00</li> \
             <li>the <em><strong>Contractor&#39;s costs</strong></em> to carry out part of the work associated with Bill of Quantities Item B/Q30 using his direct resources totalled $361,450.00 and he received an invoice from a subcontractor to complete the balance of the work for $531,000.00</li> \
        </ol>',
        #2
        'M8.<ol type="i" style="margin-left: 70px"> \
            <li>the Contractor receives an invoice to the value of $94,510.00 for carrying out all the work associated with Bill of Quantities Item B/Q28. </li> \
            <li>all the work associated with Item B/Q21 of the Bill of Quantities is <strong><em>deleted</em></strong> from the Contract.</li> \
            <li>the <em><strong>total cost</strong></em> of the work carried out directly by the Contractor to complete all the work associated with Bill of Quantities Item B/Q29 was $99,120.00</li> \
            <li>the <em><strong>Contractor&#39;s costs of using his direct resources</strong></em> to carry out part of the work associated with Bill of Quantities Item B/Q30 is $361,450.00 and he receives and invoice for $531,000.00 from the subcontractor who completes the balance of the work.</li> \
        </ol>'
    ]

    q6list = [
        #1
        'OZ.<ul type="disc"><li>You are the Superintendent for the contract.</li> \
        <li>today&#39;s date is 17/01/2018.</li> \
        <li>a situation has arisen where, although you are not certain, you suspect that the quality of one face of a reinforced concrete footing may not meet the requirements of the specification. \
        </li>Unfortunately, the footing was backfilled before you had an opportunity to inspect the workmanship.</li></ol> \
        <p>Prepare a notice to the Contractor, directing it to open up the work for inspection. The notice should also inform the Contractor of the possible consequences of this direction, and of any defective work that may be revealed by the inspection.</p> ',
        #2
        'GR.<ul type="disc"><li>you are the Superintendent for the Contract.</li> \
            <li>today&#39;s date is 01/11/2017.</li> \
            <li>the Contractor is obliged to effect insurance of the Works.</li> \
            <li>the date for giving the Contractor possession of the site has passed.</li> \
            <li>whilst the Contractor asserts that the insurance has been effected, it has not provided any evidence of such insurance to the Principal.</li></ul> \
        <p>Prepare a notice to the Contractor, informing it of the contractual consequences of its failure to comply with the Contract.</p>',
        #3
        'EA.<ul type="disc"><li>you are the Superintendent for the Contract.</li> \
            <li>today&#39;s date is 27/12/2017.</li> \
            <li>heavy rain has caused the sides of a deep excavation which is part of WUC to become unstable.</li> \
            <li>a residential building on the adjacent lot is likely to be undermined and collapse within hours unless emergency shoring work is carried out urgently.</li> \
            <li>it is after midnight and the Contractor&#39s representative has not been contactable for hours since you arrived at the site late this afternoon.</li></ul> \
        <p>Prepare a notice to the Contractor, informing it that the Principal intends to take the urgent action necessary to prevent collapse of the neighbouring building and advising of the contractual consequences of the Contractor&#39;s failure to take action.</p>',
        #4
        'TT.<ul type="disc"><li>you are the Contractor&#39;s representative for the Contract</li> \
            <li>today&#39;s date is 27/12/2017.</li> \
            <li>the Principal has not made any payment of moneys due for more than two months.</li> \
            <li>two weeks ago, in accordance with Cl 39.8 you gave the Principal a notice to show cause within eight days of the notice.</li> \
            <li>the Principal has not replied.</li></ul> \
        <p>Prepare a notice to the Principal informing it that the Contractor is suspending the whole of WUC, and advising of the potential consequences of the Principal&#39;s failure to show cause.</p>'
    ]

    q7list = [
        '01.identities of the parties to the Contract',
        'PQ.details of substantial breaches by the parties',
        'UB.why, when and by whom a construction program is created',
        'M3.the identity of any subcontractor nominated by the Principal that must be used by the Contractor to carry out a specified part of the WUC',
        '6T.risks of loss or damage to WUC for which the Principal is liable',
        'RM.whether the bill of quantities forms part of the Contract',
        'SV.from whom the Contractor is required to take instructions/directions',
        '88.in what manner the Superintendent should act (i.e. Statement of moral requirements)',
        'N9.the primary obligations of the parties to the Contract',
        'A0.The maximum period after issue of the Superintendent&#39;s decision notice regarding a claim for delay damages by the Contractor within which a dissatisfied party must issue any notice of dispute',
        'EO.an explicit statement defining a substantial breach by the Principal that is caused by a failure of the Superintendent',
        'OC.whether the Superintendent has the authority to prevent the Contractor from removing it&#39;s own equipment from the site once it is no longer required',
        'ZX.who is responsible for the cost of rectifying damage classified under Cl 15.1 d)',
        '0E.the purpose for which the Principal is permitted to copy the documents in Cl 8.3 a)',
        'QP.how the work done to rectify damage caused by an excepted risk is valued',
        '40.the Contractor&#39;s obligation to avoid interference with the ability of pedestrians to move past the site',
        'SC.what measures the Contractor can take if the Superintendent does not respond as required under Cl 34.6 after receiving the Contractor&#39;s request for the Superintendent to issue of a certificate of practical completion'
    ]


    q8list = [
        'A1.Provisional sum',
        'PA.Order of precedence',
        'HY.Selected subcontractor',
        'CV.Show cause notice',
        'BD.Cross liability',
        'VO.Novation',
        'L7.Formal instrument of agreement',
        'VC.Annexure Part A Separable Portions',
        'AN.Security',
        'A7.Final certificate'
    ]

    q9list = [
        'VG.the term <strong>&quot;in escrow&quot; </strong>',
        'B1.the phrase <strong>&quot;reasonably and in good faith&quot; </strong>',
        'IJ.the term <strong>&quot;prescribed notice&quot; </strong>',
        '3D.the term <strong>&quot;contract sum&quot; </strong>'
    ]

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
    setupLists()
    #import studentinfo
    
    with open('studinfo.csv') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        studentIDs = []
        studentNames = []
        for row in readCSV:
            studentIDs.append(row[0])
            studentNames.append(row[2]+" "+row[1])
    
    #Open IDIndexfile
    indexFile = open("output/AssignmentIDIndex.csv","w")
    indexWriter = csv.writer(indexFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    nameIndex=0
    for currentStudent in studentIDs:
        assignID=""
        #Open file and create 1st section
        file = open("output/" + studentNames[nameIndex] + "_" + currentStudent + "_AssignmentQuestions191.html","w", encoding="utf-8")
        nameIndex += 1
        file.write("<!DOCTYPE html><html><head><link rel='stylesheet' type='text/css' href='AssignmentQuestions.css'></head><body><div id='header' style='border-style: solid; border-width: 2px'><header><h1 style='margin-left: 5px'>SSUD71-308-191:</h1><h1 style='margin-left: 5px'>Project Contract Administration</h1><h2 style='margin-left: 5px'>Assignment Part B</h2><h3 style='margin-left: 5px'>Student: "+studentNames[studentIDs.index(currentStudent)] + " ("+currentStudent +")</h3> "+"<div id='examid' style='color:gray'></div></header></div><div id='instructions' style='border-style: solid; border-width: 1px'><h3 style='margin-left: 5px'>DUE DATE: 4pm Wednesday 20/03/2019</h3><h3 style='margin-left: 5px'>Submission Requirements</h3><ol type='a'><p style='margin-left: 5px'><li>Assignment  submissions must be uploaded via iLearn - <strong>no</strong> hard copy is required</li><li><strong>UPLOAD</strong> as a 'Word' document (.doc format) and in PDF (.pdf format) via the 'Assessment' tab in iLearn;</li><li>It is the student&#39;s responsibility to submit each part of the assignment as detailed above - no exceptions will be made, other than in strict accordance with university policy</ol><p style='color: red; margin-left: 5px'><strong>Late submissions will be penalized by 10% for every day that the submission is late.</strong></p><h3 style='margin-left: 5px'>Scope</h3><p style='margin-left: 5px'>Respond to all nine tasks</p><h3 style='margin-left: 5px'>Value</h3><p style='margin-left: 5px'>Part A: 10% of the assignment.</p><p style='margin-left: 5px'><strong>Part B: 90% of the assignment total.</strong></p><h3 style='margin-left: 5px'>Approach</h3><ul style='margin-left: 5px'><li>Take time to read all parts of this assignment document thoroughly before you start and carefully to ensure you <strong>understand the requirements of each task fully.</strong></li><li>You are encouraged to refer to external sources, however your responses must represent <strong>your interpretation</strong> and be written <strong>in your own words.</strong></li><li>Respond to each task strictly in accordance with the task requirements and keep your responses precise.</li><li>Quote <strong><em>all</em> contract references</strong> wherever directly relevant to any part of the task.</li><li>Provide full APA Standard in-text citations and reference list for Tasks 8 and 9 only (<strong>not required</strong> for other tasks).</li></ul><br><h3 style='margin-left: 5px'>Assessment</h3><p style='margin-left: 5px'>Grading will be in accordance with the Assessment Rubric in iLearn. Review the rubric carefully to understand the way in which the assignment will be assessed.</p><p style='margin-left: 5px; color:red'><em><strong>(Note that comprehensive responses to each task are required for full marks).</strong></em></p></div><p align='center' style='color:red'><strong>Your responses to all tasks are to be based on the lump sum building contract described in the assignment &quot;Scenario&quot;.</strong></p><hr><!--SCENARIO PART A--><h2>Scenario - Part A</h2><p>Assume that you are employed by a builder as his Contract Administrator for a commercial building project. You have just been given a copy of the executed lump sum contract for construction of the project.</p><p>The contract is comprised of the following component documents:</p><ol><li>Formal instrument</li><li>AS4000-1997 - General conditions of contract</li><li>AS4000-1997 - Annexure Part A</li><li>AS4000-1997 - Annexure Part B</li><li>Scope of works</li><li>Tender program</li><li>Bill of quantities</li><li>Technical specifications</li><li>Tender drawings</li></ol><p style='margin-left: 5px; color:red'><em><strong>Instructions: </strong>Respond to <strong>Tasks 1 and 2</strong> based on Scenario - Part A above.</em></p><hr><!--QUESTION 1--><h3 style='color:red'>Task 1 (11.25 marks)</h3><div id='q1'><p>Three component documents have been selected from the nine listed above:</p><div id='q1list'>")
        
        #Add 3 x q1 elements
        qlist=q1list
        
        file.write("<ol><li>" + RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li></ol></div><p>By reviewing and analysing &#39;real&#39; examples of these three documents <strong>describe in your own words the:</strong></p><ol type='a'><li>appearance of the document;</li><li>contents of the document;</li><li>purpose for which the document was created; and</li><li>role that the document plays in administering the Contract.</li></ol><p>You will need to use your initiative to find suitable example documents. Specify the source of each of the example documents reviewed.</p><p><em>(200-250 words in total for each of the three documents)</em></p><hr></div><!--QUESTION 2--><h3 style='color:red'>Task 2 (6.25 marks)</h3><div id='q2'><p>From the nine documents listed in Scenario-Part A, nominate one that is certain to contain:</p><div id='q2list'>")

        #Add q2 elements
        qlist = q2list
        file.write("<ol><li>" + RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li><li>"+ RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li><li>" + RandomList(qlist) + "</li></ol></div><p> Explain briefly why you selected the document in each case.</p><p><em><strong>Note: </strong>List clause references for any item that is found in AS4000-1997.</em></p><hr></div><!-- SCENARIO PART 2--><!--SCENARIO Part B--><h2>Scenario - Part B</h2><h3 style='margin-left: 5px'>ADDITIONAL DOCUMENTS</h3><p>Two of the nine component documents listed in Scenario-Part A are have been issued seperately:</p><div id='s2a'>")

        #Add Scenario part 2 elements. Record them so that appendix can be added at the end.
        s2aItem = RandomList(s2alist)
        s2bItem = RandomList(s2blist)
        s2cItem = RandomList(s2clist)
        file.write("<ul><li>" + s2aItem + "</li><li>" + s2bItem + "</li></ul></div><div id='s2c'><p><strong>ADDITIONAL DETAILS</strong></p><ol type='A'>" + s2cItem + "</li></ol></div>")

        #Add task 3 elements and question 4
        file.write("<p style='margin-left: 5px; color:red'><em><strong>Instructions: </strong>Respond to <strong>Tasks 3 to 6</strong> based on:</p><ul><li style='color:red'>Scenario Part A, Scenario Part B and</li><li style='color:red'>the additional details above</em></li></ul><hr><br /><br /><h3 style='color:red'>Task 3 (12.5 marks)</h3><div id='q3'><ol type='a'><li>By what date should the Principal have given the Contractor possession of site?</li><li>How many days late was the date of practical completion?</li><li>How much is the contract sum?</li><li>How long did the Principal have to rectify inadequate Contractor &#39;s possession of the site?</li><li>How long is the defects liability period?</li><li>What is the value of the security that should have been provided by the Contractor soon after the start of the project?</li><li>In what form should the Contractor have provided security at the start of the project?</li><li>Who is responsible for nominating the arbitrator to resolve the ongoing dispute?</li><li>The units of measure used in the bill of quantities are in the legal units of what jurisdiction?</li><li>At practical completion only 85% of the materials referenced in Item 20 d) of Annexure Part A were consumed; 15% still remains on site as surplus. The Principal wishes to leave this material on site. Who is responsible for protection of the surplus material?</li></ol><p style='margin-left: 5px'><em><strong>Note:</strong> Explain your logic, show any workings, and list all relevant references from AS4000-1997.</em></p></div> \
        <hr><!-- TASK 4--><div id='q4'><h3 style='color:red'>Task 4 (11.25 marks)</h3><div id='q4a'><ol><li>" + RandomList(q4alist) + "</li><li>What is the total amount of security  the Principal is entitled to be holding now (one week after practical completion was achieved). Explain your logic.</li><li>To update the Bill of Quantities to include the amount of work measured as &#39;actually&#39; completed by the Contractor, the quantities for the B/Q items listed must be adjusted to those shown below:</li></ol>" + RandomList(q4blist) + " <p style='margin-left: 5px'>What amount should be added to or deducted from the contract sum as a result of the adjustments made for the work  &#39;actually&#39; completed?<br><p><em><strong>Note:</strong> List all relevant references</strong> from AS4000-1997 <strong>and</strong> show your workings for items 2 and 4.</em></p><hr>")

        
        #Task 5
        file.write("<h3 style='color:red'>Task 5 (10 marks)</h3><div id='task5'><p>Calculate the adjustment required to the contract sum if:</p><div id='q5'>" + RandomList(q5list) + "</div><p><em><strong>Note:</strong> Show your workings <strong>and</strong> any relevant references from AS4000-1997</em></p></div><hr>")

        #Task 6
        file.write("<!-- TASK 6--><div id='task6'><h3 style='color:red'>Task 6 (6.25 marks)</h3><p>Make the following assumptions in relation to the assignment scenario:</p><div id='q6'>" + RandomList(q6list) + "</div></div><hr>")

        #Task 7
        file.write ("<h3 style='color:red'>Task 7 (7.5 marks)</h3><div id='task7'><p>Specify where in AS4000-1997 the following can be found:</p><div id='q7'><ol type='a'><li>" + RandomList(q7list) + "</li><li>" + RandomList(q7list) + "</li><li>" + RandomList(q7list) + "</li><li>"+ RandomList(q7list) + "</li><li>" + RandomList(q7list) + "</li><li>"+ RandomList(q7list) + "</li></ol></div><p><em><strong>Note: </strong>Nominate supporting contract references that confirm the validity of each of your responses.</em></div><hr>")
        
        
        #TASK 8
        file.write("<div id='task8'><h3 style='color:red'>Task 8 (10 marks)</h3><p><strong><em>In your own words</em></strong> describe the purpose of each of the following <strong>and</strong> their impacts on the parties to the Contract:</p><div id='q8'><ol type='a'><li>" + RandomList(q8list) + "</li><li>" + RandomList(q8list) + "</div><p><em><strong>Note:</strong> Use APA Style referencing (including In-text citations and Reference list).</em></p><p><em>(100-200 words for each item excluding referencing)</em></p></div><hr>")

        
        # TASK 9
        file.write("<h3 style='color:red'>Task 9 (15 marks)</h3><div id='q9'><p>This task requires <strong>in-depth</strong> research <strong>and</strong> analysis. Your response should draw from at least two recognised external sources (excluding Goldfayl).</p><p>Investigate " + RandomList(q9list) + "</strong> and then describe <strong><em>in your own words:</em></strong></div><ol type='i'><li>what it means when used in AS4000-1997,</li><li>under what circumstances in AS4000-1997 is it applied,</strong> and<li>any differences in meaning and/or application when used in AS4000-1997 compared with the equivalent phrase(s) in AS2124-1992</li></ol><p><em><strong>Note: </strong>Use APA Style referencing (including In-text citations and Reference list).</em></p><p><em>(200-300 words excluding referencing)</em></p></div><hr>")

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