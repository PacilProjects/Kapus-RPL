$(document).ready(function(){
    $("#username").change(function(){
        var username = $("#username").val();
        $.ajax({
            url: "/administrasi-peminjam/checkuser/",
            data : {
                'username': username
            },
            dataTyope: 'json',
            success: function(data){
                if (!data.is_taken) {
                    document.getElementById("username-error").innerHTML = "Username tidak ditemukan"
                    return false;
                }
                else{
                    document.getElementById("username-error").innerHTML = ""
                    return true;
                }
            },
        })
    });
});