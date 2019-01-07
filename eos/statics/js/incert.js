$(document).ready(function(){
    alert("good");
    $("#incert").click(function(){
        var user = $("#syscode").val();
        var pwd = $("#sysname").val();
        var pd = {"syscode":user, "sysname":pwd};
        $.ajax({
            type:"post",
            url:"/list",
            data:pd,
            cache:false,
            success:function(data){ 
                window.location.href = "/list";
            },
            error:function(){
                alert("error!");
            },
        });
    });
});
