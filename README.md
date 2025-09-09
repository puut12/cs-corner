link pws:

IMPLEMENTASI STEP BY STEP
1. Membuat Direktori dan Mengaktifkan Virtual Environment
2. Menyiapkan Dependencies dengan membuat requirements.txt dan Membuat Proyek Django bernama CScorner
3. Konfigurasi Environment Variables dan Proyek
4. Menjalankan Server

BAGAN REQUEST CLIENT KE WEB
1. Request Klien: Pengguna mengakses URL tertentu di peramban web.
2. urls.py: Django menerima permintaan dan mencocokkan URL dengan pola yang terdaftar di urls.py. Pola ini mengarahkan permintaan ke view function yang sesuai. Jika URL tidak ditemukan, Django akan memberikan respons 404 Not Found.
3. views.py: Berkas ini berisi logika bisnis. View menerima permintaan, memprosesnya, dan menentukan data apa yang dibutuhkan. Untuk mendapatkan atau memanipulasi data, view akan berinteraksi dengan Model.
4. models.py (Opsional): Model adalah representasi data dan logika bisnis. View menggunakan Model (melalui Django ORM) untuk berinteraksi dengan basis data tanpa perlu menulis SQL langsung.
5. views.py (lanjutan): Setelah mendapatkan data dari Model, view akan mengirimkan data tersebut ke Template untuk ditampilkan.
6. Berkas HTML (Template): Template adalah berkas HTML yang menampilkan data yang dikirimkan oleh view. Template menggunakan sintaks khusus Django untuk menampilkan data secara dinamis.
7. Response Klien: Django mengirimkan respons berupa halaman HTML yang sudah terisi data kepada klien.

PERAN settings.py
1. Mendaftarkan semua aplikasi yang aktif dalam proyek di INSTALLED_APPS. Dengan mendaftarkan aplikasi, Django menemukan models.py, template, dan berkasi lain dari aplikasi tersebut.
2. Mengatur konfigurasi database di DATABASES. DATABASES adalah inti dari koneksi Django dengan database. Disini, ada engine database yang digunakan, nama databasem kredensial pengguna, host, dan port. Dengan konfigurasi, Django dapat berinteraksi dengan database tanpa perlu menulis kode SQL yang masih raw.
3. Mendefinisikan lokasi urls.py utama. ROOT_URLCONF memberi tahu Django menemukan file urls.py utama proyek. File ini memproses dan mengarahkan setiap request yang masuk ke aplikasi.
4. Mengatur konfigurasi template di TEMPLATES untuk memproses file template HTML. Saat APP_DIRS true, Django mencari folder templates di aplikasi yang ada di INSTALLED_APPS. context_processors menambahkan variabel ke template, seperti request, auth, dan messages.
5. Menentutan static files (CSS, JavaScript, Images). STATIC_URL mendefinisikan URL untuk static file

CARA KERJA MIGRASI DATABASE
Migrasi database adalah fitur Django yang mengelola perubahan skema basis data. Proses ini terdiri dari dua langkah yang wajib dilakukan setiap kali mengubah model di file models.py
1. Menjalankan perintah python manage.py makemigrations
Django memindah semua perubahan pada model. Perintah ini akan membuat migrasi baru di dalam folder migrations aplikasi. File ini berisi langkah-langkah untuk mengubah  struktur tabel agar sesuai dengan model.
2. Menjalankan perintah python manage.py migrate
Django membaca file migrasi di langkah sebelumnya dan menerapkan instruksi di dalam basis data. Perintah ini membuat, mengubah, atau menghapus tabel di basis data, sesuai definisi model yang baru. Django juga melacak migrasi mana saja yang sudah diterapkan agar tidak dijalankan dua kali.

ALASAN Django MENJADI PERMULAAN BELAJAR PERANGKAT LUNAK
1. Django menggunakan pola MVT (model, view, template) yang mempermudah pemula memahami dan mengelola setiap bagian aplikasi.
2. Proyek Django memiliki struktur yang teratur sehingga mudah dikelola, diuji, dan diperluaskan.
3. Django berbasis Python, bahasa pemrograman yang mudah dipahami dan dibaca.

FEEDBACK TUTORIAL 1
Tidak ada. Tutorial 1 dapat dipahami dengan baik serta asdos juga stand by di Discord saat saya butuh bantuan.