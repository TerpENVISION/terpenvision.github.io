const APIURL = "https://api.github.com/users/TerpENVISION/repos"

console.log(APIURL)

const menuContent = document.getElementById("menucontent")

isShow = 0


function showBar() {
    if (isShow == 0) {
        menuContent.style.display = "block"
        isShow = 1
    } else if (isShow == 1) {
        menuContent.style.display = "none"
        isShow = 0
    }
}