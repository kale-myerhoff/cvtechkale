let ham_slices_number = 0;
let clickModifier = 1
let multiplier = 1
let friendCost = 150
let spc = 1;
let hamClickSound =document.getElementById('hamClickSound')
let plantMusic = document.getElementById('plantMusic')
let jazzyNBMusic = document.getElementById('jazzyNBMusic')
let chestOpenSound = document.getElementById('chestOpenSound')
let chestCloseSound = document.getElementById('chestCloseSound')
let shopOpenSound = document.getElementById('shopOpenSound')
let shopCloseSound = document.getElementById('shopCloseSound')
let hamLevel= 1
let chestOpen = false
let shopOpen = false

function addHam(){
    ham_slices_number = ham_slices_number + clickModifier * multiplier;
    numberRefesh()
}


function numberRefesh () {
    document.getElementById('ham_slices').innerHTML = 'ham slices:' + ham_slices_number  ;
    spc= clickModifier * multiplier
    document.getElementById('spc').innerHTML = "slices per click: "+ spc;
}

function ham_click () {
    addHam()
    hamClickSound.play();
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
   clickModifier = clickModifier + 1;
    numberRefesh()
    
document.getElementById('butterKnifeId').innerHTML = null; 
document.getElementById('butterKnifeId').style.display = 'none';}
else {}

}

function plasticKnife() { if (ham_slices_number >= 300){
    ham_slices_number = ham_slices_number - 300;
    clickModifier = clickModifier + 5;
    numberRefesh()
    
document.getElementById('plasticKnifeId').innerHTML = null; 
document.getElementById('plasticKnifeId').style.display = 'none';}
else {} }


//work on this 
function betterHam() { if (ham_slices_number >= 1000){
    ham_slices_number = ham_slices_number - 1000;
    multiplier = multiplier * 2;
    numberRefesh()
document.getElementById('betterHamId').innerHTML = null; 
document.getElementById('betterHamId').style.display = 'none';
if (
    hamLevel < 2
    ) {document.getElementById('Ham-Images').src='images/Better-Ham.png'
        hamLevel = 2
    } else {}
}

else {}

}
function honeyHam() { if (ham_slices_number >= 1000){
    ham_slices_number = ham_slices_number - 1000;
    multiplier = multiplier * 2;
    numberRefesh()
document.getElementById('honeyHamId').innerHTML = null; 
document.getElementById('honeyHamId').style.display = 'none';
if (
     hamLevel < 3 
    )  {document.getElementById('Ham-Images').src='images/HoneyGlazed-Ham.png'
        hamLevel = 3
    } else {}
}

else {}

}

function changefriendCost () {
    document.getElementById('bestFriendId').setAttribute ( 'data-tooltip', "Friend: +1 ham every second / $" + friendCost + " ham" )
}

function bestFriend (){
    if (ham_slices_number >= friendCost){
        ham_slices_number = ham_slices_number - friendCost;
        friendCost = Math.round( friendCost + (friendCost * 0.25))
        console.log(friendCost)
        changefriendCost()
        numberRefesh()
    setInterval(addHam, 1000);
    } else {}
}

function backgroundWhite() {
    document.getElementById("body").style.backgroundColor = "rgb(255, 255, 255)"
    document.getElementById('body').style.backgroundImage = "url(null)"
    document.getElementById("body").style.color = "rgb(0, 0, 0)"
}
function backgroundSBlue() {
    document.getElementById("body").style.backgroundColor = "rgb(255, 255, 255)"
    document.getElementById('body').style.backgroundImage = "url(images/blueStripedBackground.png)"
    document.getElementById("body").style.color = "rgb(255, 255, 255)"
}

function plantMusicFunct() {
    musicStop()
    plantMusic.loop = true; 
    plantMusic.play(); 
    document.getElementById("musicBarId").style.display = "block"
}

function jazzyNBMusicFunct() {
    musicStop()
    jazzyNBMusic.loop = true; 
    jazzyNBMusic.play(); 
    document.getElementById("musicBarId").style.display = "block"
}


function musicPlay() {
    jazzyNBMusic.play();
    plantMusic.play();
    
}

function musicStop() {
    jazzyNBMusic.pause();
    jazzyNBMusic.currentTime =1.95;

    plantMusic.pause();
    plantMusic.currentTime =0;

    document.getElementById("musicBarId").style.display = "none"
}

function chestButton() {
    if (chestOpen == false) {
        document.getElementById('chestId').src = "images/open_chest.png"
        chestOpen = true
        document.getElementById("collectionInside").style.display = "block"
        chestOpenSound.play()

    } else if (chestOpen == true){
        document.getElementById('chestId').src = "images/closed_chest.png"
        chestOpen = false
        document.getElementById("collectionInside").style.display = "none"
        chestCloseSound.play()
    }
}

function shopButton() {
    if (shopOpen == false) {
        shopOpen = true
        document.getElementById("shopInside").style.display = "block"
        shopOpenSound.play()

    } else if (shopOpen == true){
        shopOpen = false
        document.getElementById("shopInside").style.display = "none"
        shopCloseSound.play()
    }
}

