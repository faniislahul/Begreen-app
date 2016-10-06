$(document).ready(function () {
        
        
    var csrftoken = $("input[name = csrfmiddlewaretoken]").val();
        
       
        
    $("#btn1").click(function () {
            
        $("#cat_name").val('');
        $("#cat_desc").val('') ;
        $("#CRUDmodal1").show();
    });
    //////////////////////////
    $("#form1").on('submit', function () {
        event.preventDefault();
        console.log($("#CRUDmodal1").attr("state"));
        if($("#CRUDmodal1").attr("state") == "FALSE" ){  
            console.log("inside")  
            $.ajax( {
                url : '{% url 'crudhandler' %}',
                type : 'POST',
            data : { content : '0' , operation : '0' , name : $("#cat_name").val(), desc : $("#cat_desc").val(), csrfmiddlewaretoken : csrftoken},  
                
            success : function(data){
                console.log(data.result);
                if (data.result['result'] == 4){
                    console.log("success")
                    $("#catlist").append('<li type="cat'+data.result['id']+'"><div class="btn btn-xs btn-primary cat-update" data="'+data.result['id']+'" >Update</div> <div class="btn btn-xs btn-danger cat-delete" data="'+data.result['id']+'">Delete</div> '+ $("#cat_name").val()+'</li>')
                    $("#CRUDmodal1").modal("hide");
                    
                }
                else {
                    console.log ("failed")
                }
            }    
                    
            
                    
        });}
    else {
    $.ajax({
    url : '{% url 'crudhandler' %}',
    type : 'POST',
    data : { content : '0' , operation : '1' , name : $("#cat_name").val(), desc : $("#cat_desc").val(), id : $("#cat-id").val() , csrfmiddlewaretoken : csrftoken},  
                
    success : function(data){
        console.log(data.result);
        if (data.result['result'] == 4){
            console.log("success")
            $('li[type=cat'+$("#cat-id").val()+']').html('<div class="btn btn-xs btn-primary cat-update" data="'+$("#cat-id").val()+'" >Update</div> <div class="btn btn-xs btn-danger cat-delete" data="'+$("#cat-id").val()+'">Delete</div> '+ $("#cat_name").val());
            $("#CRUDmodal1").attr("state", "FALSE"); 
            $("#CRUDmodal1").modal("hide");
        }else{
            console.log("update failed")
        }
                  
                   
                    
    }
                    

};
});
///////////////////////
$("ul").on('click','.cat-update', function(){
            
    var idselected = $(this).attr("data");
    $.ajax({
        url : '{% url 'crudhandler' %}',
        type : 'POST',
    data : { content : '0' , operation : '3' , id : idselected, csrfmiddlewaretoken : csrftoken},  
                
    success : function(data){
        $("#CRUDmodal1").attr("state", "TRUE"); 
        var dash = data.result
        console.log(data.result['name']);
        $("#cat-id").val(idselected);
        $("#cat_name").val(dash['name'])
        $("#cat_desc").val(dash['description'])
        $("#CRUDmodal1").modal("show");
                    
    }
                    
});
});
////////////
$("ul").on('click','.cat-delete', function(){
            
    var idselected = $(this).attr("data");
    $.ajax({
        url : '{% url 'crudhandler' %}',
        type : 'POST',
    data : { content : '0' , operation : '2' , id : idselected, csrfmiddlewaretoken : csrftoken},  
                
    success : function(data){
        var ss = "cat"+idselected
        console.log(ss);
        $('li[type='+ss+']').remove();
                    
    }
                    
});
});

///////////////////////////////////////
/////////////subcat//////////////
//////////////////////////////////////////

$("#btn2").click(function () {
            
    $("#subcat_name").val('');
    $("#subcat_desc").val('') ;
    $("#CRUDmodal2").show();

    ///////////////////////////////
    $("#form2").on('submit', function () {
        event.preventDefault();
        console.log($("#CRUDmodal2").attr("state"));
        if($("#CRUDmodal2").attr("state") == "FALSE" ){  
            //  console.log("inside")  
            $.ajax({
                url : '{% url 'crudhandler' %}',
                type : 'POST',
            data : { content : '1' , operation : '0' , name : $("#subcat_name").val(), desc : $("#subcat_desc").val(),parent : $("subcat_parent").val(), csrfmiddlewaretoken : csrftoken},  
                
            success : function(data){
                console.log(data.result);
                if (data.result['result'] == 4){
                    console.log("success")
                    $("#subcatlist").append('<li type="subcat'+data.result['id']+'"><div class="btn btn-xs btn-primary subcat-update" data="'+data.result['id']+'" >Update</div> <div class="btn btn-xs btn-danger subcat-delete" data="'+data.result['id']+'">Delete</div> '+ $("#subcat_name").val()+'from'+$("#subcat_parent").val()+'</li>');
                    $("#CRUDmodal2").modal("hide");
                    
                }
                else {
                    console.log ("failed")
                }
                   
                    
            }
                    
        });}
    else {
        $.ajax({
    url : '{% url 'crudhandler' %}',
    type : 'POST',
    data : { content : '1' , operation : '1' , name : $("#cat_name").val(), desc : $("#cat_desc").val(), id : $("#cat-id").val() , csrfmiddlewaretoken : csrftoken},  
                
    success : function(data){
        console.log(data.result);
        if (data.result['result'] == 4){
            console.log("success")
            $('li[type=cat'+$("#cat-id").val()+']').html('<div class="btn btn-xs btn-primary cat-update" data="'+$("#cat-id").val()+'" >Update</div> <div class="btn btn-xs btn-danger cat-delete" data="'+$("#cat-id").val()+'">Delete</div> '+ $("#cat_name").val());
            $("#CRUDmodal1").attr("state", "FALSE"); 
            $("#CRUDmodal1").modal("hide");
        }else{
            console.log("update failed")
        }
                    
    }
                    
});
};
});



//////////////////
$(".sub-update").click(function(){
    console.log($( this ).attr("data"));
});
        
});