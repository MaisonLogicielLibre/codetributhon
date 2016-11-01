$(function(){

    $('.body').backstretch([
        "../../../static/img/bg/2.jpg"
    ]);

     $("#form-lang").on("change", function() { 
         $(this).submit();
     });

});
