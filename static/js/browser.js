var browser = browser || {};

browser.getFlashVersion = function() {
    try {
        try {
            var axo = new ActiveXObject('ShockwaveFlash.ShockwaveFlash.6');
            try {
                axo.AllowScriptAccess = 'always';
            } catch(e) {
                return 6;
            }
        } catch(e) {
        }
        return new ActiveXObject('ShockwaveFlash.ShockwaveFlash').GetVariable('$version').replace(/\D+/g, ',').match(/^,?(.+),?$/)[1];
    } catch(e) {
        try {
            if (navigator.mimeTypes["application/x-shockwave-flash"].enabledPlugin) {
                return parseInt((navigator.plugins["Shockwave Flash 2.0"] || navigator.plugins["Shockwave Flash"]).description.replace(/\D+/g, ",").match(/^,?(.+),?$/)[1].split(',')[0]);
            }
        } catch(e) {
        }
    }
    return 0;
};

browser.fullscreen = function(element) {
    if(element.requestFullscreen) {
        element.requestFullscreen();
    } else if(element.webkitRequestFullscreen) {
        element.webkitRequestFullscreen();
    } else if(element.mozRequestFullscreen) {
        element.mozRequestFullScreen();
    }
};