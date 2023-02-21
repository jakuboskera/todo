(function() {
    var onpageLoad = localStorage.getItem("theme") || "";
    var body = document.body.classList;

    if (onpageLoad == "bootstrap-dark") {
        body.remove("bootstrap");
        body.add("bootstrap-dark")
        document.getElementById('toggle-dark-mode').checked = true;
    }
})();


function SwapThemes() {
    var body = document.body.classList;

    if (body.contains("bootstrap")) {
        body.remove("bootstrap");
        body.add("bootstrap-dark");
    } else {
        body.remove("bootstrap-dark");
        body.add("bootstrap");
    }

    var theme = localStorage.getItem("theme");
    if (theme && theme === "bootstrap-dark") {
        localStorage.setItem("theme", "");
    } else {
        localStorage.setItem("theme", "bootstrap-dark");
    }
}
