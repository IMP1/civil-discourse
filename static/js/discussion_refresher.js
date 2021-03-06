$(document).ready(function(e) {
    setInterval("update_content();", 30000); // 30 seconds
})

function update_content(){
    $.ajax({
        type: "POST",
        url: "", // post it back to itself - use relative path or consistent www. or non-www. to avoid cross domain security issues
        cache: false, // be sure not to cache results
    }).done(function( page_html ) {
        var tempElement = document.createElement('div');
        tempElement.innerHTML = page_html;
        if (tempElement.getElementsByTagName("article")[0].innerHTML != document.getElementsByTagName("article")[0].innerHTML) {
            document.getElementsByTagName("article")[0].innerHTML = tempElement.getElementsByTagName("article")[0].innerHTML;
        }
    });   
}