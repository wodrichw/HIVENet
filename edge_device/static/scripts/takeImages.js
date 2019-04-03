$(function() {
    // Setup positions
    var positions = []
    for (var i = 0; i < 6; i++) {
        for (var j = 0; j < 5; j++) {
            positions.push([(i * 100/5).toString() + '%', (j*100/4).toString()+'%']);
        }
    }

    function takePhotos(i, maxI) {
        $.get( '/take_face_photo', () => {
            if (i < maxI) {
                $('.look-here').css({top: positions[i][0], left: positions[i][1]});
                takePhotos(i+1, maxI);
            } else {
                window.location.href = '/your_photos'
            }
        });
    }

    takePhotos(0, 1);
});