"""
Program Analisis Nilai Mahasiswa
================================
Program ini menganalisis data nilai mahasiswa menggunakan:
1. Struktur Kontrol  : if-elif-else, for loop, while loop
2. Struktur Data      : list, set, tuple
3. Library            : statistics, random, datetime
"""

import statistics
import random
from datetime import datetime

# ============================================================
# 1. STRUKTUR DATA
# ============================================================

# List berisi data mahasiswa dalam bentuk tuple (nama, nilai1, nilai2, ...)
data_mahasiswa = [
    ("Andi", [85, 90, 78, 92, 88]),
    ("Budi", [70, 65, 80, 75, 72]),
    ("Citra", [95, 98, 92, 97, 94]),
    ("Dina", [60, 55, 58, 62, 50]),
    ("Eko", [88, 82, 79, 85, 90]),
]

# Tuple untuk batas nilai grade (tidak bisa diubah / immutable)
batas_grade = (
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "E"),
)

# Set untuk menyimpan grade unik yang muncul
grade_muncul = set()

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

    # Struktur kontrol: for loop - iterasi setiap mahasiswa (list of tuple)
    for item in data_mahasiswa:
        nama = item[0]          # Akses elemen tuple index 0
        nilai_list = item[1]    # Akses elemen tuple index 1

        # Library statistics: menghitung statistik nilai
        rata_rata = float(statistics.mean(nilai_list))
        median_val = float(statistics.median(nilai_list))
        stdev_val = float(statistics.stdev(nilai_list)) if len(nilai_list) > 1 else 0.0
        nilai_max = max(nilai_list)
        nilai_min = min(nilai_list)
        grade = tentukan_grade(rata_rata)
        status = tentukan_status(grade)

        # Set: menambahkan grade ke set (otomatis unik, tidak duplikat)
        grade_muncul.add(grade)

        # Simpan hasil ke list
        hasil_analisis.append([nama, rata_rata, median_val, stdev_val,
                               nilai_max, nilai_min, grade, status])

    # Tampilkan hasil per mahasiswa
    print(f"\n{'No':<4} {'Nama':<10} {'Rata-rata':<12} {'Median':<8} "
          f"{'StDev':<8} {'Max':<6} {'Min':<6} {'Grade':<7} {'Status'}")
    print("-" * 75)

    nomor = 1
    # Struktur kontrol: for loop
    for h in hasil_analisis:
        print(f"{nomor:<4} {h[0]:<10} {h[1]:<12.2f} "
              f"{h[2]:<8.1f} {h[3]:<8.2f} {h[4]:<6} "
              f"{h[5]:<6} {h[6]:<7} {h[7]}")
        nomor = nomor + 1

    # --------------------------------------------------------
    # Statistik keseluruhan
    # --------------------------------------------------------
    semua_rata = [h[1] for h in hasil_analisis]
    rata_kelas = float(statistics.mean(semua_rata))

    # Cari mahasiswa dengan nilai tertinggi dan terendah
    tertinggi = hasil_analisis[0]
    terendah = hasil_analisis[0]
    for h in hasil_analisis:
        if h[1] > tertinggi[1]:  # type: ignore
            tertinggi = h
        if h[1] < terendah[1]:   # type: ignore
            terendah = h

    # Hitung jumlah lulus dan tidak lulus
    jml_lulus = 0
    jml_tidak = 0
    # Struktur kontrol: for loop + if-else
    for h in hasil_analisis:
        if h[7] == "LULUS":
            jml_lulus = jml_lulus + 1  # type: ignore
        else:
            jml_tidak = jml_tidak + 1  # type: ignore

    print("\n" + "=" * 60)
    print("                 RINGKASAN KELAS")
    print("=" * 60)
    print(f"  Rata-rata Kelas     : {rata_kelas:.2f}")
    print(f"  Nilai Tertinggi     : {tertinggi[0]} ({tertinggi[1]:.2f})")
    print(f"  Nilai Terendah      : {terendah[0]} ({terendah[1]:.2f})")
    print(f"  Jumlah Lulus        : {jml_lulus} mahasiswa")
    print(f"  Jumlah Tidak Lulus  : {jml_tidak} mahasiswa")

    total = len(hasil_analisis)
    persen = (jml_lulus * 100.0) / total  # type: ignore
    print(f"  Persentase Kelulusan: {persen:.1f}%")

    # --------------------------------------------------------
    # Set: menampilkan operasi himpunan (sesuai modul)
    # --------------------------------------------------------
    print("\n" + "=" * 60)
    print("            OPERASI SET (HIMPUNAN)")
    print("=" * 60)

    semua_grade = {"A", "B", "C", "D", "E"}
    grade_lulus = {"A", "B", "C"}
    grade_tidak_lulus = {"D", "E"}

    print(f"\n  Grade yang muncul         : {grade_muncul}")
    print(f"  Semua grade               : {semua_grade}")

    # Operasi Set: intersection - grade yang muncul DAN termasuk lulus
    lulus_muncul = grade_muncul.intersection(grade_lulus)
    print(f"  Grade lulus yang muncul   : {lulus_muncul}")

    # Operasi Set: difference - grade yang TIDAK muncul
    tidak_muncul = semua_grade.difference(grade_muncul)
    print(f"  Grade yang tidak muncul   : {tidak_muncul}")

    # Operasi Set: union - gabungan grade lulus dan tidak lulus
    gabungan = grade_lulus.union(grade_tidak_lulus)
    print(f"  Union lulus & tidak lulus  : {gabungan}")

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
        i = i + 1

    print("\n" + "=" * 60)
    print("  Program selesai. Terima kasih!")
    print("=" * 60)


if __name__ == "__main__":
    main()
