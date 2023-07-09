

function onClickMedia(elm , remove , set){
    const a = document.getElementsByClassName(elm);
    remove = "msg"
    set ="hidemsg"
    a[0].removeAttribute("class",remove)
    a[0].setAttribute("class",set)
    //a[0].style.display= 'none';
}
