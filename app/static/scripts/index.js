$(document).ready(function() {
  $('#search-box').keypress(function(event) {
      if (event.which == 13) {
        event.preventDefault();
        if ($('#search-box').val() !== '') {
          $('form').submit();
          // show loader
          $('#home-content').css("display", "none");
          $('#loader').css("display", "block");
        }
      }
  });
});
