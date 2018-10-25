$(document).ready(function(){
    $('.sidenav').sidenav();
});

$('.dropdown-trigger').dropdown({
	coverTrigger: false
});

$(document).ready(function(){
    $('.modal').modal();
});

$(document).ready(function(){
    $('.datepicker').datepicker();
});
$(document).ready(function(){
    $('.cpf').mask('000.000.000-00');
    $('.cep').mask('00000-000');
    $('.telefone').mask('(00) 0000-0000');
    $('.celular').mask('(00) 00000-0000');
});