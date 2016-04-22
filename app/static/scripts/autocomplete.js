// autocomplete.js

$('#search-box').typeahead({
  minLength: 3,
  highlight: true
},
{
  name: 'twitter-usernames',
  source: function(query, syncResults, asyncResults) {
    $.post('/autocomplete', {query: query}, function(data) {
      var usernameList = JSON.parse(data);
      var formattedList = usernameList.map(function(item) {
        return item[0] + ' - ' + item[1];
      });
      asyncResults(formattedList);
    });
  }
});

$('#search-box').change(function(event) {
  event.preventDefault();
  $('#search-box').typeahead('open');
});
