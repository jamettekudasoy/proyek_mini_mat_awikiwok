import pyfiglet
import math
def welcome_message():
    message = "PENGHITUNG INTEGRAL DAN VOLUME BENDA PUTAR"
    ascii_art = pyfiglet.figlet_format(message, font="slant", width=100)
    print(ascii_art)

welcome_message()

metode_integral = int(input("Pilih metode pengintegralan. 1. Riemann, 2. Trapesium (masukkan angkanya saja): "))

if metode_integral == 1:
    def integral_riemann_left(f, a, b, n):
        """
            f (function): Fungsi yang akan diintegralkan.
            a (float): Batas bawah integral.
            b (float): Batas atas integral.
            n (int): Jumlah subinterval.

        Returns:
            float: Hasil aproksimasi integral.
        """
        # Panjang tiap subinterval
        dx = (b - a) / n

        # Hitung nilai integral dengan metode Riemann kiri
        total = 0
        for i in range(n):
            x = a + i * dx
            total += f(x)

        return total * dx

    def volume_objek (f, a, b, n):
        def disk_area(x):
            return math.pi * (f(x) ** 2)

        return integral_riemann_left(disk_area, a, b, n)

    fungsi_input = input("Masukkan fungsi f(x) (gunakan 'math' untuk fungsi matematika, misal 'math.sin(x)'): ")
    def fungsi(x):
        return eval(fungsi_input)

    a = float(input("Input batas bawah: "))
    b = float(input("Input batas atas: "))
    n = int(input("Input jumlah subinterval: "))

    hasil_integral = integral_riemann_left(fungsi, a, b, n)
    volume = volume_objek(fungsi, a, b, n)

    print(f"Hasil integral dengan metode Riemann kiri: {hasil_integral}")
    print(f"Volume benda putar dengan metode cakram (Riemann kiri): {volume}")

elif metode_integral == 2:
    def integral_trapesium (f, a, b, n):
        dx = (b - a) / n
        total = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            x = a + i * dx
            total += f(x)

        return total * dx

    def volume_objek (f, a, b, n):
        def disk_area(x):
            return math.pi * (f(x) ** 2)

        return integral_trapesium(disk_area, a, b, n)

    fungsi_input = input("Masukkan fungsi f(x) (gunakan 'math' untuk fungsi matematika, misal 'math.sin(x)'): ")
    def fungsi(x):
        return eval(fungsi_input)

    a = float(input("Masukkan batas bawah (a): "))
    b = float(input("Masukkan batas atas (b): "))
    n = int(input("Masukkan jumlah subinterval (n): "))

    hasil_integral = integral_trapesium(fungsi, a, b, n)
    volume = volume_objek(fungsi, a, b, n)

    print(f"Hasil integral dengan metode trapesium: {hasil_integral}")
    print(f"Volume benda putar dengan metode cakram: {volume}")

else:
    print("Input yg bener dawg ^^")
