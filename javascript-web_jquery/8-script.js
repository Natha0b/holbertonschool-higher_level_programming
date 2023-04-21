$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const movies = data.results;
    const list = $('#list_movies');
    for (let i = 0; i < movies.length; i++) {
      const movieTitle = movies[i].title;
      list.append('<li>' + movieTitle + '</li>');
    }
  });
});
