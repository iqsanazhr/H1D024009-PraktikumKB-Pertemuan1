"""
Program Analisis Nilai Mahasiswa
================================
Program ini menganalisis data nilai mahasiswa menggunakan:
1. Struktur Kontrol  : if-elif-else, for loop, while loop
2. Struktur Data      : list, dictionary, tuple
3. Library            : statistics, random, datetime
"""

import statistics
import random
from datetime import datetime

# ============================================================
# 1. STRUKTUR DATA
# ============================================================

# Dictionary berisi data mahasiswa (nama: list nilai)
data_mahasiswa = {
    "Andi": [85, 90, 78, 92, 88],
    "Budi": [70, 65, 80, 75, 72],
    "Citra": [95, 98, 92, 97, 94],
    "Dina": [60, 55, 58, 62, 50],
    "Eko": [88, 82, 79, 85, 90],
}

# Tuple untuk batas nilai grade
batas_grade = (
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "E"),
)

# List untuk menyimpan hasil analisis
hasil_analisis = []


# ============================================================
# 2. STRUKTUR KONTROL + LIBRARY (statistics)
# ============================================================

def tentukan_grade(rata_rata):
    """Menentukan grade berdasarkan rata-rata nilai (if-elif-else)."""
    # Struktur kontrol: if-elif-else
    if rata_rata >= 90:
        return "A"
    elif rata_rata >= 80:
        return "B"
    elif rata_rata >= 70:
        return "C"
    elif rata_rata >= 60:
        return "D"
    else:
        return "E"


def tentukan_status(grade):
    """Menentukan status lulus/tidak berdasarkan grade."""
    if grade in ("A", "B", "C"):
        return "LULUS"
    else:
        return "TIDAK LULUS"


def analisis_mahasiswa(nama, nilai_list):
    """Menganalisis data seorang mahasiswa menggunakan library statistics."""
    rata_rata = float(statistics.mean(nilai_list))
    median = float(statistics.median(nilai_list))
    stdev = float(statistics.stdev(nilai_list)) if len(nilai_list) > 1 else 0.0
    nilai_max = max(nilai_list)
    nilai_min = min(nilai_list)
    grade = tentukan_grade(rata_rata)
    status = tentukan_status(grade)

    rata_rata_rounded: float = int(rata_rata * 100) / 100.0
    stdev_rounded: float = int(stdev * 100) / 100.0

    return {
        "nama": nama,
        "nilai": nilai_list,
        "rata_rata": rata_rata_rounded,
        "median": median,
        "stdev": stdev_rounded,
        "nilai_max": nilai_max,
        "nilai_min": nilai_min,
        "grade": grade,
        "status": status,
    }


# ============================================================
# 3. PROGRAM UTAMA
# ============================================================

def main():
    # Library datetime: menampilkan waktu analisis
    waktu_sekarang = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print("=" * 60)
    print("        PROGRAM ANALISIS NILAI MAHASISWA")
    print(f"        Waktu Analisis: {waktu_sekarang}")
    print("=" * 60)

    # Struktur kontrol: for loop - iterasi setiap mahasiswa
    for nama, nilai in data_mahasiswa.items():
        hasil = analisis_mahasiswa(nama, nilai)
        hasil_analisis.append(hasil)

    # Tampilkan hasil per mahasiswa
    print(f"\n{'No':<4} {'Nama':<10} {'Rata-rata':<12} {'Median':<8} "
          f"{'StDev':<8} {'Max':<6} {'Min':<6} {'Grade':<7} {'Status'}")
    print("-" * 75)

    nomor = 1
    # Struktur kontrol: for loop
    for h in hasil_analisis:
        print(f"{nomor:<4} {h['nama']:<10} {h['rata_rata']:<12} "
              f"{h['median']:<8} {h['stdev']:<8} {h['nilai_max']:<6} "
              f"{h['nilai_min']:<6} {h['grade']:<7} {h['status']}")
        nomor += 1

    # --------------------------------------------------------
    # Statistik keseluruhan
    # --------------------------------------------------------
    semua_rata = [h["rata_rata"] for h in hasil_analisis]
    rata_kelas = statistics.mean(semua_rata)
    tertinggi = max(hasil_analisis, key=lambda x: x["rata_rata"])
    terendah = min(hasil_analisis, key=lambda x: x["rata_rata"])

    # Hitung jumlah lulus dan tidak lulus
    jml_lulus: int = 0
    jml_tidak: int = 0
    # Struktur kontrol: for loop + if-else
    for h in hasil_analisis:
        if h["status"] == "LULUS":
            jml_lulus = jml_lulus + 1  # type: ignore
        else:
            jml_tidak = jml_tidak + 1  # type: ignore

    print("\n" + "=" * 60)
    print("                 RINGKASAN KELAS")
    print("=" * 60)
    print(f"  Rata-rata Kelas     : {rata_kelas:.2f}")
    print(f"  Nilai Tertinggi     : {tertinggi['nama']} ({tertinggi['rata_rata']})")
    print(f"  Nilai Terendah      : {terendah['nama']} ({terendah['rata_rata']})")
    print(f"  Jumlah Lulus        : {jml_lulus} mahasiswa")
    print(f"  Jumlah Tidak Lulus  : {jml_tidak} mahasiswa")
    persen: float = float(jml_lulus) / float(len(hasil_analisis)) * 100
    print(f"  Persentase Kelulusan: {persen:.1f}%")

    # --------------------------------------------------------
    # Library random: simulasi pengacakan soal ujian
    # --------------------------------------------------------
    print("\n" + "=" * 60)
    print("         SIMULASI PENGACAKAN SOAL UJIAN")
    print("=" * 60)

    bank_soal = [
        "Apa itu Kecerdasan Buatan?",
        "Jelaskan perbedaan AI dan Machine Learning!",
        "Sebutkan contoh penerapan AI dalam kehidupan!",
        "Apa itu Neural Network?",
        "Jelaskan algoritma pencarian (Search Algorithm)!",
        "Apa yang dimaksud dengan NLP?",
        "Sebutkan jenis-jenis Machine Learning!",
        "Apa itu Deep Learning?",
        "Jelaskan konsep supervised learning!",
        "Apa fungsi activation function pada neural network?",
    ]

    jumlah_soal = 5
    soal_terpilih = random.sample(bank_soal, jumlah_soal)

    print(f"\n  Dari {len(bank_soal)} soal, dipilih {jumlah_soal} soal secara acak:\n")

    # Struktur kontrol: while loop
    i = 0
    while i < len(soal_terpilih):
        print(f"  {i + 1}. {soal_terpilih[i]}")
        i += 1

    print("\n" + "=" * 60)
    print("  Program selesai. Terima kasih!")
    print("=" * 60)


if __name__ == "__main__":
    main()
