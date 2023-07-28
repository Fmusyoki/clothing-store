
var shop = document.getElementById("#shop-btn");

function myFunction() {
    alert("Hello from a static file!");
  }

function shop() {
    alert("yess");
}

//add to cart



// $("#add-to-cart-btn").click(function(){
//     let quantity = $("#product-quantity").val()
//     let prod_name  = $(".product_name").val()
//     let prod_id  = $(".product_id").val()
//     let prod_price  = $(".price").text()
//     let this_val =$(this)
    
//     console.log("Quantity:", quantity);
//     console.log("Name:", prod_name);
//     console.log("Id:", prod_id);
//     console.log("Price:", prod_price);
//     console.log("Current Element:", this_val);
// });



// var cart = document.getElementById("#add-to-cart-btn");
// function cart(){
//     alert("yess me");

// }
    // var quantity = document.getElementById("#product-quantity").val()
    // var prod_id = document.getElementById("#product_id").val()
//     var prod_name = document.getElementById("#product_name").text()
//     var this_val =document.getElementById(this)
//     console.log('name:', prod_name);
//     console.log("Id:", prod_id);
//     console.log("Current Element:", this_val);
    
//     alert("mee");
// }
$(document).ready(function () { 


    $('#add-to-cart-btn').on("click" , function (e) { 
        e.preventDefault();
        var product_id = $(this).closest('product_data').find('.prod_id').val();
        var product_qty = $(this).closest('product_data').find('#product-quantity').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        $.ajax({
            method: "POST",
            url: "/cart/",
            data: {
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken: token
            },
            dataType: "dataType",
            success: function (response) {
    
                console.log(response)
            }
        });
        
    });
});



// var el = document.getElementById("#add-to-cart-btn");
// el.addEventListener("click", function () {
//      alert('Button Clicked');
// }, false)

