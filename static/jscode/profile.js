
function accordionShowHide(id , set){
//    const a = document.getElementsById(id)
    console.log(id)
//    a.removeAttribute("class")
}
function onClickMedia(elm , set){
    const a = document.getElementsByClassName(elm);
    a[0].removeAttribute("class",elm)
    a[0].setAttribute("class",set)
}

