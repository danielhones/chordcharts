var Ch = {};  // Name space for ChordChart

$(function() {
    Ch.lastPlainText = $('#edit-pane form textarea').val();
    Ch.livePreviewInterval = setInterval(Ch.livePreview, 100);
});


Ch.livePreview = function livePreview() {
    var title = $('#edit-pane form input[name="title"]').val();
    var artist = $('#edit-pane form input[name="artist"]').val();
    var album = $('#edit-pane form input[name="album"]').val();
    var plain_text = $('#edit-pane form textarea').val();

    if (plain_text !== Ch.lastPlainText) {
	Ch.lastPlainText = plain_text;

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
};
