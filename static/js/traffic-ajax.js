$(document).ready(function() { 
    $('#green_btn').click(function() { 
        var postIdVar; 
        postIdVar = $(this).attr('data-postid');

        $.get('/traffic/reaction/', 
            {'postId': postIdVar}, 
            function(data) { 
                $('#green_count').html(data); 
                $('#green_btn').hide(); 
            })
    });
});


