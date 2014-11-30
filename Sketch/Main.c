/**
init variables (red/green/blue - 9/10/11 pins)
**/
int r = 9;
int g = 10;
int b = 11;

/**
Init pin mode
**/
void setup()
{
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);
  
  LEDOff();
  
  Serial.begin(9600);  // initialize serial communications at 9600 bps
}

void loop()
{ 
    while (Serial.available() > 0) {
        int mode = Serial.parseInt();
        Serial.println(mode);
        
        switch (mode) {
            case 1: 
                red();
                break;
            case 2: 
                green();
                break;
            case 3: 
                blue();
                break;
            case 4:
                yellow();
                break;
            case 5: 
                pink();
                break;
            default: 
                LEDOff();
                break;
        }
    }
}

void green()
{
    digitalWrite(b, HIGH); 
    digitalWrite(r, HIGH); 
  
    digitalWrite(g, LOW); 
}
 
void red()
{
    digitalWrite(b, HIGH); 
    digitalWrite(g, HIGH); 
  
    digitalWrite(r, LOW); 
}
 
void blue()
{
    digitalWrite(r, HIGH); 
    digitalWrite(g, HIGH); 
  
    digitalWrite(b, LOW); 
}

void yellow()
{
    digitalWrite(r, 0); 
    digitalWrite(g, 0); 
    digitalWrite(b, 255); 
}

void pink()
{
    digitalWrite(r, 0); 
    digitalWrite(g, 105); 
    digitalWrite(b, 133); 
}

void LEDOff()
{
    digitalWrite(r, HIGH); 
    digitalWrite(g, HIGH);
    digitalWrite(b, HIGH);
}
