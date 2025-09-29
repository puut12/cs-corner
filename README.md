LINK PWS: https://putri-hamidah-cscorner.pbp.cs.ui.ac.id

**TUGAS 5**

**Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

**JAWABAN**:
1. **Inline Styles**
- Yaitu CSS yang ditulis langsung di dalam HTML (```style="..."```)
- Memiliki prioritas tertinggi dan akan menimpa semua aturan stylesheet eksternal atau internal
- Contoh:
```<p style="color: blue;">Teks ini akan berwarna biru</p>```

2. **ID Selector**
- Menggunakan ID pada tag sebagai selector-nya
- ID bersifat unik dalam satu halaman web
- ID dapat ditambahkan pada halaman template HTML
- Contoh:
```#content { color: blue; }```

3. **Class Selector, Atribut Selector, dan Pseudo-class**
- Class Selector menargetkan elemen berdasarkan atribut class (contoh: ```.date```)
- Atribut Selector menargetkan elemen berdasarkan atributnya (contoh: ```[type="text"]```)
- Pseudo-class menargetkan elemen pada keadaan tertentu (contoh: ```:hover```, ```:focus```)

4. **Element Selector dan Pseudo-element**
- Element Selector menargetkan elemen berdasarkan nama tag HTML-nya (contoh: ```h1```, ```p```)
- Pseudo-element menargetkan bagian tertentu dari sebuah elemen (contoh: ```::before```, ```::after```)

**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**

**JAWABAN**:
1. Pengguna bisa mengakses website dari berbagai perangkat. Dengan responsive design, tampilan akan otomatis menyesuaikan ukuran layar
2. Tidak perlu membuat 2 versi website terpisah. Cukup satu website dengan CSS responsive
3. Google memberi peringkat lebih tinggi pada website yang mobile-friendly. Jadi responsive design bisa meningkatkan visibilitas di mesin pencari dengan SEO (Search Engine Optimization)
4. Website bisa dijangkau siapa saja, baik dari layar kecil maupun besar, tanpa hambatan tampilan

Aplikasi yang sudah menerapkan responsive design: **Netflix**
- Di desktop, Netflix menampilkan banyak thumbnail dalam format grid horizontal
- Di smartphone, tata letaknya berubah menjadi vertikal dengan thumbnail yang lebih besar dan tombol navigasi dipindahkan ke bagian bawah layar, jadinya memudahkan user untuk mengaksesnya dengan satu tangan
- Interaksi hover (menggerakkan kursor di atas elemen) di desktop digantikan dengan satu ketukan di perangkat sentuh. Tombol juga diperbesar agar mudah disentuh
- Menu navigasi yang lebar di desktop berubah menjadi menu hamburger atau bilah navigasi tetap di bagian bawah layar pada perangkat seluler. Ini membuat perpindahan antar halaman lebih mudah

Aplikasi yang belum menerapkan responsive design: **beberapa situs portal kampus seperti SIAK NG**
- Situs-situs ini sering kali memiliki desain tetap (fixed layout) yang dioptimalkan hanya untuk layar desktop
- Saat diakses dari smartphone, tampilannya tidak berubah, sehingga pengguna harus memperbesar layar (pinch-to-zoom) dan menggeser ke samping (scrolling horizontally) untuk membaca konten atau menekan tombol

**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut**

**JAWABAN**:
1. **Margin**
- Merupakan area kosong di luar border
- Fungsinya untuk memberi jarak antar elemen
- Transparan (tidak punya warna)
- Contoh: bikin jarak antara ```<div>``` dengan elemen di sebelahnya
2. **Border**
- Merupakan garis yang mengelilingi padding + content
- Bisa punya warna, ketebalan, dan gaya (solid, dashed, dotted, dll)
- Contoh: bikin kotak dengan garis tepi berwarna hitam
3. **Padding**
- Merupakan area kosong di dalam border, antara border dan isi konten
- Fungsinya untuk memberi ruang agar teks/gambar tidak mepet border
- Transparan, tapi bisa terlihat kalau diberi background

Implementasinya:
```
.box {
    width: 200px;
    background-color: lightblue;

    /* Padding → jarak antara teks dan border */
    padding: 20px;

    /* Border → garis pembungkus */
    border: 5px solid navy;

    /* Margin → jarak elemen ini dengan elemen lain */
    margin: 30px;
}
```

**Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

**JAWABAN**:

**Flexbox (Flexible Box Layout)** adalah sistem layout CSS satu dimensi yang digunakan untuk menyusun elemen dalam baris (row) atau kolom (column) secara fleksibel. Flexbox memungkinkan elemen diatur arah tata letaknya, mudah diposisikan (awal, tengah, akhir), dan ruang antar elemen dapat diatur secara proporsional. Elemen-elemen di dalamnya juga bisa menyesuaikan ukuran otomatis sesuai ruang yang tersedia.

Kegunaan Flexbox:
1. Membuat navbar responsif
2. Menyusun card atau box agar sejajar rapi
3. Mengatur tombol jadi rata tengah atau rata kanan/kiri
4. Menyusun list item agar fleksibel

**Grid Layout** adalah sistem layout CSS dua dimensi yang memungkinkan penyusunan elemen secara horizontal (kolom) dan vertikal (baris). Grid membagi halaman menjadi grid cell (kotak-kotak), jadi  bisa menempatkan elemen dengan mudah sesuai posisi yang diinginkan. Dengan kontrol penuh atas ukuran kolom, baris, dan jarak antar elemen, Grid cocok untuk membuat struktur layout yang kompleks.

Kegunaan Grid:
1. Membuat layout halaman utama (header, sidebar, main content, footer)
2. Menyusun galeri foto dengan jumlah kolom tertentu
3. Mendesain dashboard dengan banyak card teratur
4. Mengatur template halaman dengan struktur yang konsisten

**Implementasi checklist secara step-by-step**

**JAWABAN**:

1. Untuk styling dengan tailwind, di ```templates/base.html```, tambahkan tag ```<meta name="viewport">```, tambahkan script cdn tailwind di bagian head
2. Untuk implementasi fungsi edit product. di ```views.py/main```, tambahkan fungsi ```edit_items``` yang menerima parameter request dan id. Untuk variable ```form_class``` disesuaikan tergantung ```item_category```, ada ```ItemsSizeForm``` dan ```ItemsForm```
3. Buatlah ```edit_itenms.html``` pada ```main/templates```. Isinya dari tutorial 4
4. Di ```urls.py/main```, tambahkan import ```edit_items``` dan ```path('items/<uuid:id>/edit', edit_items, name='edit_items'),```
5. Di ```main.html``` pada ```main/templates```, tambahkan kode untuk tombol edit pada loop ```items_list```
6. Untuk implementasi fungsi delete product. di ```views.py/main```, tambahkan fungsi ```delete_items``` yang menerima parameter request dan id. Isinya dari tutorial 4
7. Di ```urls.py/main```, tambahkan import ```delete_items``` dan ```path('items/<uuid:id>/delete', delete_items, name='delete_items'),```
8. Di ```main.html``` pada ```main/templates```, tambahkan kode untuk tombol delete pada loop ```items_list```
9. Buat ```navbar.html``` di ```templates```, isi masih dari tutorial 4 untuk sementara
10. Pada ```settings.py```, tambahkan middleware WhiteNoise serta konfigurasi STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL
11. Modifikasi ```base.html``` untuk menghubungkan ```global.css``` dan script Tailwind ke ```base.html```. Isi dari tutorial 4
12. Custom styling ke global.css. Isi dari tutorial 4
13. Styling navbar. Ubah berkas ```navbar.html```. Kustomisasi: title di kiri yaitu CS Corner (C-nya biru, S-nya merah, Corner-nya hitam), menu navigasi di tengah (Home, Shoes, Apparel, Balls, Merchandise, Create Product), user section (logout, login, register) di kanan
14. Karena untuk jersey dan jaket itu masuk ke apparel, serta poster dan figur masuk ke merchandise. Jadi, pada fungsi ```show_main``` di ```views.py/main```, tambahkan if else untuk category_name, lalu di ```urls.py/main``` tambahkan ```path('category/<str:category_name>/', show_main, name='show_category'),```
15. Styling halaman login. Ubah berkas ```login.html```. Kustomisasi: tombolnya warna biru, sisanya sama dari tutorial 4
16. Styling halaman register. Ubah berkas ```register.html```. Kustomisasi: tombolnya warna biru, sisanya sama dari tutorial 4
17. Styling halaman home. Buat ```card_items.html``` di ```main/templates```. Tiap card ada foto, nama produk (tebal), deskripsi, harga (tebal), jumlah views di ujung, tombol Selengkapnya di bawah, tombol edit sama delete. Kalau tampilan kosong, muncul ```no-items.png```, jadi ubah juga ```main.html```
18. Styling halaman detail product. Ubah berkas ```items_detail.html```. Kustomisasi: Tombol warna disesuaikan. Mirip tutorial 4, ada name, price, description, size, views
19. Styling halaman create product. Ubah berkas ```create_items.html```. Kustomisasi: Tombol disesuaikan, warnanya juga. Mirip tutorial 4
20. Styling halaman edit product. Ubah berkas ```edit_items.html```. Kustomisasi: Tombol disesuaikan, warnanya juga. Mirip tutorial 4

**TUGAS 4**

**Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**

**JAWABAN**:

Django ```AuthenticationForm``` adalah fitur dari modul ```django.contrib.auth``` untuk menangani proses login user. Form digunakan untuk memvalidasi kredensial username dan password yang dimasukin user.

**Kelebihan**:
- Terintegrasi dengan sistem autentikasi Django, yaitu model User dan fungsi ```login()```
- Otomatis cek apakah username dan password yang dimasukkan cocok dengan data pengguna di database
- Mengurangi risiko kesalahan implementasi
- Mendukung berbagai jenis otentikasi, seperti username dan email

**Kekurangan**:
- Dipakai hanya untuk login, tidak bisa digunakan untuk registrasi atau reset password
- Terikat dengan model ```User``` bawaan Django, jadi jika pakai model user yang berbeda mungkin perlu formulir otentikasi sendiri


**Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**

**JAWABAN**:

**Autentikasi** adalah proses verifikasi identitas user. Contohnya, saat login ke web, sistem akan memeriksa apakah username dan password yang diinput valid.

Sedangkan, **otorisasi** adalah proses menentukan yang diizinkan dan tidak untuk dilakukan oleh user yang terautentikasi. Contohnya, admin bisa mengakses halaman pengelola user, tapi user biasa tidak bisa.

Django mengimplementasikannya dari modul ```django.contrib.auth```. 

Untuk **autentikasi**, bisa pakai;
1. Model ```User``` untuk menyimpan informasi user
2. Form login pakai ```AuthenticationForm``` untuk validasi kredensial
3. Fungsi ```login()``` yang memasukkan sesi user login ke ```request``` dan mengatur ```request.user``` diakses dimana aja.

Untuk **otorisasi**, bisa pakai;
1. ```Permissions``` untuk hak akses tertentu, ada ```add```, ```change```, dan ```delete```
2. ```decorators``` ada ```@login_required``` untuk cek hanya user yang sudah login yang bisa akses dan ```@permission_required``` untuk batasin akses hanya bagi user tertentu
3. ```user.has_perm()``` untuk cek apakah user punya izin tertentu
4. ```user.is_staff``` untuk akses ke Django admin dan ```user.is_superuser untuk semua akses tanpa batasan


**Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**

**JAWABAN**:

```session``` adalah metode di mana data disimpan di server, dan browser user hanya menyimpan Session ID yang unik

**Kelebihan session**:
1. Data sensitif disimpan di server jadi lebih aman dan keamanannya tinggi
2. Kapasitas penyimpanan data hanya dibatasi oleh memori jadi bisa menyimpan data dalam jumlah besar
3. Tidak bergantung pada pengaturan browser user selama user mengizinkan cookies untuk Session ID

**Kekurangan session**:
1. Data disimpan di server jadi butuh memori server ekstra jika ada banyak user yang aktif
2. Data harus dapat diakses oleh semua server jadi perlu shared session storage

```cookies``` adalah data kecil yang disimpan di browser user

**Kelebihan cookies**:
1. Data disimpan langsung di browser user
2. Data cookies dapat diakses offline
3. Server tidak perlu mengalokasikan memori untuk menyimpan informasi user

**Kekurangan cookies**:
1. Ukuran cookies sangat kecil (4KB) jadi tidak cocok untuk menyimpan data yang besar
2. Data yang disimpan di cookies dapat dibaca, dimanipulasi, atau disalahgunakan, sehingga tidak aman untuk menyimpan informasi sensitif 


**Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**

**JAWABAN**:

Penggunaan ```cookies``` tidak sepenuhnya aman. Ada beberapa risiko seperti;
1. **Cross-Site Scripting (XSS)** yaitu menyuntikkan skrip berbahaya ke halaman web. Skrip ini  mencuri informasi sensitif yang disimpan di cookies jika web punya celah keamanan XSS
**Penanganan XSS di Django** yaitu dengan ```HttpOnly flag``` pada cookies. Fitur ini memastikan bahwa session cookie Django tidak dapat diakses oleh skrip di sisi klien
2. Cross-Site Request Forgery (CSRF) yaitu memaksa user melakukan permintaan yang tidak mereka inginkan ke web lain. Jika sesi user disimpan di cookies tanpa perlindungan, permintaan ini akan dianggap valid oleh server
**Penanganan CSRF di Django** yaitu dengan CSRF middleware. Middleware akan otomatis menyisipkan token CSRF ke setiap formulir HTML. Ketika user mengirimkan formulir, server Django akan memvalidasi token tersebut. Jika tokennya tidak cocok, permintaan akan ditolak. Jadinya ini memastikan kalau permintaan POST hanya dari formulir yang sah di situs kita


**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**

**JAWABAN**:

**Fungsi registrasi**
1. Di ```main/views.py```, tambahin import ```UserCreationForm``` dan ```messages```
2. Tambahkan fungsi ```register``` di bawah ini ke dalam ```views.py``` (dari tutorial 3)
3. Buat ```register.html``` pada ```main/templates```. Isi ```register.html``` dari tutorial 3

**Fungsi login**

4. Di ```main/views.py```, tambahin import ```authenticate```, ```login```, dan ```AuthenticationForm```
5. Tambahin fungsi ```login_user``` dari tutorial 3 ke ```main/views.py```
6. Buat ```login.html``` pada ```main/templates```. Isi ```login.html``` dari tutorial 3
7. Di ```main/urls.py```, tambahin import ```login_user``` dan path utl ke ```urlpatterns```

**Fungsi logout**

8. Di ```main/views.py```, tambahin import ```logout```
9. Tambahin fungsi ```logout_user``` dari tutorial 3 ke ```main/views.py```
10. Di ```main.html``` pada ```main/templates```, tambahin kode button Logout setelah tag Add Products
11. Di ```main/urls.py```, tambahin import ```logout_user``` dan path url ke ```urlpatterns```

**Restriksi main.html dan items_detail.html dan data dari cookies**

12. Di ```main/views.py```, tambahin import ```login_required```
13. Tambahin ```@login_required(login_url='/login')``` di atas fungsi ```show_main``` dan ```show_items```
14. Di ```main/views.py```, tambahin import ```HttpResponseRedirect```, ```reverse```, dan ```datetime```
15. Ubah kode di fungsi ```login_user``` untuk menyimpan cookie baru bernama ```last_login```. Kode dari tutorial 3
16. Di fungsi ```show_main```, tambahkan ```'last_login': request.COOKIES.get('last_login', 'Never')``` ke variabel ```context```
17. Ubah fungsi ```logout_user``` untuk menghapus cookie ```last_login```. Kode dari tutorial 3
18. Di ```main.html```pada ```main/templates```, tambahin kode ```<h5>Sesi terakhir login: {{ last_login }}</h5>``` setelah tombol logout
19. Jalankan ```python manage.py runserver``` dan login

**Buat 2 akun pengguna dengan tiga data model**

20. Di localhost, buat 2 akun dan tambahin 3 data products
21. Di PWS, buat 2 akun dan tambahin 3 data products

**Menghubungkan model Product dengan User**

22. Di ```main/models.py```, tambahin import ```User```
23. Pada model ```Items```, tambahin ```user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)```
24. Migrasi model dengan ```python manage.py makemigrations``` dan ```python manage.py migrate```
25. Di ```main/views.py```, ubah ```form.save()``` di ```form.is_valid():``` jadi
    ```
    items_entry = form.save(commit = False)
    items_entry.user = request.user
    items_entry.save()
    ```
26. Di ```main/views.py```, modifikasi awal kodenya jadi
    ```
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        items_list = Items.objects.all()
    else:
        items_list = Items.objects.filter(user=request.user)
    ```
27. Tambahin tombol filter My dan All pada ```main.html```
28. Tampilkan nama author di ```items_detail.html```
29. Jalankan ```python manage.py runserver```
30. add, commit, push ke github dan pws
    
**TUGAS 3**

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawaban:
Data delivery diperlukan untuk saling tukar informasi yang berbeda di sebuah platform. Dalam sebuah platform, data dikirimkan dari satu stack ke stack lainnya.

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawaban:
XML dan JSON sebenarnya sama-sama self describing dan mudah dimengerti, tapi memang JSON lebih populer. 
Alasan JSON lebih populer yaitu:
1. JSON lebih ringkas karena tidak ada tag pembuka dan penutup seperti XML
2. Format JSON mudah dibaca dan ditulis karena mirip objek JavaScript
3. JSON terintegrasi dengan JavaScript jadi pertukaran data lebih efisien

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawaban:
is_valid() berfungsi sebagai validasi data yang diterima user. Method akan cek tiap field di form dan memastikan kalau data yang masuk memenuhi kriteria

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawaban:
csrf_token dibutuhkan sebagai security untuk mencegah serangan berbahaya. Jika form tidak ada csrf_token, bisa ada yang membuat form palsu di web lain yang mengirimkan request ke server kita. Request itu akan diterima dan dijalankan tanpa kita tahu, bisa seperti data dihapus, sandi diubah, dan lainnya.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban:
1. Membuat direktori templates di root folder yang berisi base.html. Isinya dari tutorial 2
2. Modifikasi DIRS di settings.py
3. Membuat forms.py di main untuk struktur form yang menerima data items. Ada 2 class yaitu ItemsForm dan ItemsSizeForm (untuk item jersey dan jaket)
4. Modifikasi views.py di main. Tambahkan Items.object.all() untuk mengambil semua objek Items di database. create_items untuk menghasilkan form yang menambajkan data produk ketika data di submit. show_items untuk mengambil objek News dan jika tidak ada akan ke halaman 404
5. Tambahkan path URL create_items dan show_items ke urlpatterns di urls.py dalam main
6. Di main.html, update content untuk menampilkan data produk dan "Add Product" yang redirect ke halaman form. Sesuaikan tampilannya mau menampilkan atribut apa saja.
7. Di main/templates, buat create_items.html untuk halaman form input detail produk. Sesuaikan isinya apa saja.
8. Di main/templates, buat items_detail.html untuk halaman saat klik 'Read More'. Sesuaikan tampilannya seperti apa untuk semua atributnya.
9. Tambahkan url pws pada CSRF_TRUSTED_ORIGINS di settings.py
10. Routing runserver untuk cek apakah sudah bisa add product dan sudah benar
11. Di main/views.py, tambahkan import HttpResponse dan Serializer, serta fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id
12. Di main/urls.py, tambahkan path URL fungsi tersebut ke urlpatterns
13. Routing runserver lagi dan cek untuk tampilan xml, json, xml by id, dan json by id
14. Cek juga ke postman

Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Jawaban:
Tidak ada, asdos stand by di discord saat tutorial. Jadi pas ada kendala fatal push pws, bisa segera dibantu

Screenshot hasil akses URL pada Postman
![XML](<Screenshot 2025-09-15 221838.png>)
![JSON](<Screenshot 2025-09-15 221614.png>)
![XML by ID](<Screenshot 2025-09-15 221905.png>)
![JSON by ID](<Screenshot 2025-09-15 221926.png>)