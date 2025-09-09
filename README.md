
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