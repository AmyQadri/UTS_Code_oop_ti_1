# Nama : Andi Muhammad Yusuf Qadri
# Nim : 236250004

class Admin:
    def __init__(self, **kwargs):
        self.name = ""
        self.__cash = 0
        self.address = ""
        self.__learn_cash = 0
        self.daily_work = 10.00
        self.list_worker = []
        self.list_villa = []
        self.list_customer = []

        for key, value in kwargs.items():
            setattr(self,key,value)

    @property
    def cash(self):
        return self.__cash

    @cash.setter
    def cash(self, value):
        try:
            value1 = int(value)
            self.__cash = value1
        except:
            print('Ganti uang harus dalam bentuk angka')

    def villa_learn_cash(self, value):
        try:
            self.__cash = int(value)
        except:
            print("Terjadi Error pada server, Tambah uang harus dalam bentuk angka")

    @property
    def learn_cash(self):
        return self.__learn_cash
    
    @learn_cash.setter
    def learn_cash(self, value):
        try:
            value1 = int(value)
            self.__learn_cash = value1
        except:
            print('Ganti Gaji harus dalam bentuk angka')


    def show_list_villa(self):
        for i, item in enumerate(self.list_villa, start=1):
            print('{}. {}'.format(i,item))

    def add_list_villa(self):
        input1 = str(input("Masukkan nama villa : "))
        if len(input1) >= 3:
            self.list_villa.append(Villa(name=input1))
        else:
            print('Nama Villa harus lebih dari 3 karakter')
            self.add_list_villa()

    def show_list_worker(self):
        for i, item in enumerate(self.list_worker, start=1):
            print('{}. {}'.format(i,item))

    def order_customer(self):
        name_customer = str(input('Masukkan nama pelanggan : '))
        try:
            customer_capacity = int(input('Masukkan jumlah penghuni : '))
            for i, item in enumerate(self.list_villa):
                print(f'{i}. {item}')
                for i, room in enumerate(item.list_room):
                    if customer_capacity <= room.room_capacity:
                        print(i + ' ' + room.room_name)
            try:
                if input_villa <= len(self.list_villa):
                    input_villa = int("Masukkan urutan villa ke berapa")
                    choose_villa = self.list_villa[input_villa-1]
                    input_room = int("Masukkan urutan ruangan ke berapa")
                    if input_room <= len(choose_villa):
                        choose_room = choose_villa.list_room[input_room-1]
                        if choose_room.status != False:
                            self.villa_learn_cash(choose_room.room_price)
                            choose_room.status = False
                            print("Ruangan Berhasil di Pesan")
                        else:
                            print("Ruangan Kotor. Harus di bersihkan sama petugas terlebih dahulu")
                    else:
                        print("Pilihan anda tidak sesuai dengan pilihan ruangan")
                else:
                    print("Pilihan anda tidak sesuai dengan pilihan")
            except:
                print("Masukkan villa sesuai urutan !")
                self.order_customer()
        except:
            print("Harus dalam bentuk angka")
            self.order_customer()

    def add_room_villa(self):
        for i, item in enumerate(self.list_villa):
            print('{}. {}'.format(i,item))
        try:
            input_villa = int(input("Pilih villa yang anda pesan : "))
            if input_villa <= len(self.list_villa):
                choose_villa = self.list_villa[input_villa-1]
                input_name = input("Masukkan nama ruangan")
                input_price = input("Masukkan harga ruangan")
                input_capacity = input("Masukkan kapasitas ruangan")
                input_luas = input("Masukkan luas ruangan")
                if input_price and input_capacity and input_luas:
                    print("Ada yang error pada memasukkan data, tolong masukkan harga, kapasitas ruangan dan luas ruangan di atas 0")
                else:
                    choose_villa.append(Room(name=input_name,room_price=input_price,room_capacity=input_capacity,luas_ruangan=input_luas))
                    print("Anda Berhasil menambahkan ruangan")
        except:
            print("Pilihan harus dalam bentuk angka")

    def main(self):
        menu = '0'
        while menu != '8':
            menu = input("Masukkan Perintah anda : ")
            if menu == '1':
                self.show_list_villa()
            elif menu == '2':
                self.add_list_villa()
            elif menu == '3':
                self.show_list_worker()
            elif menu == '4':
                self.order_customer()
            elif menu == '5':
                self.add_room_villa()
            elif menu == '6':
                print("Menu belum ada")
            elif menu == '7': 
                print("Menu belum ada")
            elif menu == '8':
                print("Anda telah keluar")
            else:
                print("Menu yang anda masukkan salah !")

class Worker:
    def __init__(self,**kwargs):
        self.__name = ""
        self.keletihan = 0
        self.__cash = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.__name

class Customer:
    def __init__(self):
        self.name = ""
        self.cash = 1000000

class Room:
    def __init__(self, **kwargs):
        self.room_name = ""
        self.__room_price = 0
        self.__room_capacity = 0
        self.__luas_ruangan = 0
        self.status = True
        self.kebersihan = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def room_price(self):
        return self.__room_price

    @room_price.setter
    def room_price(self, value):
        try:
            value1 = int(value)
            self.__room_price = value1
        except:
            print("Harga yang anda masukkan salah!\n Harus dalam bentuk angka")

    @property
    def room_capacity(self):
        return self.__room_capacity
    
    @room_capacity.setter
    def room_capacity(self, value):
        try:
            value1 = int(value)
            self.__room_capacity = value1
        except:
            print("kapasitas ruangan yang anda masukkan salah!\n Harus dalam bentuk angka")

    @property
    def luas_ruangan(self):
        return self.__luas_ruangan
    
    @luas_ruangan.setter
    def luas_ruangan(self, value):
        try:
            value1 = int(value)
            self.__luas_ruangan = value1
        except:
            print("luas ruangan yang anda masukkan salah!\n Harus dalam bentuk angka")

class Villa:
    def __init__(self, **kwargs):
        self.name = ""
        self.list_room = []

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.name

admin_villa = Admin(name='Wisata bahari',address='Jalan tombolotutu')
admin_villa.main()