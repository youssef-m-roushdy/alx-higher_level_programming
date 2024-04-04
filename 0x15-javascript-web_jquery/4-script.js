$( "div#toggle_header" ).on( "click", function() {
    if(!($("header").hasClass("red"))){
        $( "header" ).removeClass( "green" );
        $( "header" ).addClass( "red" );
    }
    else{
        $( "header" ).removeClass( "red" );
        $( "header" ).addClass( "green" );
    }
  });