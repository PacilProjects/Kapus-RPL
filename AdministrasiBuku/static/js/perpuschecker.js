$(document).ready(function(){
    $("#nama").change(function(){
        var nama = $("#nama").val();
        $.ajax({
            url: "/administrasi-buku/checkperpus/",
            data : {
                'nama': nama
            },
            dataTyope: 'json',
            success: function(data){
                if (data.is_taken) {
                    document.getElementById("nama-error").innerHTML = "Perpustakaan sudah terdaftar"
                    return false;
                }
                else{
                    document.getElementById("nama-error").innerHTML = ""
                    return true;
                }
            },
        })
    });
});