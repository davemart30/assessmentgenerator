import secrets
import random 
import csv

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
    q1list = ['H1.Formal instrument','1Z.AS4000-1997 - General conditions of contract','43.AS4000-1997 - Annexure Part A','B4.AS4000-1997 - Annexure Part B','15.Scope of Works','6P.Program' 'KL.Bill of quantities','WK.Technical specifications','G2.Construction drawings']

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
        'ZZ.which party is required to effect the public liability policy for the project',
        'U7.the sequence in which the Superintendent expects the Contractor to undertake the Works',
        'Q9.the agreed duration of the contract',
        '2G.the technical description of WUC',
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
        'PI.Bill of quantities (Version A)',
        'IT.Bill of quantities (Version B)'
    ]

    s2clist = [
        #1
        '51.<li>Date of acceptance of tender = 02/06/2017.</li><li>The Contractor&#39;s overheads and profit percentage was agreed: 13% \
        </li><li>The Contractor did not reach practical completion until one week ago: 01/06/2018 \
        </li><li>The Superintendent has certified a cumulative total amount of $560,000.00 to be added to the contract sum. \
        </li><li>Eight weeks ago the Contractor issued a notice of dispute but the dispute has not been resolved.',
        #2
        '8U.<li>Date of acceptance of tender = 12/06/2017.</li><li>The Contractor&#39;s overheads and profit percentage was agreed: 13% \
        </li><li>The Contractor did not reach practical completion until one week ago: 01/06/2018 \
        </li><li>The Superintendent has certified a cumulative total amount of $560,000.00 to be added to the contract sum. \
        </li><li>Eight weeks ago the Contractor issued a notice of dispute but the dispute has not been resolved.',
        #3
        'SQ.<li>Date of acceptance of tender = 02/06/2017.</li><li>The Contractor&#39;s overheads and profit percentage was agreed: 15% \
        </li><li>The Contractor did not reach practical completion until one week ago: 01/06/2018 \
        </li><li>The Superintendent has certified a cumulative total amount of $560,000.00 to be added to the contract sum. \
        </li><li>Eight weeks ago the Contractor issued a notice of dispute but the dispute has not been resolved.',
        #4
        '4M.<li>Date of acceptance of tender = 12/06/2017.</li><li>The Contractor&#39;s overheads and profit percentage was agreed: 15% \
        </li><li>The Contractor did not reach practical completion until one week ago: 01/06/2018 \
        </li><li>The Superintendent has certified a cumulative total amount of $560,000.00 to be added to the contract sum. \
        </li><li>Eight weeks ago the Contractor issued a notice of dispute but the dispute has not been resolved.'
    ]

    q4alist = [
        '1Y.According to AS4000 what actions should the Contractor have taken within 6 weeks of the contract date?',
        'YY.According to AS4000 what actions should the Principal have taken within 6 weeks of the contract date?'
    ]

    q4blist = [
        #1
        'CC.<p style="text-indent: 70px">BQ07 = 5156.0 sq m</p> \
        <p style="text-indent: 70px">BQ11 = 2,497.2 sq m</p> \
        <p style="text-indent: 70px">BQ12 = 0</p> \
        <p style="text-indent: 70px">BQ16 = 4,681.5 sq m</p> \
        <p style="text-indent: 70px">BQ20 = 12,096.4 sq m</p> \
        <p style="text-indent: 70px">BQ21 = 3,618.0 sq m</p>',
        #2
        '72.<p style="text-indent: 70px">BQ07 = 5130.2.0 sq m</p> \
        <p style="text-indent: 70px">BQ11 = 2484.7 sq m</p> \
        <p style="text-indent: 70px">BQ12 = 0</p> \
        <p style="text-indent: 70px">BQ16 = 4,682.7 sq m</p> \
        <p style="text-indent: 70px">BQ20 = 12,097.6 sq m</p> \
        <p style="text-indent: 70px">BQ21 = 3,599.9 sq m</p>',
        #3
        '37.<p style="text-indent: 70px">BQ07 = 5181.5 sq m</p> \
        <p style="text-indent: 70px">BQ11 = 2,509.6 sq m</p> \
        <p style="text-indent: 70px">BQ12 = 0</p> \
        <p style="text-indent: 70px">BQ16 = 4,729.5 sq m</p> \
        <p style="text-indent: 70px">BQ20 = 12,218.6 sq m</p> \
        <p style="text-indent: 70px">BQ21 = 3,635.9 sq m</p>',
    ]

    q5list = [
        #1
        'G2.<ol type="i" style="margin-left: 70px"> \
            <li>the amount invoiced by a subcontractor to the Contractor for work done under a provisional sum was as follows: \
            <p style="text-indent: 70px">Provisional Sum = $108,000.00</p> \
            <p style="text-indent: 70px">Subcontractor invoice =  $94,500.00</p></li> \
            <li>the artwork in Item B/Q 012 of the bill of quantities is <strong><em>deleted</em></strong> from the Contract</li> \
            <li>the <em><strong>total cost</strong></em> to the Contractor of work carried out by the Contractor in relation to a provisional sum was as follows:  \
            <p style="text-indent: 70px">Provisional Sum = $107,500.00</p> \
            <p style="text-indent: 70px">Contractors <strong><em>costs</em></strong> = $98,900.00</p></li> \
        </ol>',
        #2
        'M8.<ol type="i" style="margin-left: 70px"> \
            <li>the amount invoiced by a subcontractor to the Contractor for work done under a provisional sum was as follows: \
            <p style="text-indent: 70px">Provisional Sum = $108,000.00</p> \
            <p style="text-indent: 70px">Subcontractor invoice =  $94,500.00</p></li> \
            <li>the artwork in Item B/Q 012 of the bill of quantities is <strong><em>deleted</em></strong> from the Contract</li> \
            <li>the <em><strong>total cost</strong></em> to the Contractor of work carried out by the Contractor in relation to a provisional sum was as follows:  \
            <p style="text-indent: 70px">Provisional Sum = $105,700.00</p> \
            <p style="text-indent: 70px">Contractors <strong><em>costs</em></strong> = $98,900.00</p></li> \
        </ol>'
    ]

    q6list = [
        #1
        'OZ.<p>You are the Superintendent for the contract described in the assignment scenario and a situation has arisen where, although you are not certain, you suspect that the quality of one face of a reinforced concrete footing may not meet the requirements of the specification. Unfortunately, the footing was backfilled before you had an opportunity to inspect the workmanship.</p> \
        <p>Prepare a notice to the Contractor, directing it to open up the work for inspection. It should also inform the Contractor of the possible consequences of this direction, and of any defective work that may be revealed by the inspection.</p> ',
        #2
        'GR.<ul><li>you are the Superintendent for the Contract</li> \
            <li>the Contractor is obliged to effect insurance of the Works</li> \
            <li>the date for giving the Contractor possession of the site has passed</li> \
            <li>whilst the Contractor asserts that the insurance has been effected, it has not provided any evidence of such insurance to the Principal</li></ul> \
        <p>Prepare a notice to the Contractor, informing it of the contractual consequences of its failure to comply with the Contract.</p>',
        #3
        'EA.<ul><li>you are the Superintendent for the Contract</li> \
            <li>heavy rain caused the sides of a deep excavation which is part of WUC to become unstable </li> \
            <li>a residential building on the adjacent lot is likely to be undermined and collapse within hours unless emergency shoring work is carried out urgently </li> \
            <li>it is after midnight and the Contractor&#39s representative has not been contactable for the past 2 hours</li></ul> \
        <p>Prepare a notice to the Contractor, informing it that the Principal intends to take the urgent action necessary to prevent collapse of the neighbouring building and advising of the contractual consequences of the Contractor&#39;s failure to take action.</p>',
        #4
        'TT.<ul><li>you are the Superintendent for the Contract</li> \
            <li>you are the Contractor&#39;s representative for the Contract</li> \
            <li>the Principal has not made any payment of moneys due for more than two months</li> \
            <li>two weeks ago, in accordance with Cl 39.8 you gave the Principal a notice to show cause within eight days of the notice</li> \
            <li>the Principal has not replied</li></ul> \
        <p>Prepare a notice to the Principal informing it that the Contractor is suspending the whole of WUC, and advising of the potential consequences of the Principal&#39;s failure to show cause.</p>'
    ]

    q7list = [
        '01.identities of the parties to the Contract',
        'PQ.details of substantial breaches by the parties',
        'UB.how a construction program is instigated',
        'M3.identity of a nominated subcontractor',
        '6T.risks of loss or damage to WUC for which the Principal is liable',
        'RM.whether the bill of quantities forms part of the Contract',
        'SV.from whom the Contractor is required to take instructions/directions',
        '88.in what manner the Superintendent should act',
        'N9.the primary obligations of the parties to the Contract',
        'A0.the period after a party becomes aware of a claim in relation to a Superintendent&#39;s direction within which the party is required to issue a notice of dispute',
        'EO.an explicit statement defining a substantial breach by the Principal that is caused by a failure of the Superintendent',
        'OC.whether the Superintendent has the authority to prevent the Contractor from removing it&#39;s own equipment from the site once it is no longer required',
        'ZX.who is responsible for the cost of rectifying damage classified under Cl 15.1 d)',
        '0Ethe purpose for which the Principal is permitted to copy the documents in Cl 8.3 a)',
        'QP.how the work required to rectify damage caused by an excepted risk is valued',
        '40.the Contractor&#39;s obligation to avoid interference with the ability of pedestrians to move past the site',
        'SC.what measures the Contractor can take if the Superintendent does not respond as required under Cl 34.6 after receiving the Contractor&#39;s request for issue of a certificate of practical completion'
    ]


    q8list = [
        'A1.Provisional sum',
        'PA.Order of precedence',
        'HY.Selected subcontractor',
        'CV.Time bar',
        'BD.Cross liability',
        'VO.Novation',
        'L7.Formal instrument of agreement',
        'VC.Annexure Part A Separable Portions',
        'AN.Security',
        'A7.Final certificate'
    ]

    q9list = [
        'VG.in escrow',
        'B1.time bar',
        'IJ.Prescribed notice',
        '3D.Contract sum'
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
    indexFile = open("AssignmentID Index.csv","w")
    indexWriter = csv.writer(indexFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for currentStudent in studentIDs:
        assignID=""
        
        #Open file and create 1st section
        file = open(currentStudent + "_AssignmentQuestions191.html","w")
        file.write("<!DOCTYPE html><html><head><style type='text/css'>body {font-family: 'Arial', Arial;}</style></head><body>   <div id='header' style='border-style: solid; border-width: 2px'><header><h1 style='margin-left: 5px'>SSUD71-308-191: Project Contract Administration</h1><h2 style='margin-left: 5px'>Assignment Parts 2 &amp;3</h2><h3>Student: "+studentNames[studentIDs.index(currentStudent)] + " ("+currentStudent +")</h3> "+"<div id='examid' style='color:gray'></div></header></div><br /><div id='instructions' style='border-style: solid; border-width: 1px'><h3 style='margin-left: 5px'>Due Dates GROUP 1</h3><p style='margin-left: 5px'><strong>Part 2:</strong> 19/06/18</p><p style='margin-left: 5px'><strong>Part 3:</strong> 10/07/18</p><br /><h3 style='margin-left: 5px'>Due Dates GROUP 2</h3><p style='margin-left: 5px'><strong>Part 2:</strong> 22/06/18</p><p style='margin-left: 5px'><strong>Part 3:</strong> 13/07/18</p><br /><h3 style='margin-left: 5px'>Lodgement:</h3><p style='margin-left: 5px'>Answers to Parts 2 &amp; Part 3 are both to be submitted:</p><ol type='a' ><li>as &#39;Word&#39; documents (.doc format) via the &#39;Assessment&#39; tab iLearn;</li><li>in hard copy to the Level 2 Assignment Drop Box in Building 3; and</li><li>with a cover sheet detailing your name and SID.</li></ol><p style='margin-left: 5px'>You must also:</p><ol><li>Save this page as a PDF, including your student number in the file name.</li><li>Change your internet browser tab or window back to iLearn</li><li>Use the Assignment Parts 2 &amp; 3 link to upload a copy of your PDF Assignment Questions without answers.<li>Keep a copy of these Assignment Questions on your computer.</li><li>Submit your answers, and a copy of the Assignment Questions as part of your submission by the due date.</li></ol><p style='margin-left: 5px'>It is the student&#39;s responsibility to submit each part of the assignment as detailed above - no exceptions will be made, other than in strict accordance with university policy. <p><p style='color: red; margin-left: 5px'><strong>Late submissions will be penalized by 10% for every day that the submission is late.</strong></p><h3 style='margin-left: 5px'>Scope</h3><p style='margin-left: 5px'>Respond to all nine tasks</p><br /> <h3 style='margin-left: 5px'>Value</h3><p style='margin-left: 5px'>Part 2: 15% of the subject total.</p><p style='margin-left: 5px'>Part 3: 75% of the subject total.</p><br /><h3 style='margin-left: 5px'>Approach</h3><p style='margin-left: 5px'>Follow the 5 point list of instructions above very carefully to your assignment for safe keeping. Report any problems immediately.</p><p style='margin-left: 5px'>Take time to read all parts of this assignment document thoroughly and carefully to ensure you <strong>understand the tasks fully.</strong></p><p style='margin-left: 5px'>You are encouraged to refer to other sources, however your responses must represent your interpretation and be written in your own words.</p><p style='margin-left: 5px'>Respond to each task strictly in accordance with the request and keep your responses precise.</p><p style='margin-left: 5px'>List <em>all</em> relevant contract references wherever applicable, and provide <em>full</em> APA Standard in-text citations and reference list.</p><p style='margin-left: 5px'><em>(Remember that precision in reading and interpretation is a cornerstone of contract administration).	</em></p><br /><h3 style='margin-left: 5px'>Assessment</h3><p style='margin-left: 5px'>Grading will be in accordance with the Assessment Rubric. </p><p style='margin-left: 5px; color:red'><em>(Comprehensive responses addressing each task are required to achieve full marks). </em></p></div><br /> <hr><h3>All parts of this assignment are based on one lump sum building contract as described in the Scenario.</h3><!--SCENARIO 1--><h2>Scenario (Part 1)</h2>  <p>You have been given a copy of the lump sum contract which is comprised of the following component documents:</p> <ol><li>Formal instrument</li><li>AS4000-1997 - General conditions of contract</li><li>AS4000-1997 - Annexure Part A</li><li>AS4000-1997 - Annexure Part B</li><li>Scope of Works</li><li>Tender Program</li><li>Bill of quantities</li><li>Technical specifications</li><li>Construction drawings</li></ol><!--QUESTION 1--><h3 style='color:red'>Task 1 (15 marks)</h3><div id='q1'><p>For each of the three component documents listed below, describe in your own words its:<ol type='a' style='margin-left: -20px'><li>appearance and contents, and </li><li>purpose and role.</li></ol><div id='q1list'>")
        
        #Add 3 x q1 elements
        qlist=q1list
        
        file.write("<ol><li>" + RandomList(qlist) + "</li><br /><li>" + RandomList(qlist) + "</li><br /><li>" + RandomList(qlist) + "</li></ol></div><p><em><strong>Note:</strong> Include clause references from AS4000 where applicable.</em></p><p><em>(100-200 words for each item)</em></p>    <hr></div><!--QUESTION 2--><h3 style='color:red'>Task 2 (7.5 marks)</h3><div id='q2'><p>Nominate one component document from the list in Task 1 in which the information for the following <strong><em>will be included</em></strong>. Nominate one document only for each of the following - no further explanation is required.</p><div id='q2list'>")

        #Add q2 elements
        qlist = q2list
        file.write("<ol><li>" + RandomList(qlist) + "</li><br /><li>" + RandomList(qlist) + "</li><br /><li>"+ RandomList(qlist) + "</li><br /><li>" + RandomList(qlist) + "</li><br /><li>" + RandomList(qlist) + "</li></ol></div><p><em><strong>Note: </strong>List clause references for any item that will be found in AS4000-1997.</em></p><hr></div><!-- SCENARIO PART 2--><!--SCENARIO 1--><h2>Scenario (Part 2)</h2><p>Refer to the component documents at the end of the assignment from the contract:</p><div id='s2a'>")

        #Add Scenario part 2 elements. Record them so that appendix can be added at the end.
        s2aItem = RandomList(s2alist)
        s2bItem = RandomList(s2blist)
        s2cItem = RandomList(s2clist)
        file.write("<ul><li>" + s2aItem + "</li></ul></div><div id='s2b'><ul><li>" + s2bItem + "</li></ul></div><div id='s2c'><p><strong>ADDITIONAL DETAILS</strong></p><ol type='A'>" + s2cItem + "</li></ol></div>")

        #Add task 3 elements and question 4
        file.write("<br /><h3 style='color:red'>Task 3 (10 marks)</h3><div id='q3'><ol type='a'><li>By what date should the Principal given the Contractor possession of site?</li><li>How many days late was the date of practical completion?</li><li>How much is the contract sum?</li><li>How long does the Principal have to rectify inadequate Contractor &#39;s possession of the site?</li><li>How long is the defects liability period?</li><li>What is the value of the security that should have been provided by the Contractor initially?</li><li>In what form should the Contractor initially have provided security?</li><li>Who is responsible for nominating the arbitrator to resolve the ongoing dispute?</li><li>The units of measure used in the bill of quantities are in the legal units of what jurisdiction?</li><li>Who is responsible for protecting surplus &#39;Principal supplied&#39; materials that the Principal does not want returned to the supplier after the practical completion?</li></ol></div><hr><!-- TASK 4--><h3 style='color:red'>Task 4 (15 marks)</h3><div id='q4'><div id='q4a'><ol><li>" + RandomList(q4alist) + "</div<ol start='2'><li>What is the total amount of security that the Principal is entitled to be holding now (one week after practical completion was achieved). Explain your logic.</li><li>The Superintendent has certified that WUC is complete and the parties have agreed the actual quantities of work carried out under each B/Q Item. What amount should be added to or deducted from the contract sum if the final &#39;actual&#39; quantities are:</li></ol><div id='q4b'>" + RandomList(q4blist) + "</div><p><em><strong>Note:</strong> List all relevant references from AS4000-1997 and show your workings for 2 and 3.</em></p></div><hr>")

        #Add line breaks to format for printing
        file.write("<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />")
        
        #Task 5
        file.write("<h3 style='color:red'>Task 5 (10 marks)</h3><div id='task5'><p>Calculate the adjustment required to the contract sum if:</p><div id='q5'>" + RandomList(q5list) + "</div><p><em><strong>Note:</strong> Show your workings and relevant references from AS4000-1997</em></p></div><hr>")

        #Task 6
        file.write("<!-- TASK 6--><h3 style='color:red'>Task 6 (10 marks)</h3><div id='task6'><p>Make the following assumptions regarding the assignment scenario:</p><div id='q6'>" + RandomList(q6list) + "</div></div><hr>")

        #Task 7
        file.write ("<h3 style='color:red'>Task 7 (12.5 marks)</h3><div id='task7'><p>Specify where in AS4000-1997 the following can be found:</p><div id='q7'><ol type='a'><li>" + RandomList(q7list) + RandomList(q7list) + "</li><li>" + RandomList(q7list) + "</li><li>"+ RandomList(q7list) + "</li><li>" + RandomList(q7list) + "</li><li>"+ RandomList(q7list) + "</li><li>" + RandomList(q7list) + "</li></ol></div><hr>")
        
        # Add line breaks for printed format
        file.write("<br /><br /><br /><br /><br /><br /><br />")
        
        #TASK 8
        file.write("<h3 style='color:red'>Task 8 (10 marks)</h3><div id='task8'><p><strong><em>In your own words</em></strong> describe the purpose of each of the following:</p><div id='q8'><ol type='a'><li>" + RandomList(q8list) + "</li><li>" + RandomList(q8list) + "</div><p><em><strong>Note:</strong> Use APA Style referencing (including In-text citations and Reference list).</em></p><p><em>(100-200 words for each item)</em></p></div><hr>")

        
        # TASK 9
        file.write("<h3 style='color:red'>Task 9 (10 marks)</h3><div id='q9'><p>Investigate the term <strong>" + RandomList(q9list) + "</strong> and then describe <strong><em>in your own words:</em></strong></div><ol type='i'><li>what it means <strong>in the context of AS4000-1997,</strong></li><li>how and/or when it is used <strong>in administering AS4000-1997,</strong> and<li>differences between its application in AS4000-1997 and in AS2124-1992.</li><p><em><strong>Note: </strong>Use APA Style referencing (including In-text citations and Reference list).</em></p><p><em>(200-300 words)</em></p></div><hr>")

        file.write("<h3 style='color:red'>"+ s2aItem+"</h3>")
        if s2aItem == "Annexure Part A and B (Version 1)":
            file.write("<p>Annexure version 1 info goes here</p>") 
        else:
            file.write("<p>Annexure version 2 info goes here</p>")
        file.write("<hr><h3 style='color:red'>"+ s2bItem+ "</h3>")
        if s2bItem == "Bill of quantities (Version A)":   
            file.write("<p>Bill of quantities version A goes here</p>")
        else:
           file.write("<p>Bill of quantities version B goes here</p><hr>")     
        file.write("<p style='font-size: 9px'>ID:"+assignID)
        indexWriter.writerow([currentStudent,assignID])

        #close the file
        file.close()
        setupLists()
    indexFile.close()

main()