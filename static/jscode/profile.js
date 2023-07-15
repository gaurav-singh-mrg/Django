
function accordionShowHide(id , set){
    const a = document.getElementById(id)
    console.log(a)
    console.log('Gauravsingh')
//    a.removeAttribute("class")
}
function onClickMedia(elm , set) {
    let a;
    a = document.getElementsByClassName(elm);
    a[0].removeAttribute("class", elm)
    a[0].setAttribute("class", set)
}

function btn(id){
    const a = document.getElementById(id);
    const b = a.classList
    if (b[0] === 'show') {
        a.removeAttribute('class', "show")
        a.setAttribute("class", "collapse")
    } else
        a.setAttribute("class", "show")
}


function ChangePicture(src,target){
    const a = document.getElementById(src)
    console.log(a)
    console.log(a.value)
}


function showImage(src,target) {
  var fr=new FileReader();
  fr.onload = function(e) { target.src = this.result; };
  src.addEventListener("change",function() {
    fr.readAsDataURL(src.files[0]);
  });
}

var src = document.getElementById("id_imageField");
var target = document.getElementById("PlaceForProfilePic");
showImage(src,target);


