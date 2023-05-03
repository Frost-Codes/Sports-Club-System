$('.plus-cart').click(function(){
    console.log("button clicked")
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data:",data);
            eml.innerText=data.quantity 
            document.getElementById("amount_tt").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2] 
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity 
            document.getElementById("amount_tt").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})


$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("amount_tt").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove() 
        }
    })
})


$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/pluswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            //alert(data.message)
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})


$('.minus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/minuswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})


$('.form-check-input').click(function(){
    var id = $(this).attr("value")


    $.ajax({
        type:"GET",
        url:"/selectedaddress",
        data:{
            address_id:id
        },
        success:function(data){
            document.getElementById("shipping").innerText=data.shipping_cost
            total_amount_field = document.getElementById("final")
            total_amount_field.value = data.total_amount
        }
    })

})


$('.remove-wishlist').click(function(){
    var id = $(this).attr("pid").toString();

    var to_remove = this.parentNode.parentNode.parentNode.parentNode
    $.ajax({
        type:"GET",
        url:"/removewishlist",
        data:{
            wishlist_id:id
        },
        success:function(data){
            to_remove.remove()
        }
    })
})


