var tag_list = document.getElementById("added-tags");

function add_tag(tag_name, search_link) {
  	var li = document.createElement("li");
  	var a = document.createElement("a");
  	a.appendChild(document.createTextNode(tag_name));
  	a.href = search_link + "?search_tag=" + tag_name
  	a.classList.add("tag");
  	li.appendChild(a);
	tag_list.appendChild(li);
}