// allows the user to register to the newsapp
$(document).on('submit', ".registeration-form", function(e){
    e.preventDefault();
    console.log('In the method');
    $.ajax({
      type: 'POST',
      url: '/register_account/',
    headers: {
        'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val()
      },
      data:{
        firstname: $('#firstname').val(),
        surname: $('#surname').val(),
        mobile: $('#mobile').val(),
        email: $('#email').val(),
        password: $('#password').val(),
      },
      success:function(data){
        if(data == "success")
        {
          alert("Congrats your account has been created");
        }
        else {
          alert("Sorry, the email already belongs to an account");
          $('#email').css('border', '2px solid red')
        }
      },
      error : function(xhr,errmsg,err) {
              console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      },
    });
  });
