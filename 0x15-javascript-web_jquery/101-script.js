$(document).ready(function() {
    $("DIV#add_item").on("click", () => {
        const item = "<li>Item</li>";
        $("UL.my_list").append(item);
    });

    $("DIV#remove_item").on("click", () => {
        $("UL.my_list li:last-child").remove();
    });

    $("DIV#clear_list").on("click", () => {
        $("UL.my_list").empty();
    });
});

