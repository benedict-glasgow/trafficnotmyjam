

$(document).ready(function() { 
    $('#green_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');

        $.get('/traffic/greenreaction/', 
            {'postId': postIdVar}, 
            function(data) { 
                $('#green_count').html(data); 
                $('#green_btn').hide(); 
            })
    });
});

$(document).ready(function() { 
    $('#yellow_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');

        $.get('/traffic/yellowreaction/', 
            {'postId': postIdVar}, 
            function(data) { 
                $('#yellow_count').html(data); 
                $('#yellow_btn').hide(); 
            })
    });
});

$(document).ready(function() { 
    $('#red_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');

        $.get('/traffic/redreaction/', 
            {'postId': postIdVar}, 
            function(data) { 
                $('#red_count').html(data); 
                $('#red_btn').hide(); 
            })
    });
});

$(document).ready(function() { 
    $('#stop_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');

        $.get('/traffic/stopreaction/', 
            {'postId': postIdVar}, 
            function(data) { 
                $('#stop_count').html(data); 
                $('#stop_btn').hide(); 
            })
    });
});


