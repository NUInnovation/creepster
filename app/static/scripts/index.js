$(document).ready(function() {

  // Search box
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


  // Masonry
  var $photoGrid = $('.photo-grid').masonry({
    itemSelector: '.grid-item',
    gutter: 20,
    fitWidth: true
  });

  $photoGrid.imagesLoaded().progress(function() {
    $photoGrid.masonry('layout');
  });


  // Image hover effect
  $('.image-card').hover(function(e) {
    var imageHover = e.currentTarget.children[0].children[0].children[0];
    $(imageHover).css({'display': 'block'});
  }, function(e) {
    var imageHover = e.currentTarget.children[0].children[0].children[0];
    $(imageHover).css({'display': 'none'});
  });

});
