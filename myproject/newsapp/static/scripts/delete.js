$(document).on('click', '.delete_comment', function(e){
  // prevent the page from reloading when the comment id deleted or not
    e.preventDefault();
    // get necessary values to delete comment
    var comment_id = $(this).attr('id');
    var comment = $(this).parent();
    // ajax call
    $.ajax({
      // method type
       type: 'DELETE',
       // url to be called
       url: '/delete_comment/'+comment_id,
       headers: {
           'X-CSRFTOKEN': $("[name=csrfmiddlewaretoken]").val(),
         },
         // data to passed on to the url in the servwer
       data: {
         id: comment_id,
       },
       // on success remove the comment
       success:function(){
         comment.remove();
       },
       // display any errors in the console log
       error : function(xhr,errmsg,err) {
               console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
       },
     });
});
