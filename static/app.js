let currentEmp = '';
let empNoteList = new Object;


function arrayOfEmployees() {
    let emps = [];
    $('.employees-int').each( function(i, val) {
        emps.push($(val).text());
    })
    return emps;
}

// Create array of employees for employee dropdown selection on interaction page
$('.dropdown').on('click', "a", function(e) {
    e.preventDefault()
    arrayOfEmployees()
})

// function for creating an object to hold interactions for each employee
function createNotesObject() {
    let emps = arrayOfEmployees()
    let keys = Object.keys(empNoteList)
    if (keys.length === 0) {
        for (let e of emps) {
            empNoteList[e] = [];
            return empNoteList
        }
    } else {
        return empNoteList;
    }
}

// Displaying employee name on interaction page
$('.employees-int').on("click", function(e) {
    e.preventDefault();
    let $empNameTitle = $('#employee-name-title').text()
    let empName = e.target.innerText;
    if ($empNameTitle) {
        $('#employee-name-title').text('');
        $('#employee-name-title').append(empName);
        currentEmp = empName;
    } else {
        $('#employee-name-title').append(empName);
        currentEmp = empName;
    }
    $('#emp-info').removeClass('d-none');
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
    let notes = createNotesObject()
    let noteContent = $.trim($('textarea').val());
    let $notesHead = $('#notes-header').text();
    let timestamp = moment().format("MMM Do, h:mm a");

    if (noteContent != '') {
        notes[currentEmp].push(noteContent)

        $('.interaction-list').append(
            `<li class="note-link text-decoration-none"
            id="note-${notes[currentEmp].indexOf(noteContent)}" >
            <a>${$notesHead} on ${timestamp}</a></li>`
            );

    } else {
        alert('Please enter note!')
    }
})

// displaying the interaction link
$('.interaction-list').on('click', 'li', function(e) {
    e.preventDefault()
    let notes = createNotesObject();
    $('#note-display').text(notes[currentEmp]);
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

}, 1000);