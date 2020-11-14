# import library zerorpc
import zerorpc

class Payment(object):
    @staticmethod
    def beli_pulsa(nominal, saldo):
        # Cek Saldo dengan Nominal
        if saldo >= nominal:
            saldo -= nominal
            # Jika Saldo lebih dari samadengan nominal maka akkan mengembalikan pesan
            return "Anda Berhasil Membeli Pulsa Rp." + str(nominal) + ' \n' +"Sisa Saldo Anda Adalah Rp." + str(saldo)
        else:
            # Jika Saldo tidak memenuhi syarat lebih dari samadengan nominal maka akkan mengembalikan pesan
            return "\nMaaf Saldo Anda Tidak Cukup Untuk Membeli Pulsa Sebesar Rp." + str(nominal) + '\n' + "Transaksi Dibatalkan ...."

try:
    s = zerorpc.Server(Payment())
    s.bind("tcp://0.0.0.0:4242")
    s.run()
except  KeyboardInterrupt:
    print("Provider Meninggoi ................. ")