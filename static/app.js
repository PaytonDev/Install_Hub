// Create array of employees
$('.dropdown').on('click', "a", function(e) {
    e.preventDefault()
    let emps = [];
    let empobj = new Object; 
    $('.employees-int').each( function(i, val) {
        emps.push($(val).text());
        return emps;
    })
})


$('.employees-int').on("click", function(e) {
    e.preventDefault();
    let $empName = $('#employee-name-title').text()
    if ($empName) {
        $('#employee-name-title').text('');
        $('#employee-name-title').append(e.target.innerText);

    } else {
        $('#employee-name-title').append(e.target.innerText);
    }
    $('#emp-info').removeClass('d-none');

})

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

// Adding a timestamped interaction and correlating note 
$('#add-note').on('click', function(e) {
    e.preventDefault();
    let noteContent = $.trim($('textarea').val());
    let $notesHead = $('#notes-header').text();
    let timestamp = moment().format("MMM Do, h:mm a");
    let numNotes = Object.keys(notes).length

    if (noteContent != '') {
    $('.interaction-list').append(`<li class="note-link text-decoration-none" id="note-${numNotes}" >${$notesHead} on ${timestamp}</a></li>`);
    notes[`note-${numNotes}`] = noteContent;
    console.log(noteContent)
    return notes
    } else {
        alert('Please enter note!')
    }
})


$('.interaction-list').on('click', 'li', function(e) {
    e.preventDefault()
    console.log(e)
    $('#note-display').text(notes[e.target.id]);
    $('.notes-area').removeClass("d-none");
});

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