var updateBtns = document.getElementsByClassName('card-button')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId, action)

        console.log(user)
        if(user === 'AnonymousUser'){
            console.log("Not logged in")
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    var url = '/update_item/'
    console.log('url',url)
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        location.reload()
    })
}
$(function() {
    $(window).scroll(function() {
      var x = $(window).scrollTop();
      if (x >= 300) {
        $("#header-logo").hide("1000");
      }
      else {
        $("#header-logo").show("1000");
      }
    });
  });

