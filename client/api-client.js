 function callClickApi() {

    return $.get("http://127.0.0.1:5000/my-link/", function (data) {
        return data;
    });

}