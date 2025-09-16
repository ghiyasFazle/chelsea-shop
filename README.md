
Link project : https://ghiyas-fazle-chelseashop.pbp.cs.ui.ac.id/

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
