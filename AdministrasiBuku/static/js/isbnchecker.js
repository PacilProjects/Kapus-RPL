$(document).ready(function(){
    $("#isbn").change(function(){
        var isbn = $("#isbn").val();
        $.ajax({
            url: "/administrasi-buku/checkisbn/",
            data : {
                'isbn': isbn
            },
            dataTyope: 'json',
            success: function(data){
                if (data.is_taken) {
                    document.getElementById("isbn-error").innerHTML = "Buku dengan ISBN tersebut sudah terdaftar"
                    return false;
                }
                else{
                    document.getElementById("isbn-error").innerHTML = ""
                    return true;
                }
            },
        })
    });
});