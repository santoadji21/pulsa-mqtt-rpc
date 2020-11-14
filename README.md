# Simple MQTT and RPC for top up The Balance

## Description

This repository contains a Simple MQTT and RPC for top up The Balance.

## Usage

### Dependencies

To running this program make sure that the following dependencies library are installed on python3 in your system:
  - zerorpc
  - paho-mqtt

### Project structure

```
pulsa-mqtt-rpc/ 
|- Payment.py  		  #as server for Provider
|- Provider.py      #as server for buyer and as client in Payment
|- Buyer.py        	#as client in Provider
```

Running Program Sequentially

## References

- [Zerorpc](https://www.zerorpc.io/)
- [MQTT](https://mqtt.org/)
- [Wikipedia: Remote Procedure Call ](https://en.wikipedia.org/wiki/Remote_procedure_call)
