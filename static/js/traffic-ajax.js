//Deals with Green Reaction Button
$(document).ready(function() { 
    $('#green_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');
        var getUrl = $(this).attr('data-url');

        $.get(getUrl, 
            {'postId': postIdVar}, 
            function(data) { 
                $('#green_btn').text(data); 
            })
    });
});

//Deals with Yellow Reaction Button
$(document).ready(function() { 
    $('#yellow_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');
        var getUrl = $(this).attr('data-url');

        $.get(getUrl, 
            {'postId': postIdVar}, 
            function(data) { 
                $('#yellow_btn').text(data); 
            })
    });
});

//Deals with Red Reaction Button
$(document).ready(function() { 
    $('#red_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');
        var getUrl = $(this).attr('data-url');

        $.get(getUrl, 
            {'postId': postIdVar}, 
            function(data) { 
                $('#red_btn').text(data); 
            })
    });
});

//Deals with Stop Reaction Button
$(document).ready(function() { 
    $('#stop_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');
        var getUrl = $(this).attr('data-url');

        $.get(getUrl, 
            {'postId': postIdVar}, 
            function(data) { 
                $('#stop_btn').text(data);
            })

    });
});


