/** @omm_video **/
odoo.define('metafoormedia.video.scripts', function(require) {
    'use strict';
    
    function generateVimeoPlayer() {
        console.log('Play the movie!!');
    };

    //generateVimeoPlayer();

    var url = window.location.href;
    //var page_url = url.replace('#', '?');
    //var params = parseURLParams(page_url);

    //const pageHref = "?page=1&query=javascript";

    // Construct a new object and pass the page href to URLSearchParams
    //const searchParams = new URLSearchParams(pageHref.substring(pageHref.indexOf('?')));
    
    //console.log(searchParams);
    // Output:
    // URLSearchParams { 'page' => '1', 'query' => 'javascript' }

    console.log(url);
});