/** @omm_video **/
odoo.define('metafoormedia.video.scripts', function(require) {
    'use strict';
    
    function generateVimeoPlayer() {
        console.log('Play the movie!!');
    };

    //generateVimeoPlayer();

    var url = window.location.href;
    var page_url = url.replace('#', '?');
    var params = parseURLParams(page_url);
    console.log(params);
});