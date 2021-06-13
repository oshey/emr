$(document).ready(function() {
  $('#cancel-btn').click(function(event){
        event.preventDefault();
        window.history.back();
    })
})