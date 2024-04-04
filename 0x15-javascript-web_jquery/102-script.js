$(document).ready(function() {
const Translation = async () => {
    const res = await fetch(
        "https://www.fourtonfish.com/hellosalut/hello/"
    );
    const data = await res.json();
    console.log(data.hello)
};


Translation()

})
 
  