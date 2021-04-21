let selectedEmp = '';
let selectedNote = '';
let selectedTimeNote = '';
let linkCopyList = [];
let linkList = [];
let empNoteList = new Object;


function arrayOfEmployees() {
    let emps = [];
    $('.employees-int').each( function(i, val) {
        emps.push($(val).text());
    })
    return emps;
}

// Create array of employees for employee dropdown selection on interaction page
$('.emp-list-item').on('click', "li a", function(e) {
    e.preventDefault();
    arrayOfEmployees();
    createNotesObject();
})

// function for creating an object to hold interactions for each employee
function createNotesObject() {
    let emps = arrayOfEmployees()
    let keys = Object.keys(empNoteList)
    if (keys.length === 0) {
        for (let e of emps) {
            empNoteList[e] = new Object;
            empNoteList[e]['notes'] = [];
        }
    } 
    return empNoteList;
}

// Displaying employee name on interaction page
$('.employees-int').on("click", function(e) {
    e.preventDefault();
    let $empNameTitle = $('#employee-name-title').text()
    let empName = e.target.innerText;
    selectedEmp = empName

    if ($empNameTitle) {
        $('#employee-name-title').text('');
        $('#employee-name-title').append(empName);

    } else {
        $('#employee-name-title').append(empName);
        
    }

    $('#emp-info').removeClass('d-none');

    createNotesObject();
    showLinks();

    return selectedEmp
})

// Adding notes header with type of interaction
$('.int-action').on('click', function(e) {
    e.preventDefault();
    let $notesHead = $('#notes-header')
    let $notesHeadText = $('#notes-header').text()
    if ($notesHeadText) {
        $notesHead.text('')
        $notesHead.text(e.target.innerText)
    } else {
        $notesHead.append(e.target.innerText)
    }
})

// Adding a timestamped interaction link that leads to correlating note 
$('#add-note').on('click', function(e) {
    e.preventDefault();
    let noteObj = createNotesObject()
    let noteArray = noteObj[selectedEmp]['notes']
    let noteContent = $.trim($('textarea').val());
    let $notesLinkCopy = $('#notes-header').text();
    let timestamp = moment().format("MMM Do, h:mm a");

    let link = `<li class="note-link py-2 w-100"><a>${$notesLinkCopy} on ${timestamp}</a></li>`

    let linkCopy = `${$notesLinkCopy} on ${timestamp}`
    

    let linkAndNote = {
        [linkCopy]:noteContent,
        [link]:noteContent,
        timestamp:timestamp,
        }
    if (noteContent === '') {   
        alert('Please enter note!')
    } else if ($notesLinkCopy === 'Notes'){
        alert('Please select interation type!')
    } else {
        $('.interaction-list').append(link)
        noteArray.push(linkAndNote)
    }
})

// displaying the interaction from correlating link
$('.interaction-list').on('click', 'li', function(e) {
    e.preventDefault()
    let noteObj = createNotesObject();
    let noteArray = noteObj[selectedEmp]['notes']
    let $noteDisplay = $('#note-display')
    let $noteTime = $('#time-of-note')
    let linkCopy = getLinkCopy();


        if ($noteDisplay.text() === "") {
            $noteDisplay.text(noteArray[linkCopy.indexOf(e.target.innerText)][e.target.innerHTML])
            $noteTime.text(noteArray[linkCopy.indexOf(e.target.innerText)]['timestamp'])
        } else {
            $noteDisplay.text('')
            $noteDisplay.text(noteArray[linkCopy.indexOf(e.target.innerText)][e.target.innerText])
            $noteTime.text(noteArray[linkCopy.indexOf(e.target.innerText)]['timestamp'])
        }

    $('.notes-area').removeClass("d-none");
});

// Covid Countdown Timer
setInterval(function time(){
    let d = new Date();
    let hours = 24 - d.getHours();
    let min = 60 - d.getMinutes();
    let sec = 60 - d.getSeconds();

    if ((min + '').length == 1){
        min = "0" + min;
    }

    if ((sec + '').length == 1){
        sec = "0" + sec;
    }

    $('#covid-countdown').text(`${hours}hrs ${min}mins ${sec}s`)

}, 1000)

// Function to display all interaction links for each Employee

    // How do I gather data that holds employee - note relationship?



    // How do I display that information with a list of links?
    function getLinkCopy() {
        let notesArr = empNoteList[selectedEmp]['notes']
        let linkCopy = []
        for (let n of notesArr){
            linkCopy.push(Object.keys(n)[0])
        }
         linkCopyList = linkCopy;
         return linkCopyList;
    }

    function getLinks() {
        let notesArr = empNoteList[selectedEmp]['notes']
        let links = []
        for (let n of notesArr){
            links.push(Object.keys(n)[1])
        }
         linkList = links;
         return linkList;
    }
    // Do they change when the employee changes?
    // Do the links persist?

    function showLinks(){
        $('.interaction-list').text('')
        
        let links = getLinks();
        if (links.length != 0){

            for (let link of links) {
                $('.interaction-list').append(link)
            }
        }
        return links
    }

