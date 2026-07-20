fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const list = document.querySelector('#list_movies');
    data.results.forEach((film) => {
      const li = document.createElement('li');
      li.textContent = film.title;
      list.appendChild(li);
    });
  });
  