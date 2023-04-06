
ButtonOnClick = (val) => {

    query_input = document.getElementById("query")

    if (val == ",") {
        query_input.value -= " ";
        query_input.value += "."
    }
    else {
    query_input.value += (val + " ")
    }
}

