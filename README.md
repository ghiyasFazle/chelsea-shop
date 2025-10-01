
Link project : https://ghiyas-fazle-chelseashop.pbp.cs.ui.ac.id/

## TUGAS 2 ##
Pertanyaan: 
1.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
: -Pertama saya membuat folder untuk tugas individu
  -mengaktifkan env, menginstall requirements lalu membuat project django baru mengcopy file .env dan env.prod
  -memodifikasi file settings.py
  -menghubungkannya dengan repo github dgn melakukan git init
  -buat app main lalu menambahkan main ke settings
  -membuat folder template dan file main.html
  -mengubah file models sesuai dengan project yang saya buat dgn menambahkan beberapa atribut
  -buat migrations lalu mengubah isi view dan menghubungkannya dengan template
  -mengubah isi template sesuai dengan tema project saya
  -routing url main dan proyek lalu melakukan push ke github dan pws,

2.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
:![alt text](<WhatsApp Image 2025-09-10 at 05.49.11_3efd4862.jpg>)
simpelnya disini urls.py menghubungkan request ke views.py lalu views.py sebagai "bridge" mengambil data dari model dan dikirim ke templates yang mana template tadi akan mengubah hasil akhirnya untuk client.

3.Jelaskan peran settings.py dalam proyek Django!
:settings merupkan tempat untuk menyimpan konfigurasi utama seperti database, apps yang aktif, middleware, template, static files, bahkan keamanan (SECRET_KEY, DEBUG, ALLOWED_HOSTS).

4.Bagaimana cara kerja migrasi database di Django?
:django membaca perubahan yang ada pada models lalu membuat file migrasi dengan command makemigrations dalam berisi operasi SQL python. lalu, migrasi di eksekusi sehingga file di migrate ke database yang juga menyimpan catatan di django_migrations tabel sehingga struktur database selalu sinkron dengan model.

5.Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
:Mungkin karena kemudahan bagi pengguna yang baru belajar. Sebab django sendiri merupakan framework yang tergolong lengkap karena sudah memiliki ORM,admin,authentication,security sehingga relatif aman tanpa harus menambah lapisan keaman lain. Lalu menurut saya juga django adalah framework yang terstruktur, sebab kita di tuntut untuk membuat projek dengan memakai pola Models View dan Template yang bisa dikatan merupakan sebbuah panduan bagi pemula bagaimana merancang sebuah website step by step secara disiplin.

6.Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
: Untuk tutorial 1 asdos sangat membantu di kelas apabila terjadi error .

### TUGAS 3 ###


![alt text](<WhatsApp Image 2025-09-17 at 00.30.05_6a8aa287.jpg>)
![alt text](<WhatsApp Image 2025-09-17 at 00.29.44_6cd4c81b.jpg>)
![alt text](<WhatsApp Image 2025-09-17 at 00.26.58_cddfc2ec.jpg>)
![alt text](<WhatsApp Image 2025-09-17 at 00.27.20_0f6e6b21.jpg>)

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
jawaban: agar memungkinkan terjadinya pertukarat data antara server dan client. data delivery juga memungkinkan integrasi dengan aplikasi lain dan dapat memudahkan pengelolaan dan pemrosesan data.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
jawaban: JSON lebih ringan, lebih mudah dibaca dan dimengerti manusia juga mudah diproses oleh JS (JavaScript). sedangkan xml lebih kompleks karena memerlukan closed tag <>.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
jawaban: method tersebut berguna untuk memeriksa kevalid-an sebuah data yang diinput ke dalam form agar sesuai dengan aturan yang ditentukan. 

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
jawaban: csrf_token sednri sesuai dengan namanya dibutuhkan untuk mencegah serangan Cross Site Request Forgery (CSRF), yaitu serangan di mana penyerang memanfaatkan sesi login user untuk mengirim request tanpa sepengetahuan user. Jika tidak menambahkan csrf_token, form menjadi lebih beresiko terhadap serangan ini sehingga attacker bisa melakukan kejahatan seperti submit data atau perubahan data tanpa izin user.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
jawaban : 
-pertama saya membuat main.html yang menampilkan list product, lalu dengan tombol add product yang akan mendirect ke page create_product dan tombol detail untuk melihat detail product.
-setelah itu saya membuat 4 fungsi show xml,json,xml by id, json by id. 
-lalu saya menambahkan routing keempat URL dari views tadi ke urls.py di main
-terakhir saya membuat serta memodifikasi page detail yang menampilkan semua atribut sesuai dengan yang ada di model saya.

6. Feedback untuk asdos di tutorial 2:
sangat baik saat saya mengalami error dalam mengerjakan tutorial.

#### TUGAS 4 ####

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
jawaban: form bawaan dari django yang berfungsi menghandle proses login user. form ini secara otomatis menyediakakn field username dan password sekaligus melakukan validasi/autentikasi terhadap kredensial user

kelebihannya, tentu form ini sudah terintegrasi dengan sistem autentikasi django, sehingga memudahkan validasi login secara otomatis dan aman. kekurangannya, form ini kurang fleksibel dan hanya mendukung autentikasi berdasarkan username dan password tanpa autentikasi kompleks seperti email, OTP, dll.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
jawaban:
-autentikasi: Django menyediakan sistem login/logout, session, dan model User. Proses login menggunakan form seperti AuthenticationForm.
-otorisasi: Django menggunakan permission dan group. Setiap user bisa punya hak akses tertentu (misal: is_staff, is_superuser, atau permission custom). Otorisasi dicek dengan decorator seperti @login_required atau @permission_required, serta pengecekan di view/template.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
jawaban: 
kelebihan dari session dapat menyimpan data di server da;am jumlah yang lebih besar sehingga lebih aman dan sulit dimanipulasi. kalau cookies, dapat menyimpan data di browser user sehingga tidak membebani server dan mudah diakses dari client-side ,

kekurangan session, dapat membebani server karena menyimpan data dari setiap user dan membutuhkan mekanisme identifikasi. Kekurangan cookies, kapasitas penyimpanan yang terbatas dan rentan terhadap manipulasi dan pencurian data

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada resiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
jawaban: 
penggunaan cookies tidak sepenuhnya aman secara default. ada beberapa resiko potensial seperti pencurian data (cookie theft), manipulasi data, dan serangan CSRF. cookies bisa diakses dan dimodifikasi oleh user, serta dikirim pada setiap request.

django sendiri menangani resiko ini dengan:

Menyediakan opsi HttpOnly agar cookie tidak bisa diakses JavaScript.
Opsi Secure agar cookie hanya dikirim lewat HTTPS.
Proteksi CSRF dengan token khusus.
Session data disimpan di server, hanya sessionid yang disimpan di cookie.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
jawaban:
-import usercreationform, authenticationform, login, authenticate, logout, HttpResponseRedirect, reverse, dan datetime di views.py
-menambahkan fungsi register, login, dan logout di views.py
-mengimport semua fungsi tadi di urls dan menambahkannya di path url
-menambahkan button logout di page main 
-melakukan restriksi dengan menambahkan @login_required(login_url='/login') di atas show main dan show product
-memodifikasi fungsi login dan logout agar mengintegrasikan cookies
-menambahkan last login di show main

##### TUGAS 5 ####

1. 
Prioritas CSS ditentukan berdasarkan spesifisitas. Urutannya dari yang paling rendah ke yang paling tinggi adalah:
-Selector elemen atau tag, misalnya div atau p
-Selector class atau atribut, misalnya .card atau [type=text]
-Selector id, misalnya #header
-Selector inline style yang ditulis langsung pada elemen HTML, misalnya style="color:red"

2. 
Responsive design penting agar tampilan web tetap nyaman dilihat dan digunakan di berbagai ukuran layar, baik di desktop, tablet, maupun smartphone. Tanpa responsive design, tampilan web bisa pecah atau susah diakses di perangkat tertentu.
Contoh aplikasi yang sudah responsive adalah Tokopedia, Instagram web, atau Google. Semua elemen menyesuaikan ukuran layar.
Contoh aplikasi yang belum responsive misalnya beberapa website lama universitas atau portal berita lama. Saat dibuka di smartphone, tombol dan teks menjadi terlalu kecil atau layout pecah karena desainnya hanya untuk desktop

3. 
Margin adalah jarak antara elemen dengan elemen lain di luar elemen tersebut.
Sedangkan border adalah garis di tepi elemen yang membatasi area konten dan padding.
Lalu, padding adalah jarak antara konten di dalam elemen dengan border.
contoh mengimplementasikan ketiganya:

<head>
  <title>Contoh Margin, Border, dan Padding</title>
  <style>
    .box {
      width: 200px;          /* Lebar box */
      height: 100px;         /* Tinggi box */
      background-color: lightblue;  /* Warna latar */
      
      /* Padding: jarak antara konten dengan border */
      padding: 20px;
      
      /* Border: garis tepi box */
      border: 5px solid blue;
      
      /* Margin: jarak box dengan elemen lain */
      margin: 30px;
    


4. 
Flex box adalah sistem layout satu dimensi, bisa horizontal atau vertical. Kegunaannya untuk menyusun elemen agar fleksibel, mudah diatur jarak, posisi, dan ukuran relatif terhadap elemen lain. Contoh property: display flex, justify content, align items

Grid layout adalah sistem layout dua dimensi, bisa baris dan kolom. Kegunaannya untuk membuat tata letak yang kompleks dengan baris dan kolom tetap, misalnya layout halaman dashboard atau galeri gambar. Contoh property: display grid, grid template columns, grid gap

5. 
-Buat fungsi untuk menghapus product dengan mengambil id product dan menghapus dari database 
-Buat fungsi untuk mengedit product dengan menampilkan form berisi data product yang sudah ada, lalu simpan perubahan
-Buka template HTML yang sudah ada, kustomisasi menggunakan CSS Tailwind untuk halaman login, register, tambah product, edit product, dan detail product, tambahkan style yang menarik misalnya warna, shadow, padding, radius pada input dan button
-buat pengecekan untuk halaman filter daftar product, cek apakah ada product. Jika tidak ada, tampilkan gambar dan pesan "belum ada product".Jika ada, buat card untuk setiap product dengan informasi product, lalu buat dua button untuk edit dan hapus
-Buat navigation bar di bagian atas halaman, pastikan responsive dengan menambahkan kelas untuk mobile dan desktop jika pakai CSS framework
