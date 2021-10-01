$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log(id);
    $.ajax(
        {
            type: "GET",
            url: "/pluscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                eml.innerText = data.quantity
            }
        })
});

$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log(id);
    $.ajax(
        {
            type: "GET",
            url: "/minuscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                eml.innerText = data.quantity
                console.log(data);
            }
        })
});

$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var elm = this;
    console.log(id);
    $.ajax(
        {
            type: "GET",
            url: "/removecart",
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log(data);
                window.location.reload()
            }
        })
});


