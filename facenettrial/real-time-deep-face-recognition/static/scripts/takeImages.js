$(function() {
    // Setup positions
    var positions = []
    for (var i = 0; i < 6; i++) {
        for (var j = 0; j < 5; j++) {
            // positions.push([(i * 100/5).toString() + '%', (j*100/4).toString()+'%'])
            positions.push([(i * 100/5).toString() + '%', (j*100/4).toString()+'%']);
        }
    }

    var i = 0

    var time$ = rxjs.interval(500)
        .pipe(rxjs.operators.take(30))
    
    time$.subscribe(i => {
            $('.look-here').css({top: positions[i][0], left: positions[i][1]});
            $.get( '/take_face_photo', (res) => {
                console.log(res)
            });
        });
});