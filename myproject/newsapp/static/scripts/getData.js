// just to get the users phone number
$(document).ready(function(e){

  // get the necessary
  var username = $('#email').val();
  console.log(username);
  $.ajax({
    type: 'GET',
    url: '/get_user_info/'+username,
    headers: {
        'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val()
    },
    // set the values of attribute when you get the data related to the user
    success:function(data){
      $('#mobile').val(data)
    },
    error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
    },
  });
});
