$(function() {
    function submitTrainFaceForm() {
        name = $('#trainFaceForm').find('input').val();
        name = name.toLowerCase();
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
    }
$('#trainFaceForm').find('button').click(() => {
    submitTrainFaceForm();
});
$('#trainFaceForm').keydown(function (e) {
    console.log(e)
    if (e.which === 13) { // if e is Enter key
        submitTrainFaceForm();
    }
});
});