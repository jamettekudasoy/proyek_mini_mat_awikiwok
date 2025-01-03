import pyfiglet
import math

def welcome_message():
    message = "PENGHITUNG INTEGRAL DAN VOLUME BENDA PUTAR"
    ascii_art = pyfiglet.figlet_format(message, font="slant", width=100)
    print(ascii_art)

welcome_message()

satuan_str = input("Masukkan satuan panjang (misalnya m, cm, km, etc.): ").strip()

def integral_riemann_left(f, a, b, n):
    dx = (b - a) / n
    total = 0
    for i in range(n):
        x = a + i * dx
        total += f(x)
    return total * dx

def integral_trapesium(f, a, b, n):
    dx = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * dx
        total += f(x)
    return total * dx

def volume_objek(f, a, b, n, method="trapesium"):
    def disk_area(x):
        return math.pi * (f(x) ** 2)
    if method == "riemann":
        return integral_riemann_left(disk_area, a, b, n)
    elif method == "trapesium":
        return integral_trapesium(disk_area, a, b, n)

total_volume = 0
total_integral = 0

while True:
    print("\nMenu Utama:")
    print("1. Metode Riemann")
    print("2. Metode Trapesium")
    print("3. Keluar")

    pilihan = input("Pilih metode (1/2) atau keluar (3): ").strip()

    if pilihan == "1" or pilihan == "2":
        if pilihan == "1":
            metode = "riemann"
            integral_function = integral_riemann_left
            print("Metode Riemann dipilih.")
        else:
            metode = "trapesium"
            integral_function = integral_trapesium
            print("Metode Trapesium dipilih.")

        fungsi_input = input("Masukkan fungsi f(x) (gunakan 'math' untuk fungsi matematika, misal 'math.sin(x)'): ")
        def fungsi(x):
            return eval(fungsi_input)

        a = float(input(f"Masukkan batas bawah (a) dalam {satuan_str}: "))
        b = float(input(f"Masukkan batas atas (b) dalam {satuan_str}: "))
        n = int(input("Masukkan jumlah subinterval (n): "))

        hasil_integral = integral_function(fungsi, a, b, n)
        volume = volume_objek(fungsi, a, b, n, method=metode)

        total_integral += hasil_integral
        total_volume += volume

        print(f"Hasil integral dengan metode {metode}: {hasil_integral:.4f} {satuan_str}^2")
        print(f"Volume benda putar dengan metode cakram ({metode}): {volume:.4f} {satuan_str}^3")

    elif pilihan == "3":
        print(f"\nTotal integral dari semua fungsi: {total_integral:.4f} {satuan_str}^2")
        print(f"Total volume benda putar dari semua fungsi: {total_volume:.4f} {satuan_str}^3")
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Input tidak valid. Silakan coba lagi.")
