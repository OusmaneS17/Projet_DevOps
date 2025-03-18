function loadDesktopCSS(){
    if(!desktopStylesLoaded&&window.innerWidth>=600){
        for(var e=0,d=document.querySelectorAll('head > link[href*="css"][media="screen and (min-width:37.5em)"]');e<d.length;e++)
           d[e].removeAttribute("disabled");desktopStylesLoaded=!0
        }
    }

var desktopStylesLoaded=!1;
loadDesktopCSS(),window.addEventListener("resize",loadDesktopCSS)
    