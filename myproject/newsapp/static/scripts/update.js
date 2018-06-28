// update the users existing data such as firstname, and last name
$(document).on('submit', ".update-form", function(e){

  e.preventDefault();
  console.log("In the method");
  console.log($('#mobile').val());
  var username = $('#email').val();

  $.ajax({

    type: 'PUT',
    url: '/update_user_data/'+username,
    headers: {
        'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val()
      },
    data:{
      firstname: $('#firstname').val(),
      surname: $('#surname').val(),
      phone_number: $('#mobile').val(),
    },
    success:function(data){

        console.log(data);
        if(data == "success")
        {
          alert("Update was Successful");

        }
        else if(data=="phone_number") {
          alert("Can't update. Either number is taken or used by you or length is not 11");
        }
        else{
          alert("Update was not Successful");
        }
    },
    error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
    },
  });

});
