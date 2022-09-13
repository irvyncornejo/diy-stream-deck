
class Display{
  /*
   * Nextion
  */
  void showInformation(){};
  void showAlert(){};
  void showControlPanel(){};
};

//Auxiliar Functions
void defineAction(byte displayResponse[8]){
  byte byte1 = displayResponse[1];  // Botón->Error | Slider -> Identificador de memoria 
  byte byte2 = displayResponse[2];  // boton->Página desde donde llega la información desde la pantalla | slider-> Valor del componente
  byte byte3 = displayResponse[3];  // Identificación del componente que ha enviado la información desde la pantalla
  byte byte4 = displayResponse[4];  // Evento del componente que se ha enviado
  byte byte5 = displayResponse[5];  // fin de envío FF
  byte byte6 = displayResponse[6];  // "
  byte byte7 = displayResponse[7];  // "
}
