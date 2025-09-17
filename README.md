LINK PWS: https://putri-hamidah-cscorner.pbp.cs.ui.ac.id

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

Tugas 4
Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 