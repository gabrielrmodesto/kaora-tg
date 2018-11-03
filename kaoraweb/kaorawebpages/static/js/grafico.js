var ctx = document.getElementById("myChart");
var dadosMusculos = JSON.parse('{{ dadosMusculos| safe }}');
var dia = JSON.parse('{{ dia|safe }}');

var graficoPaciente = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dia,
        datasets:[{
            label: 'Dados Musculares',
            data: dadosMusculos,
            borderWidth: 6,
			borderColor: 'rgba(77,166,253,0.85)',
			backgroundColor: 'transparent',
        }]
    },
    options: {
        title: {
            display: true,
            fontSize: 20,
            text: 'Analise Muscular do Paciente',
        },
        labels:{
            fontStyle: 'bold',
        },
    }
});
