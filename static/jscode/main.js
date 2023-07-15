
function hideElement(elm){
    const a = document.getElementsByClassName(elm);
    a[0].removeAttribute("class","msg")
    a[0].setAttribute("class","hidemsg")
}
