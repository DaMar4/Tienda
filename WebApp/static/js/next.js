var params = new URLSearchParams(window.location.search)
if(params.has("next"))
    document.getElementById("next").value = params.get("next")