# import library zerorpc
import zerorpc
# import library paho mqtt
import paho.mqtt.client as mqtt

# Inisiasi mqtt client
client = mqtt.Client(client_id="pulsa", clean_session=False)

# Buat koneksi ke broker
client.connect("18.218.227.128", port=1883)

# Konseksi Provider Sebagai Client ke Payment
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

class Provider(object):
    @staticmethod
    def provider_pulsa(nominal, nomorhp, saldo):
        resi = c.beli_pulsa(nominal, saldo)
        # Publish Pesan ke topik /pulsa/1
        client.publish("/pulsa/1", payload= '\n'+"Anda Akan Membeli Pulsa Sebesar: Rp."  +  str(nominal) + '\n' + "Dengan Nomorhp: " + str(nomorhp) + '\n \n' +  str(resi), qos=1)
        return "Notif Akan Dikirimkan Melalui Protokol MQTT .... "

try:
    # Konseksi Provider Sebagai Server ke Buyer
    s = zerorpc.Server(Provider())
    s.bind("tcp://0.0.0.0:4243")
    s.run()
except  KeyboardInterrupt:
    print("Provider Meninggoi ................. ")