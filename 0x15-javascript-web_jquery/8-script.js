const Titles = async () => {
    const res = await fetch(
        "https://swapi-api.alx-tools.com/api/films/?format=json"
    );
    const data = await res.json();
    const titles = data.results
    return titles
  };
  
 Titles().then(titles => {
    titles.forEach(movie => {
        const movieTitle = `<li>${movie.title}</li>`
        $("UL#list_movies").append(movieTitle)
    });
 })
  