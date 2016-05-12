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

  var $photoGrid = $('.photo-grid').masonry({
    itemSelector: '.grid-item',
    gutter: 20,
    fitWidth: true
  });

  $photoGrid.imagesLoaded().progress(function() {
    $photoGrid.masonry('layout');
  });
});
