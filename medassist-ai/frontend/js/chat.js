function addMessage(text,type){

const chat=document.getElementById("chat-window");

const msg=document.createElement("div");

msg.className = type==="user" ? "user-message" : "bot-message";

msg.innerText=text;

chat.appendChild(msg);

chat.scrollTo({
top:chat.scrollHeight,
behavior:"smooth"
});

}



function sendMessage(){

const input=document.getElementById("message");
const text=input.value.trim();

if(text==="") return;


// user message

addMessage(text,"user");

input.value="";


// show typing animation

document.getElementById("typing").classList.remove("hidden");


// simulate AI thinking

setTimeout(()=>{

document.getElementById("typing").classList.add("hidden");

addMessage("Processing your question...","bot");

},1500);

}



// ENTER KEY SUPPORT

document.getElementById("message").addEventListener("keydown",function(e){

if(e.key==="Enter"){

sendMessage();

}

});
function typeBotMessage(text){

const chat=document.getElementById("chat-window");

const msg=document.createElement("div");
msg.className="bot-message";

chat.appendChild(msg);

let i=0;

function typing(){

if(i<text.length){

msg.innerHTML+=text.charAt(i);

i++;

chat.scrollTop=chat.scrollHeight;

setTimeout(typing,20);

}

}

typing();

}
