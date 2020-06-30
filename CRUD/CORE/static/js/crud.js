function addNote(){
	$.ajax({
		url:"/add/",
		type:"POST",
		data: $("#form").serialize(),

		success: function(response){
			alert('Nota añadida');
			location.reload();
		},
		error: function(){alert("Ha ocurrido un error")}
	});
}

function delNote(id_note){
	$.ajax({
		url:"/delete/",
		type:"POST",
		data:{
			'id' : id_note,
		},
		success: function(response){
			alert('Nota eliminada');
			location.reload();
		},
		error: function(){alert("Ha ocurrido un error inesperado...")}
	});
}

function updateNote(id_note){
	$.ajax({
		url:"/update/",
		type:"POST",
		data:
		 $("#form_update").serialize(),
		 'id' : id_note,
		

		success: function(response){
			alert('Nota actualizada');
			location.reload();
		},
		error: function(){alert("Ha ocurrido un error inesperado...")}
	});
}
