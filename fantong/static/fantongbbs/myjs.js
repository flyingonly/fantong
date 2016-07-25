$(function() {
    $('input.save.btn.btn-default[postid]').bind("click", function() {
        var pid = $(this).attr("postid");
        var content = $('form.post-form[postid=' + pid + '] textarea').val();
        if (content != '') {
            $.ajax({
                url: '/ajax_deal/',
                type: 'post',
                data: { 'PParentID': pid, 'PContent': content },
                success: function(data, textStatus) {
                    window.location.reload()
                }
            })
        }
    })
    $('#fileImage').bind("change", function() {
        if ($(this).prop('files')[0].type.indexOf("image") <= -1) {
            alert("请选择图片！");
            return;
        }
        var formdata = new FormData()
        formdata.append("file",$(this).prop('files')[0])
        $.ajax({
            url: "/ajax_append_image/",
            type: "POST",
            data: formdata,
            processData: false,
            contentType: false
        });
        console.log($(this).prop('files')[0].name);
        $("form textarea").append("<img src='" + $(this).val() + "'>")
        alert("{%static asd %}")
    })
});
