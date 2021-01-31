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

$('#add-note').on('click', function(e) {
    e.preventDefault();
    let $noteContent = $('#note-content');
    let $notesHead = $('#notes-header').text();
    let timestamp = moment().format("MMM Do, h:mm a")
    $('.interaction-list').append(`<li><a>${$notesHead} on ${timestamp}</a></li>`);
})

// function addNote() {
//     const intNotes = [];
//     let $intListText = $('.interaction-list li:first-child').text()
//     if ($intListText) {

//     }
// }