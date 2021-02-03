const notes = new Object
let numNotes = Object.keys(notes).length


$('.employees-int').on("click", function(e) {
    e.preventDefault();
    let $empName = $('#employee-name-title').text()
    if ($empName) {
        $('#employee-name-title').text('');
        $('#employee-name-title').append(e.target.innerText);
    } else {
        console.log(e)
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
        console.log(e)
        $notesHead.append(e.target.innerText)
    }
})

// Adding a timestamped interaction and correlating note 
$('#add-note').on('click', function(e) {
    e.preventDefault();
    let $noteContent = $('#note-content').text();
    let $notesHead = $('#notes-header').text();
    let timestamp = moment().format("MMM Do, h:mm a")
    $('.interaction-list').append(`<li><a href="#" id="note-${numNotes}" class="note-link text-decoration-none">${$notesHead} on ${timestamp}</a></li>`);
    notes[numNotes] = $noteContent;
})


$('.note-link').on('click', function(e) {
    e.preventDefault();
    $('#note-display').text(notes[e.target.attribute.id]);
    console.log(notes)
    $('.notes-area').toggleClass("d-none");
})