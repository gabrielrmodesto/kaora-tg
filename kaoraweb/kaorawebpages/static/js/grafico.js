var ctx = document.getElementById("myChart");
var dadosMusculos = JSON.parse('[10,20,30]');
var dia = JSON.parse('["2018-11-10 01:38:26+00:00", "2018-11-03 12:00:00+00:00", "2018-11-14 06:00:00+00:00"]');

var graficoPaciente = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dadosMusculos,
        datasets:[{
            label: 'Dados Musculares',
            data: dia,
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
        },
    }
});
