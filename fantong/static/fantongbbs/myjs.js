$(function() {
    $('input.save.btn.btn-default[postid]').bind("click", function() {
        var pid = $(this).attr("postid");
        var content = $('form.post-form[postid=' + pid + '] textarea').val();
        if (content != '') {
            $.ajax({ url: '/ajax_deal/',
                type: 'post',
                data: { 'PParentID': pid, 'PContent': content },
                success: function(data, textStatus){
                    window.location.reload()
            }
            })
        }
    })
    return true;
});
