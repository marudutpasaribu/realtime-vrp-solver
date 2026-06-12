# VRP Optimization System

Sistem optimisasi logistik untuk menyelesaikan _Vehicle Routing Problem_ (VRP). Proyek ini menggunakan algoritma dari Google OR-Tools untuk mencari rute pengiriman barang yang paling efisien dengan mempertimbangkan batasan kapasitas kendaraan dan lokasi geografis.

---

## Fitur Utama

- **Solver VRP:** Menggunakan `OR-Tools` untuk mencari rute optimal secara efisien.
- **Integrasi Data:** Mengambil data lokasi nyata dari OpenStreetMap menggunakan `OSMnx`.
- **Perhitungan Jarak:** Menggunakan rumus _Haversine_ untuk menghitung jarak antar titik secara akurat.
- **API Ready:** Dilengkapi dengan endpoint API menggunakan `FastAPI` untuk integrasi sistem secara real-time.
- **Visualisasi:** Mendukung pembuatan visualisasi rute hasil optimisasi menggunakan `Matplotlib`.
- **Evaluasi Otomatis:** Memiliki skrip untuk mengukur performa (_benchmarking_) waktu dan jarak (menggunakan `pandas`).

---

## Logika Matematis

### Tujuan (Objective Function)

Meminimalkan total jarak tempuh seluruh kendaraan:
**Minimalkan: Σ d(i, j) \* x(i, j)**

### Batasan (Constraints)

- **Kunjungan:** Setiap pelanggan (node) harus dikunjungi tepat satu kali.
- **Kapasitas:** Total beban pada setiap kendaraan tidak boleh melebihi kapasitas yang ditentukan.
- **Depot:** Setiap rute harus dimulai dan diakhiri di Depot (pusat lokasi).

---

## Cara Menjalankan

1. **Install library yang dibutuhkan:**
   ```bash
   pip install -r requirements.txt
   ```
