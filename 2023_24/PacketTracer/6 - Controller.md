# WLAN Controller

In questo esempio vogliamo riprodurre una situazione reale dove abbiamo una rete wireless che utilizza wireless access point e un server DHCP per assegnare automaticamente gli indirizzi IP ai devices che si connetteranno alla rete wireless protetta con WPA.  

Topologia della rete:  

![LAB-NAT](imgs/WIFIController/WLAN-Controller.png)  

Configurazione del wireless LAN controller:  

![LAB-NAT](imgs/WIFIController/2-ControllerConf.png)  

Setto un SSID per identificare la mia rete e una password  

![LAB-NAT](imgs/WIFIController/3-ConfigurazioneControllerWirelessLAN.png)  

A questo punto configuro il server DHCP in modo tale da poter assegnare gli IP automaticamente agli host collagati:  

![LAB-NAT](imgs/WIFIController/4-ConfigurzioneDHCPWirelessLanController.png)  


Aggiungo un laptop e cotrollo se sono disponibili delle reti alle quali potermi collegare:  

![LAB-NAT](imgs/WIFIController/5-ConnessioneWifiLaptop.png)  


Configurazione finale con laptop collegato:  

![LAB-NAT](imgs/WIFIController/6-ConfigurazioneFinale.png)  
