# import library zerorpc
import zerorpc
# import library paho mqtt
import paho.mqtt.client as mqtt

# inisiasi client mqtt
client = mqtt.Client(client_id="buyer", clean_session=False)
# Koneksikan ke broker 18.218.227.128(aws ec2)
client.connect("18.218.227.128", port=1883)
# Subscribe ke salah satu topik
client.subscribe("/pulsa/1", qos=1)

# Buat fungsi untuk menghandle message yang masuk
def on_message(client, obj, msg):
    #Terima Pesan Dari Provider Kemuda Decode Menjadi Format 'utf-8'
    print(msg.payload.decode('utf-8'))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# Daftarkan fungsi callback
client.on_connect = on_connect
client.on_message = on_message

# nominal= 50000
# nomorhp = 8059642
# saldo = 2000

#User Menginputkan Data Yang Digunakan Untuk Pembelian Pulsa
nominal= int(input("Masukan Nominal \t: "))
nomorhp = input("Masukan Nomorhp \t: ")
saldo = int(input("Masukan Saldo \t\t: "))

#Mengirimkan Data Pembelian Dengan RPC Ke Program Provider (Penyedia Layanan Pulsa)
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4243")
print(c.provider_pulsa(nominal, nomorhp, saldo))

try :
    # Buat infinite loop supaya subscriber tidak mati
    client.loop_forever()
except KeyboardInterrupt :
    print("Buyer Meninggoi .........")