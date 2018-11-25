#define velocidade 9600
#define porta A2
#define ID '1' // identification

int dado_musculo;
int calibragem[10];

void setup() {
  // Definindo a velocidade do emg
  Serial.begin(velocidade);
}

void loop() {
  // variavel que ira receber o valor analisado pelo emg
  int dado_musculo = analogRead(porta);
  for(int i = 0; i < 10; i++){
    calibragem[i] = dado_musculo;
  }
  //printando o valor da variavel
  Serial.println(dado_musculo);
  // imprimindo a cada 1 seg
  delay(500);
}

void serialEvent() // routine of serial event
{
  char receive = Serial.read();
  
  if(receive == ID) // was received the ID
  {
    if(isnan(dado_musculo)) // check error of read 
    {
      Serial.println("{\"error\": \"Falha ao ler o sensor\"}");
    }
    else
    {
      Serial.print("{");
      Serial.print("\"Dados Musculares\": ");
      Serial.print(dado_musculo);
      Serial.print("}");
      Serial.println(); // treat to receive string /r/n. 
    }
  }
}
