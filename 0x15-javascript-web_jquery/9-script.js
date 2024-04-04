const Translation = async () => {
    const res = await fetch(
        "https://hellosalut.stefanbohacek.dev/?lang=fr"
    );
    const data = await res.json();
    const helloTranslation = data.hello
    return helloTranslation
};

Translation().then(hello => {
    $("DIV#hello").append(hello)
})
  
 
  