// General scheduler

let table = document.getElementById("table-formset");

function cloneMore(selector, prefix) {
    let newElement = $(selector).clone();
    let total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function () {
        var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    return false;
}

function removeItem(element, prefix) {
    let total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1) {
        let node = element.parent().parent()[0];
        table.deleteRow(node.rowIndex);
        total -= 1;
        $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    } else {
        alert("No puede eliminar la fila");
        return false;
    }
}