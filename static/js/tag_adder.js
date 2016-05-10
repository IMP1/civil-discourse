var tag_list = document.getElementById("added-tags");
var hidden_elements = document.getElementById("hidden-elements");
var new_tag_textbox = document.getElementById("new-tag");

new_tag_textbox.onfocus = function() { 
    new_tag_textbox.classList.remove('error') 
    
};

function new_tag_enter(e, search_link) {
    if (e.keyCode == 13) {
        add_tag(search_link);
        // e.stopPropagation();
        return false;
    }
    return true;
}

function add_tag(search_link) {
    var tag_name = new_tag_textbox.value;
    if (!tag_name || tag_exists(tag_name)) {
        new_tag_textbox.classList.add('error');
        return;
    }

    var hidden_element = document.createElement("input");
    var icon = document.createElement("span");
    var tag = document.createElement("a");
    var li = document.createElement("li");
    var remove_button = document.createElement("button");
    
    hidden_element.setAttribute('name', 'tags');
    hidden_element.setAttribute('type', 'hidden');
    hidden_element.setAttribute('value', tag_name);
    hidden_elements.appendChild(hidden_element);

    icon.classList.add("fa");     icon.classList.add("fa-lg");
    icon.classList.add("fa-tag"); icon.classList.add("user-tag");

    remove_button.onclick = function() { remove_tag(li, hidden_element); };
    remove_button.setAttribute('type', 'button');
    remove_button.setAttribute('title', "Remove tag: " + tag_name);
    remove_button.classList.add("undecorated");
    remove_button.classList.add("fa");
    remove_button.classList.add("fa-close");

    tag.href = search_link + "?search_tag=" + tag_name;
    tag.setAttribute('target', '_blank');
    tag.setAttribute('title', "Search for tag: " + tag_name);
    tag.classList.add("tag");
    tag.appendChild(icon);
    tag.appendChild(document.createTextNode("\n" + tag_name));

    li.appendChild(tag);
    li.appendChild(document.createTextNode("\n"));
    li.appendChild(remove_button);
    tag_list.appendChild(li);
    new_tag_textbox.value = "";
}

function tag_exists(tag_name) {
    var items = hidden_elements.getElementsByTagName("input");
    for (var i = 0; i < items.length; ++i) {
        if (items[i].name === "tags" && items[i].value === tag_name) {
            return true;
        }
    }
    return false;
}

function remove_tag(visible_element, hidden_element) {
    visible_element.parentNode.removeChild(visible_element);
    hidden_element.parentNode.removeChild(hidden_element);
}