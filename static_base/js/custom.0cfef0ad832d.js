
// const myButton = document.getElementById("reply_btn");


// myButton.addEventListener("click", function(){

//     const details = document.getElementById("all_replies");

//     if (details.classList.contains('d-none')){
//         details.classList.remove('d-none');

//     }
//     else{
//         details.classList.add('d-none');
 
//     }


// })


const myButton = document.getElementById("reply_btn");

myButton.addEventListener("click", function(){
    
    he = document.getElementsByTagName("h3");
    he.style.color ="blue;"

    const replies = document.getElementById("d-none");
        replies.classList.remove('d-none');
})
