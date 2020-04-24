
const myButton = document.getElementById("reply_btn");


myButton.addEventListener("click", function(){

    const replies = document.getElementById("all_replies");

    if (replies.classList.contains('d-none')){
        replies.classList.remove('d-none');
        myButton.textContent = "Comment";

    }
    else{
        replies.classList.add('d-none');
        myButton.textContent = "Reply";
        

 
    }


})

let showDate = function(message){

    document.getElementById('date').textContent = message 
}


let date = new Date();
showDate(date.toDateString());
