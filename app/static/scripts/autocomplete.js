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
      asyncResults(usernameList);
    });
  },
  display: function(suggestion) {
    // set input box to Twitter username when suggestion selected
    return suggestion[1];
  },
  limit: 10,
  templates: {
    notFound: '<strong>No suggestions found!</strong>',
    pending: '<em>Loading...</em>',
    suggestion: function(suggestion) {
      // format suggestions correctly: {{Name}} - {{Username}}
      return '<div>' + suggestion[0] + '-' + suggestion[1] + '</div>';
    }
  }
});

$('#search-box').change(function(event) {
  event.preventDefault();
  $('#search-box').typeahead('open');
});
