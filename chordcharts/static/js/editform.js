$(function() {
    $('#preview-button').click(livePreview);
});


function livePreview() {
    var plainText = $('#edit-pane form textarea').val();
    
    var request = $.post('/parse/', plainText);
    request.done(function(r) {
	$('#preview-pane').html(r);
    });
	    
}
