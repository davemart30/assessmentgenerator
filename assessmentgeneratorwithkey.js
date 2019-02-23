// Use JS injection into html elements to generate random components of the assessment item

// @param list: an Array   BASED ON SOURCE FROM: https://j11y.io/snippets/random-unique/
// @param alias: name for getter function,
//               by default it's "getItem"

var examID = '';

function RandomList(list, alias) {
    if (!list) { return; }
    var length = list.length;
    this.indexes = [];
    this.remainingItems = function () {
        return this.indexes.length;
    };
    this[alias || 'getItem'] = function () {
        var rand = Math.floor(Math.random() * this.indexes.length),
            item = list[this.indexes[rand]];
        this.indexes.splice(rand, 1);
        examID = item.substring(0, 2) + examID;
        item = item.substring(3);
        return item;
    };
    while (length--) {
        this.indexes[this.indexes.length] = length;
    }
}


//Question 1 options
var q1list = [
    'H1.Formal instrument',
    '1Z.AS4000-1997 - General conditions of contract',
    '43.AS4000-1997 - Annexure Part A',
    'B4.AS4000-1997 - Annexure Part B',
    '15.Scope of Works',
    '6P.Program',
    'KL.Bill of quantities',
    'WK.Technical specifications',
    'G2.Construction drawings'
];

var q2list = [
    '27.the parties to the Contract',
    '8G.dimensions for the Works',
    '3R.the type and amount of security to be provided by the Contractor',
    'R4.the contract sum',
    'DD.the person nominated to act on behalf of the Principal',
    'QU.the scope of the Works',
    'HT.the conditions upon which the Contractor is to be given possession of site',
    'T8.details of the Contractor&#39s obligation to notify of a delay', 
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
	'29.how much information about the project that the Contractor can include in it&#39s industry magazine advertising'
];

var s2alist = [
    '3G.<li>Annexure Part A and B (Version 1)</li>',
    '32.<li>Annexure Part A and B (Version 2)</li>'
];

//var s2blist = [
//    'PI.<li><a href="Bill of quantities (Version A).pdf" target="blank">Bill of quantities (Version A)',
//    'IT.<li><a href="Bill of quantities (Version B).pdf" target="blank">Bill of quantities (Version B)'
//]
var s2clist = [
    //1
    '51.<li>Date of acceptance of tender = 02/06/2017.</li><li>The Contractor&#39s overheads and profit percentage was agreed: 13% \
    </li><li>The Contractor did not reach practical completion until one week ago: 01/06/2018 \
    </li><li>The Superintendent has certified a cumulative total amount of $560,000.00 to be added to the contract sum. \
    </li><li>Eight weeks ago the Contractor issued a notice of dispute but the dispute has not been resolved.',
    //2
    '8U.<li>Date of acceptance of tender = 12/06/2017.</li><li>The Contractor&#39s overheads and profit percentage was agreed: 13% \
    </li><li>The Contractor did not reach practical completion until one week ago: 01/06/2018 \
    </li><li>The Superintendent has certified a cumulative total amount of $560,000.00 to be added to the contract sum. \
    </li><li>Eight weeks ago the Contractor issued a notice of dispute but the dispute has not been resolved.',
    //3
    'SQ.<li>Date of acceptance of tender = 02/06/2017.</li><li>The Contractor&#39s overheads and profit percentage was agreed: 15% \
    </li><li>The Contractor did not reach practical completion until one week ago: 01/06/2018 \
    </li><li>The Superintendent has certified a cumulative total amount of $560,000.00 to be added to the contract sum. \
    </li><li>Eight weeks ago the Contractor issued a notice of dispute but the dispute has not been resolved.',
    //4
    '4M.<li>Date of acceptance of tender = 12/06/2017.</li><li>The Contractor&#39s overheads and profit percentage was agreed: 15% \
    </li><li>The Contractor did not reach practical completion until one week ago: 01/06/2018 \
    </li><li>The Superintendent has certified a cumulative total amount of $560,000.00 to be added to the contract sum. \
    </li><li>Eight weeks ago the Contractor issued a notice of dispute but the dispute has not been resolved.'
];

var q4alist = [
    '1Y.According to AS4000 what actions should the Contractor have taken within 6 weeks after the contract date?',
    'YY.According to AS4000 what actions should the Principal have taken within 6 weeks after the contract date?'
];

var q4blist = [
    //1
    'CC.<p style="text-indent: 70px">BQ07 = 5156.0 sq m</p> \
    <p style="text-indent: 70px">BQ11 = 2,497.2 sq m</p> \
    <p style="text-indent: 70px">BQ12 = 0</p> \
    <p style="text-indent: 70px">BQ16 = 4,681.5 sq m</p> \
    <p style="text-indent: 70px">BQ20 = 12,096.4 sq m</p> \
    <p style="text-indent: 70px">BQ21 = 3,618.0 sq m</p>',
    //2
    '72.<p style="text-indent: 70px">BQ07 = 5130.2.0 sq m</p> \
    <p style="text-indent: 70px">BQ11 = 2484.7 sq m</p> \
    <p style="text-indent: 70px">BQ12 = 0</p> \
    <p style="text-indent: 70px">BQ16 = 4,682.7 sq m</p> \
    <p style="text-indent: 70px">BQ20 = 12,097.6 sq m</p> \
    <p style="text-indent: 70px">BQ21 = 3,599.9 sq m</p>',
    //3
    '37.<p style="text-indent: 70px">BQ07 = 5181.5 sq m</p> \
    <p style="text-indent: 70px">BQ11 = 2,509.6 sq m</p> \
    <p style="text-indent: 70px">BQ12 = 0</p> \
    <p style="text-indent: 70px">BQ16 = 4,729.5 sq m</p> \
    <p style="text-indent: 70px">BQ20 = 12,218.6 sq m</p> \
    <p style="text-indent: 70px">BQ21 = 3,635.9 sq m</p>'
];

var q5list = [
    //1
    'G2.<ol type="i" style="margin-left: 70px"> \
        <li>the amount invoiced by a subcontractor to the Contractor for work done under a provisional sum was as follows: \
        <p style="text-indent: 70px">Provisional Sum = $108,000.00</p> \
        <p style="text-indent: 70px">Subcontractor invoice =  $94,500.00</p></li> \
        <li>the artwork in Item B/Q 012 of the bill of quantities is <strong><em>deleted</em></strong> from the Contract</li> \
        <li>the <em><strong>total cost</strong></em> to the Contractor of work carried out by the Contractor in relation to a provisional sum was as follows:  \
        <p style="text-indent: 70px">Provisional Sum = $107,500.00</p> \
        <p style="text-indent: 70px">Contractors <strong><em>costs</em></strong> = $98,900.00</p></li> \
    </ol>',
    //2
    'M8.<ol type="i" style="margin-left: 70px"> \
        <li>the amount invoiced by a subcontractor to the Contractor for work done under a provisional sum was as follows: \
        <p style="text-indent: 70px">Provisional Sum = $108,000.00</p> \
        <p style="text-indent: 70px">Subcontractor invoice =  $94,500.00</p></li> \
        <li>the artwork in Item B/Q 012 of the bill of quantities is <strong><em>deleted</em></strong> from the Contract</li> \
        <li>the <em><strong>total cost</strong></em> to the Contractor of work carried out by the Contractor in relation to a provisional sum was as follows:  \
        <p style="text-indent: 70px">Provisional Sum = $105,700.00</p> \
        <p style="text-indent: 70px">Contractors <strong><em>costs</em></strong> = $98,900.00</p></li> \
    </ol>'
];

var q6list = [
    //1
	'OZ.<p>You are the Superintendent for the contract described in the assignment scenario and a situation has arisen where, although you are not certain, you suspect that the quality of one face of a reinforced concrete footing may not meet the requirements of the specification. Unfortunately, the footing was backfilled before you had an opportunity to inspect the workmanship.</p> \
	<p>Prepare a notice to the Contractor, directing it to open up the work for inspection. It should also inform the Contractor of the possible consequences of this direction, and of any defective work that may be revealed by the inspection.</p> ',
	//2
    'GR.<ul><li>you are the Superintendent for the Contract</li> \
		<li>the Contractor is obliged to effect insurance of the Works</li> \
		<li>the date for giving the Contractor possession of the site has passed</li> \
		<li>whilst the Contractor asserts that the insurance has been effected, it has not provided any evidence of such insurance to the Principal</li></ul> \
	<p>Prepare a notice to the Contractor, informing it of the contractual consequences of its failure to comply with the Contract.</p>',
    //3
    'EA.<ul><li>you are the Superintendent for the Contract</li> \
		<li>heavy rain caused the sides of a deep excavation which is part of WUC to become unstable </li> \
		<li>a residential building on the adjacent lot is likely to be undermined and collapse within hours unless emergency shoring work is carried out urgently </li> \
		<li>it is after midnight and the Contractor&#39s representative has not been contactable for the past 2 hours</li></ul> \
	<p>Prepare a notice to the Contractor, informing it that the Principal intends to take the urgent action necessary to prevent collapse of the neighbouring building and advising of the contractual consequences of the Contractor&#39s failure to take action.</p>',
    //4
    'TT.<ul><li>you are the Contractor&#39s representative for the Contract</li> \
		<li>the Principal has not made any payment of moneys due for more than two months</li> \
		<li>two weeks ago, in accordance with Cl 39.8 you gave the Principal a notice to show cause within eight days of the notice</li> \
		<li>the Principal has not replied</li></ul> \
	<p>Prepare a notice to the Principal informing it that the Contractor is suspending the whole of WUC, and advising of the potential consequences of the Principal&#39;s failure to show cause.</p>'
];

var q7list = [
    '01.identities of the parties to the Contract',
	'PQ.details of substantial breaches by the parties',
	'UB.how a construction program is instigated',
	'M3.identity of a nominated subcontractor',
	'6T.risks of loss or damage to WUC for which the Principal is liable',
	'RM.whether the bill of quantities forms part of the Contract',
	'SV.from whom the Contractor is required to take instructions/directions',
	'88.in what manner the Superintendent should act',
	'N9.the primary obligations of the parties to the Contract',
	'A0.the period after a party becomes aware of a claim in relation to a Superintendent&#39ss direction within which the party is required to issue a notice of dispute',
	'EO.an explicit statement defining a substantial breach by the Principal that is caused by a failure of the Superintendent',
	'OC.whether the Superintendent has the authority to prevent the Contractor from removing it&#39s own equipment from the site once it is no longer required',
	'ZX.who is responsible for the cost of rectifying damage classified under Cl 15.1 d)',
	'0E.the purpose for which the Principal is permitted to copy the documents in Cl 8.3 a)',
	'QP.how the work required to rectify damage caused by an excepted risk is valued',
	'40.the Contractor&#39s obligation to avoid interference with the ability of pedestrians to move past the site',
	'SC.what measures the Contractor can take if the Superintendent does not respond as required under Cl 34.6 after receiving the Contractor&#39ss request for issue of a certificate of practical completion'
];


var q8list = [
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
];

var q9list = [
    'VG.In escrow',
	'B1.Time bar',
    'IJ.Prescribed notice',
    '3D.Contract sum'
];

// Construct the random lists the old way
var q1div = document.getElementById('q1list');
var injectq1list = new RandomList(q1list);
// Retrieve items randomly and display for q1;
q1div.innerHTML += "<ol><li>" + injectq1list.getItem() + "</li><br /><li>" + injectq1list.getItem() + "</li><br /><li>" + injectq1list.getItem() + "</li></ol>";

// Construct q2
var q2div = document.getElementById('q2list');
var injectq2list = new RandomList(q2list);
// Retrieve items randomly and display for q1;
q2div.innerHTML += "<ol><li>" + injectq2list.getItem() + "</a></li><br /><li>" + injectq2list.getItem() 
 + "</li><br /><li>"+ injectq2list.getItem() + "</li><br /><li>" + injectq2list.getItem() + "</li><br /><li>" + injectq2list.getItem() + "</li></ol>";

// Construct scenario 2 part a
var s2adiv = document.getElementById('s2a');
var injects2alist = new RandomList(s2alist);
// Retrieve items randomly and display for scenario 2 part a;
s2adiv.innerHTML += "<ul>" + injects2alist.getItem() + "</li></ul>";

// Construct scenario 2 part b - not used in 182
//var s2bdiv = document.getElementById('s2b');
//var injects2blist = new RandomList(s2blist);
// Retrieve items randomly and display for scenario 2 part a;
//s2bdiv.innerHTML += "<ul>" + injects2blist.getItem() + "</li></ul>";

// Construct scenario 2 part c
var s2cdiv = document.getElementById('s2c');
var injects2clist = new RandomList(s2clist);
// Retrieve items randomly and display for scenario 2 part c;
s2cdiv.innerHTML += "<ol type='A'>" + injects2clist.getItem() + "</li></ul>";

// Construct task 4 question 1
var q4adiv = document.getElementById('q4a');
var injectq4alist = new RandomList(q4alist);
// Retrieve items randomly and display for Task 4 q1;
q4adiv.innerHTML += "<li>" + injectq4alist.getItem() + "</li>";

// Construct task 4 question 3
var q4bdiv = document.getElementById('q4b');
var injectq4blist = new RandomList(q4blist);
// Retrieve items randomly and display for Task 4;
q4bdiv.innerHTML += injectq4blist.getItem();

// Construct task 5 
var q5div = document.getElementById('q5');
var injectq5list = new RandomList(q5list);
// Retrieve items randomly and display for Task 5;
q5div.innerHTML += injectq5list.getItem() + "</p>";

// Construct task 6
var q6div = document.getElementById('q6');
var injectq6list = new RandomList(q6list);
// Retrieve items randomly and display for Task 6;
q6div.innerHTML += injectq6list.getItem() + "</p>";

// Construct task 7
var q7div = document.getElementById('q7');
var injectq7list = new RandomList(q7list);
// Retrieve items randomly and display for task 7;
q7div.innerHTML += "<ol type='a'><li>" + injectq7list.getItem() + "</li><li>" + injectq7list.getItem() + "</li><li>"
+ injectq7list.getItem() + "</li><li>" + injectq7list.getItem() + "</li><li>"+ injectq7list.getItem() + "</li><li>" +
injectq7list.getItem() + "</li></ol>";


// Construct task 8
var q8div = document.getElementById('q8');
var injectq8list = new RandomList(q8list);
// Retrieve items randomly and display for Task 8;
q8div.innerHTML += '<ol type="a"><li>' + injectq8list.getItem() + "</li><li>" + injectq8list.getItem();

// Construct task 9
var q9div = document.getElementById('q9');
var injectq9list = new RandomList(q9list);
// Retrieve items randomly and display for Task 9;
q9div.innerHTML += '<ol type="a"><li><p>Investigate the term <strong>' + injectq9list.getItem() + '</strong>, then</li><li>Describe <strong><em>in your own words</em></strong>:';

// Add examID
var examiddiv = document.getElementById('examid');
examiddiv.innerHTML += '<p style="font-size: 9px">ID: ' + examID + '</p>';
