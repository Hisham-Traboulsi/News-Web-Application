//this is the js code for the like button
$(document).on('click', '.like_article', function(e){
  //dont reload page whne the ajax call is executed
    e.preventDefault();
    //store the data for the like button in variables
    var article_id =  $('#article_id').val();
    var user_full_name = $('#user_full_name').val();
    //ajax call
    $.ajax({
      //method type
      type: 'POST',
      //the url to send the data to
      url: '/rate/',
      headers: {
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val()
      },
      //the data to be sent
      data:{
        article_id: $('#article_id').val(),
        user_email: $('#username').val(),
        rating : "True",
      },
      //when the call has been successful we cheack what value the data is and
      //different functions
      success:function(data){

        if(data == "successful")
        {   //set the color to royalblue for the element with id thumbs-up
           $('#thumbs-up').css("color", "royalblue");
        }
        else if(data == "deletedRating")
        {
          //set the color to white for the element with id thumbs-up
           $('#thumbs-up').css("color", "white");
        }
        else if(data == "switchRating")
        {
          //set the color to white for the element with id thumbs-down
          $('#thumbs-down').css("color", "white");
          //set the color to royalblue for the element with id thumbs-up
          $('#thumbs-up').css("color", "royalblue");
        }
      },
      //display any errors in the console log
      error : function(xhr,errmsg,err) {
              console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      },
    });
});

//this is the js code for the dislike button
$(document).on('click', '.dislike_article', function(e){
    //dont reload page whne the ajax call is executed
    e.preventDefault();
    //store the data for the like button in variables
    var article_id =  $('#article_id').val();
    var user_full_name = $('#user_full_name').val();
    //ajax call
    $.ajax({
      //method type
      type: 'POST',
      //the url to send the data to
      url: '/rate/',
      headers: {
          'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val()
      },
      //the data to be sent
      data:{
        article_id: $('#article_id').val(),
        user_email: $('#username').val(),
        rating : "False",
      },
      //when the call has been successful we cheack what value the data is and
      //different functions
      success:function(data){

        if(data == "successful")
        {
           //set the color to red for the element with id thumbs-down
           $('#thumbs-down').css("color", "red");
        }
        else if(data == "deletedRating")
        {
          //set the color to white for the element with id thumbs-down
           $('#thumbs-down').css("color", "white");
        }
        else if(data == "switchRating")
        {
          //set the color to white for the element with id thumbs-up
          $('#thumbs-up').css("color", "white");
          //set the color to red for the element with id thumbs-down
          $('#thumbs-down').css("color", "red");
        }
      },
      //display any errors
      error : function(xhr,errmsg,err) {
              console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      },
    });
});
