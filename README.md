LINK PWS: https://putri-hamidah-cscorner.pbp.cs.ui.ac.id

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