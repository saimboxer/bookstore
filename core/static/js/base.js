
var a=0;
function add_optional_field()
{   
    
    a= a+1;
    // create div for attribute
    // let attrdiv = document.createElement('div');
    // attrdiv.classList.add('col-sm-2');
    // attrdiv.id = "divattr";

    // create attribute field
    let attr = document.createElement("INPUT");
    attr.setAttribute("type", "text");
    attr.setAttribute("name", "attr"+a);
    attr.id = "attr"+a;
    attr.classList.add('form-control');
    attr.setAttribute("placeholder", "Attribute");

    // create div for attribute value
    // let attrvaldiv = document.createElement('div');
    // attrvaldiv.classList.add('col-sm-10');
    // attrvaldiv.id = "divattrval";

    // create attribute value field
    let attrval = document.createElement("INPUT");
    attrval.setAttribute("type", "text");
    attrval.setAttribute("name", "attrval"+a);
    attrval.id = "attrval"+a;
    attrval.classList.add('form-control');
    attrval.setAttribute("placeholder", "Attribute Value");

    // append everything
    //let optionaldiv = document.querySelector('#optionalFields');

    // optionaldiv.appendChild(attrdiv);

    document.querySelector('#divattr').appendChild(attr);
    document.querySelector('#divattrval').appendChild(attrval);
    $('#optional_fields_count').val(a);
}

function remove_optional_field()
{
    document.getElementById("attr"+a).remove();
    document.getElementById("attrval"+a).remove();
    a= a-1;
    $('#optional_fields_count').val(a);
}