const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$(document).ready(
    function(){
        setTimeout(
            function(){
                $('#message').fadeOut();
            }, 2000
        )
    }
);
