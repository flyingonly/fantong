
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
                    if (data == "hello") {
                    window.location.reload()
                }
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
        console.log($(this).prop('files')[0]);
        $.ajax({
            url: "/ajax_append_image/",
            type: "POST",
            data: formdata,
            processData: false,
            contentType: false,
            success: function(data, textStatus) {
                $("form textarea").val($("form textarea").val() + "__url_start__" + data + "__url_end__")
            }
        });
        alert("{%static asd %}")
    })
    $('#file').bind("change", function() {
        var formdata = new FormData()
        for (var i = $(this).prop('files').length - 1; i >= 0; i--) {
            formdata.append($(this).prop('files')[i].name,$(this).prop('files')[i])
        }
        console.log($(this).prop('files'));
        $.ajax({
            url: "/ajax_append_files/",
            type: "POST",
            data: formdata,
            processData: false,
            contentType: false,
            success: function(data, textStatus) {
                for (var i = data.length - 1; i >= 0; i--) {
                    $("form textarea").val($("form textarea").val() + "__data_start__" + data[i] + "__data_end__")
                }
            }
        });
        alert("{%static asd %}")
    })
});
