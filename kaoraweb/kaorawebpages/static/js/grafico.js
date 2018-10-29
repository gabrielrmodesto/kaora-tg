var ctx = document.getElementById("paciente-grafico");
var dados_musculos = JSON.parse('{{ dados_musculos| safe }}');
var data = JSON.parse('{{ data|safe }}');

var graficoPaciente = new Chart(ctx, {
    type: 'line',
    data: {
        labels: data,
        datasets:[{
            label: 'Dados Musculares',
            data: dados_musculos,
            borderWidth: 6,
			borderColor: 'rgba(77,166,253,0.85)',
			backgroundColor: 'transparent',
        }]
    },
    options: {
        title: {
            display: true,
            fontSize: 20,
            text: 'Análise Muscular do Paciente',
        },
        labels:{
            fontStyle: 'bold',
        }
    }
});
