int readLDRSensor(){
  int ldrValue = map(analogRead(ANALOG_PIN),0,4095,0,100);
  return ldrValue;
}
