# PhotoDownloader

## Deskripsi
**Image Downloader Tool** adalah aplikasi yang memudahkan kamu untuk mengunduh gambar secara massal dari URL yang ada di file Excel atau CSV. Cocok digunakan untuk mengunduh foto dari database atau storage yang URL-nya sudah terstruktur dalam spreadsheet.

**Image Downloader Tool** is an app that helps you download images in bulk from URLs stored in an Excel or CSV file. It's perfect for downloading photos from databases or storages that have their URLs structured in a spreadsheet.

## Fitur

- Pilih file Excel atau CSV yang berisi URL gambar.
- Tentukan folder untuk menyimpan gambar yang diunduh.
- Progress bar untuk melihat status pengunduhan.
- Log untuk menampilkan hasil pengunduhan, apakah sukses atau gagal.
- Menangani error ketika pengunduhan gagal.

- Select an Excel or CSV file that contains image URLs.
- Choose a folder to save the downloaded images.
- A progress bar to show the download status.
- A log to display the download results, whether successful or failed.
- Handles errors when the download fails.

## Screen Shoot

<img width="712" alt="image" src="https://github.com/user-attachments/assets/e5e8406e-a2a4-4673-b355-bb368c9da510" />

<img width="712" alt="image" src="https://github.com/user-attachments/assets/6ea4d270-01b0-4ec9-b815-7a9b6e72a6d8" />


## Kebutuhan Sistem / System Requirements

- Python 3.x
- PyQt6
- pandas
- requests

## Instalasi / Installation

1. Install dependencies menggunakan `pip`:

    ```bash
    pip install PyQt6 pandas requests
    ```

2. Clone atau download repository:

    ```bash
    git clone https://github.com/yourusername/image-downloader.git
    ```

3. Jalankan aplikasi:

    ```bash
    python image_downloader.py
    ```

## Cara Penggunaan / Usage

1. **Pilih File Excel atau CSV**: Klik tombol "Browse" untuk memilih file yang berisi URL gambar. Pastikan kolom URL bernama `photo_path`.

2. **Pilih Folder Output**: Tentukan folder tempat menyimpan gambar yang diunduh.

3. **Mulai Download**: Klik tombol "Start Download" untuk memulai proses pengunduhan. Progress bar akan menunjukkan status pengunduhan.

4. **Log**: Lihat log untuk melihat status pengunduhan gambar. Jika ada gambar yang gagal diunduh, akan tampil pesan kesalahan.

1. **Select Excel or CSV File**: Click the "Browse" button to select the file that contains the image URLs. Make sure the URL column is named `photo_path`.

2. **Choose Output Folder**: Choose a folder to save the downloaded images.

3. **Start Download**: Click the "Start Download" button to begin the download process. The progress bar will indicate the download status.

4. **Log**: Check the log to see the status of the image downloads. If any image fails to download, an error message will appear.

### Format File / File Format

File input kamu harus memiliki kolom bernama `photo_path` yang berisi URL gambar.

Your input file must have a column named `photo_path` containing the image URLs.

| photo_path           |
|----------------------|
| http://example.com/img1.jpg |
| http://example.com/img2.jpg |
| http://example.com/img3.jpg |

### Catatan / Notes
- Mendukung format file Excel (.xlsx) dan CSV (.csv).
- Aplikasi ini hanya mengunduh gambar yang URL-nya valid dan dapat diakses.
- Jika pengunduhan gagal, error akan ditampilkan di log.

- Supports Excel (.xlsx) and CSV (.csv) file formats.
- The app will only download images with valid and accessible URLs.
- If a download fails, an error message will appear in the log.

## Troubleshooting

- **Error: "URL not found"**: Periksa kembali URL gambar di file input.
- **Error: "Timeout"**: Cek koneksi internet atau coba lagi nanti.
- **Progres tidak terupdate**: Pastikan koneksi internet stabil.

- **Error: "URL not found"**: Double-check the image URLs in your input file.
- **Error: "Timeout"**: Check your internet connection or try again later.
- **Progress not updating**: Ensure your internet connection is stable.

## Kontribusi / Contributing
Silakan kirim pull request jika ingin menambahkan fitur atau perbaikan.

Feel free to submit a pull request if you want to add features or fix issues.

## Lisensi / License
MIT License - lihat file [LICENSE](LICENSE) untuk detail.

MIT License - see [LICENSE](LICENSE) file for details.
