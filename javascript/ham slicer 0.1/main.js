let ham_slices_number = 0;
let clickModifier = 1
let multiplier = 1

function numberRefesh () {
    document.getElementById('ham_slices').innerHTML = 'ham slices:' + ham_slices_number * multiplier ;
}

function ham_click () {

    console.log("hai")
    ham_slices_number = ham_slices_number + clickModifier;
    numberRefesh()
}

function shop_click() {
    //needs to be worked on
}

function devHam () {
    ham_slices_number = ham_slices_number + 1000;
    numberRefesh()
}

function butterKnife() { if (ham_slices_number >= 60){
    ham_slices_number = ham_slices_number - 60;
    numberRefesh()
clickModifier = clickModifier + 1;
document.getElementById('butterKnifeId').innerHTML = null; 
document.getElementById('butterKnifeId').style.display = 'none';}
else {}

}

function plasticKnife() { if (ham_slices_number >= 300){
    ham_slices_number = ham_slices_number - 300;
    numberRefesh()
clickModifier = clickModifier + 1;
document.getElementById('plasticKnifeId').innerHTML = null; 
document.getElementById('plasticKnifeId').style.display = 'none';}
else {} }


//work on this 
function betterHam() { if (ham_slices_number >= 1000){
    ham_slices_number = ham_slices_number - 1000;
    numberRefesh()
clickModifier = clickModifier + 1;
document.getElementById('plasticKnifeId').innerHTML = null; 
document.getElementById('plasticKnifeId').style.display = 'none';}
else {}

}

function bestFriend (){
    if (ham_slices_number >= 150){
        ham_slices_number = ham_slices_number - 150;
        numberRefesh()
    setInterval(addHam, 1000);
    document.getElementById('bestFriendId').innerHTML = null;
    document.getElementById('bestFriendId').style.display = 'none';} else {}
}