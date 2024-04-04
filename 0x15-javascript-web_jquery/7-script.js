const Name = async () => {
  const res = await fetch(
    "https://swapi-api.alx-tools.com/api/people/5/?format=json"
  );
  const data = await res.json();
  const name = data.name;
  return name;
};

Name().then((name) => {
  $("DIV#character").append(name)
});
