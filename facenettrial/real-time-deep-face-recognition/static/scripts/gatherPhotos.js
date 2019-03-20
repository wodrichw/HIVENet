$(function() {
$('#trainFaceForm').find('button').click(() => {
    name = $('#trainFaceForm').find('input').val();
    $.ajax({
        type: "POST",
        url: "./training_form",
        data: JSON.stringify({"name": name}),
        contentType: "application/json; charset=utf-8", // this
    }).done((res) => {
        if (res === 'success') {
            window.location.href = '/take_face_photos'
        }
    });
});
});