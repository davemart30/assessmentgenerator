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