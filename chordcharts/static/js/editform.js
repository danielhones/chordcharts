// Name space for ChordChart:
var Ch = {};

$(function() {
    // TODO: There's probably a better way to do this, ie first check for changes so it doesn't waste
    //
    Ch.livePreviewInterval = setInterval(Ch.livePreview, 200);
});


Ch.livePreview = function livePreview() {
    var title = $('#edit-pane form input[name="title"]').val();
    var artist = $('#edit-pane form input[name="artist"]').val();
    var album = $('#edit-pane form input[name="album"]').val();
    var plain_text = $('#edit-pane form textarea').val();
    var data = {
	title: title,
	artist: artist,
	album: album,
	plain_text: plain_text
    };
    
    var request = $.post('/parse/', data);
    request.done(function(r) {
	$('#preview-pane').html(r);
    });
	    
}
