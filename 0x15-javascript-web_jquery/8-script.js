$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType: 'json',
    success: function (data) {
      const results = data.results;
      for (const movie of results) {
        const title = $('<li></li>').text(movie.title);
        $('#list_movies').append(title);
      }
    }
  });