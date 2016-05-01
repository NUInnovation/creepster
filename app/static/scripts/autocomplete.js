// autocomplete.js

$('#search-box').typeahead({
  minLength: 7,
  highlight: true
},
{
  name: 'twitter-usernames',
  source: function(query, syncResults, asyncResults) {
    $.post('/autocomplete', {query: query}, function(data) {
      var usernameList = JSON.parse(data);
      // pass results into asyncResults callback
      asyncResults(usernameList);
    });
  },
  display: function(suggestion) {
    // set input box to full name when suggestion selected
    return suggestion[0];
  },
  limit: 10,
  templates: {
    notFound: '<strong>No suggestions found!</strong>',
    pending: '<em>Loading...</em>',
    suggestion: function(suggestion) {
      // format suggestions correctly: {{Name}} - {{Username}}
      return '<div>' + suggestion[0] + ' <b style="color:grey">@' + suggestion[1] + '</b></div>';
    }
  }
});
