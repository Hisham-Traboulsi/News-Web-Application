$(document).on('submit', ".login-form", function(e){
  //this will prevent the page from realoading in case of failure
  console.log();
  e.preventDefault();
  //initiate the ajax call to pass data to server side
  $.ajax({
    //the method call
    type: 'GET',
    //the url the data is being passed to
    url: '/login_to_account/',
    //this is to set the csrf token to allow the data to be sent to the server side
    headers: {
        'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
    },
    // the data to be sent
    data:{
      email : $('#email').val(),
      password : $('#password').val(),
    },
    //when the data has been validated and is successful run through success
    success:function(data){
      //data will hold any values passed as a json object from server side
      //if the data is successful redirect the user to their account page if not then dont
      if(data == "success")
      {
        alert("Login successful");
        window.location.href = '/account_info';
      }else{
        alert("Login Unsuccessful");
      }
    },
    //display the error in the console
    error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
    },
  });
});
