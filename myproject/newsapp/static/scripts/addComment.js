$(document).on('submit', ".comment-form", function(e){
  // prevent the data from reloading when the comment is added or not
    e.preventDefault();

    var article_id =  $('#article_id').val();
    var user_full_name = $('#user_full_name').val();
    var comment = $('#comment').val();
    var today = new Date();
    // ajax call to be made
    $.ajax({
      // method type
      type: 'POST',
      // the url to be called
      url: '/add_comment/',
      headers: {
        'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val()
      },
      // data to be passed on to the server
      data:{
        article_id: $('#article_id').val(),
        user_full_name: $('#user_full_name').val(),
        comment: $('#comment').val(),
        username: $('#username').val(),
      },
      success:function(data){
        // if successful display the comment with the date, time user name and the content of the comment
        if(data[0] == "success")
        {
          var months = [ "Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
              "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec." ];
            var date = months[today.getMonth(0+1)] + " "+today.getDate()+", "+today.getFullYear()+", ";
            var hours = today.getHours() < 13 ?  today.getHours() :  today.getHours() - 12;
            var minutes = today.getMinutes();
            var am_pm = today.getHours() >= 12 ? "p.m." : "a.m.";
            var time = hours + ":" + minutes + " " + am_pm;
            var dateTime = date+' '+time;
            var result = "<div><p>"+user_full_name + " " +dateTime+"</p> <p>"+comment+"</p> <br> <button class='delete_comment' type='button' name='Delete' id = "+data[1]+">Delete</button><hr></div>";
            $('.comments-list').append(result);
        }
        else
        {
            alert("Comment wasn't posted");
        }
      },
      // display any errors in the console log
      error : function(xhr,errmsg,err) {
              console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      },
    });
  });
