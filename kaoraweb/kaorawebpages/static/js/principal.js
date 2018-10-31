//funcao responsavel por abrir menu responsivo
$(document).ready(function(){
    $('.sidenav').sidenav();
});
//funcao responsavel pelo menu dropdown
$('.dropdown-trigger').dropdown({
	coverTrigger: false
});
// funcao responsavel pela abertura de modais
$(document).ready(function(){
    $('.modal').modal();
});
// funcao responsavel pela escolha de datas
$(document).ready(function(){
    $('.datepicker').datepicker();
});
// funcao relacionada a mascara dos inputs
$(document).ready(function(){
    $('.cpf').mask('000.000.000-00');
    $('.cep').mask('00000-000');
    $('.telefone').mask('(00) 0000-0000');
    $('.celular').mask('(00) 00000-0000');
    $('.crefito').mask('00000-A');
});
// funcao para melhorar a visibilidade de imagens
$(document).ready(function(){
    $('.materialboxed').materialbox();
});
// funcao para o select
$(document).ready(function(){
    $('select').formSelect();
});