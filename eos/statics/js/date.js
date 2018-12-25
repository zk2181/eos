$(document).ready(function(){
    $("#create").click(function(){
        alert("admin");
        var tabledate = $("#htmldate").val();
        var pd1 = {"htmldate":tabledate};
        $.ajax({
            type:"post",
            url:"/admin",
            data:pd1,
            cache:false,
            success:function(data){ 
                alert("good!");
                window.location.href = "/list";
            },
            error:function(){
                alert("error!");
            },
        });
    });
});
