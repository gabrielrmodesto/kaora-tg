#define velocidade 115200
#define porta A3

int dado_musculo;

void setup() {
  // Definindo a velocidade do emg
  Serial.begin(velocidade);
}

void loop() {
  // variavel que ira receber o valor analisado pelo emg
  int dado_musculo = analogRead(porta);
  //printando o valor da variavel
  Serial.println(dado_musculo);
  // imprimindo a cada 1 seg
  delay(1000);
}
