import streamlit as st
import streamlit.components.v1 as components
import time

with st.spinner('Wait for it...'):
    time.sleep(5)

with st.container():
    st.title("CYBER SECURITY ⏳")

    # Cyber Security
    st.warning("""
        Dalam tujuan memastikan keamanan informasi, keamanan siber mengacu secara khusus pada penyediaan perangkat keras dan perangkat lunak pemrosesan yang aman.
        Tugas keamanan informasi dan keamanan siber dapat diklasifikasikan 
        sebagai lima fungsi, mengikuti kerangka kerja yang dikembangkan oleh
        National Institute of Standards and Technology (NIST).
    """)
    expander = st.expander("Identify ")
    expander.markdown("""
        Mengembangkan kebijakan dan kemampuan keamanan. Mengevaluasi risiko, ancaman, dan kerentanan dan merekomendasikan kontrol keamanan untuk menguranginya.
        Protect: pengadaan/pengembangan, pemasangan, pengoperasian, dan penonaktifan aset perangkat keras dan perangkat lunak TI dengan keamanan sebagai persyaratan yang melekat pada setiap tahap siklus hidup operasi ini
    """)

    expander = st.expander("Detect")
    expander.markdown("""
        Melakukan pemantauan proaktif yang berkelanjutan untuk memastikan bahwa kontrol efektif dan mampu melindungi dari jenis ancaman baru.
    """)

    expander = st.expander("Respond")
    expander.markdown("""
        Mengidentifikasi, menganalisis, menahan, dan memberantas ancaman terhadap sistem dan keamanan data
    """)

    expander = st.expander("Recover")
    expander.markdown("""
        Menerapkan ketahanan cybersecurity untuk memulihkan sistem dan data jika kontrol lain tidak dapat mencegah serangan.
    """)

st.image("1.png")
# Information Security Competencies
st.title("INFORMATION SECURITY COMPETENCIES")

st.markdown("""
    Profesional TI yang bekerja dalam peran dengan tanggung jawab keamanan harus kompeten dalam berbagai disiplin ilmu,
    mulai dari desain jaringan dan aplikasi hingga pengadaan dan sumber daya manusia (SDM)
    . Kegiatan berikut mungkin khas dari peran tersebut:
""")

st.markdown("""
    - Berpartisipasi dalam penilaian risiko dan pengujian sistem keamanan dan membuat rekomendasi.
    - Tentukan, sumber, instal, dan konfigurasikan perangkat dan perangkat lunak yang aman.
    - Mengatur dan memelihara kontrol akses dokumen dan profil hak pengguna.
    - Pantau log audit, tinjau hak pengguna, dan kontrol akses dokumen.
    - Kelola respons dan pelaporan insiden terkait keamanan.
    - Membuat dan menguji kesinambungan bisnis dan rencana serta prosedur pemulihan bencana.
    - Berpartisipasi dalam program pelatihan dan pendidikan keamanan.
""")

# VULNERABILITY, THREAT, AND RISK
st.title("VULNERABILITY, THREAT, AND RISK")
st.markdown("""
    Mengklasifikasikan dan mengevaluasi kemampuan jenis aktor ancaman memungkinkan kita untuk menilai dan mengurangi risiko secara lebih efektif. Memahami metode yang digunakan pelaku ancaman untuk menyusup ke jaringan dan sistem sangat penting bagi kita untuk menilai permukaan serangan jaringan Anda dan menerapkan kontrol untuk memblokir vektor serangan
""")
st.markdown("""
    - Vulnerability adalah kelemahan yang dapat dipicu secara tidak sengaja atau dieksploitasi dengan sengaja untuk menyebabkan pelanggaran keamanan.
    - Threat adalah potensi seseorang atau sesuatu untuk mengeksploitasi kerentanan dan melanggar keamanan.
    - Risk adalah kemungkinan dan dampak (atau konsekuensi) dari aktor ancaman yang mengeksploitasi kerentanan.
""")
st.image("2.png")
# HACKERS, SCRIPT KIDDIES, AND HACKTIVISTS
st.title("HACKERS, SCRIPT KIDDIES, AND HACKTIVISTS")
st.markdown("""
    Hackers : menggambarkan seorang individu yang memiliki keterampilan untuk mendapatkan akses ke sistem komputer melalui cara yang tidak sah atau tidak disetujui.
    Script Kiddies : seseorang yang menggunakan alat peretas tanpa harus memahami cara kerjanya atau memiliki kemampuan untuk membuat serangan baru.
    Hacker Teams and Hacktivists : mencoba untuk mendapatkan dan melepaskan informasi rahasia ke domain publik, melakukan serangan penolakan layanan (DoS), atau merusak situs web.
""")
# PERFORMING SECURITY ASSESSMENT
st.title("PERFORMING SECURITY ASSESSMENT")
st.markdown("""
    Penilaian keamanan mengacu pada proses dan alat yang mengevaluasi permukaan serangan. Dengan pengetahuan tentang taktik dan kemampuan musuh, kita dapat menilai apakah titik di permukaan serangan berpotensi menjadi vektor serangan yang rentan. Keluarannya adalah rekomendasi untuk menyebarkan, meningkatkan, atau mengkonfigurasi ulang kontrol keamanan untuk mengurangi risiko kerentanan yang dapat dieksploitasi oleh aktor ancaman.
""")

# IDENTIFYING SOCIAL ENGINEERING AND MALWARE
st.title("IDENTIFYING SOCIAL ENGINEERING AND MALWARE")
st.markdown("""
    Tidaklah cukup bagi penilaian keamanan untuk hanya berfokus pada kerentanan perangkat lunak dan kesalahan konfigurasi. Pelaku ancaman bisa menggunakan teknik rekayasa sosial untuk memperoleh informasi, mendapatkan akses ke lokasi, dan untuk mengelabui pengguna agar menjalankan kode yang berbahaya.
""")

# SOCIAL ENGINEERING
st.title("SOCIAL ENGINEERING")
st.markdown("""
    Musuh dapat menggunakan beragam teknik untuk mengkompromikan sistem keamanan. Prasyarat dari banyak jenis serangan adalah untuk mendapatkan informasi tentang jaringan dan sistem keamanan. Rekayasa sosial mengacu pada cara baik memperoleh informasi dari seseorang atau membuat mereka melakukan beberapa tindakan untuk aktor ancaman. Itu juga bisa disebut sebagai "meretas manusia." Rekayasa sosial dapat digunakan untuk mengumpulkan intelijen sebagai pengintaian dalam persiapan untuk intrusi, atau mungkin digunakan untuk mempengaruhi intrusi yang sebenarnya. Skenario intrusi rekayasa sosial yang khas meliputi:
""")
st.markdown("""
- Penyerang membuat file yang dapat dieksekusi yang meminta pengguna jaringan untuk memasukkan kata sandi mereka, dan kemudian merekam apa pun yang dimasukkan pengguna. Penyerang kemudian mengirim email file yang dapat dieksekusi ke pengguna dengan cerita bahwa pengguna harus mengklik dua kali file tersebut dan masuk ke jaringan lagi untuk menyelesaikan beberapa masalah masuk yang dialami organisasi pagi itu. Setelah pengguna mematuhi, penyerang sekarang memiliki akses ke kredensial jaringan mereka.
- Seorang penyerang menghubungi meja bantuan berpura-pura menjadi perwakilan penjualan jarak jauh yang membutuhkan bantuan untuk mengatur akses jarak jauh. Melalui serangkaian panggilan telepon, penyerang memperoleh nama/alamat server akses jarak jauh dan kredensial login, selain nomor telepon untuk akses jarak jauh dan untuk mengakses telepon pribadi dan sistem pesan suara organisasi.
- Seorang penyerang memicu alarm kebakaran dan kemudian menyelinap ke dalam gedung selama kebingungan dan memasang perangkat pemantauan ke port jaringan.
""")

# SOCIAL ENGINEERING PRINCIPLES
st.title("SOCIAL ENGINEERING PRINCIPLES")
st.markdown("""
    Rekayasa sosial adalah salah satu teknik jahat yang paling umum dan sukses. Karena mengeksploitasi kepercayaan dasar manusia, rekayasa sosial telah terbukti menjadi cara yang sangat efektif untuk memanipulasi orang agar melakukan tindakan yang mungkin tidak mereka lakukan. Agar persuasif, serangan rekayasa sosial bergantung pada satu atau beberapa prinsip berikut.
""")

# HASHING ALGORITHMS
st.title("Hashing Algorithms")
st.markdown("""
    Hashing adalah jenis operasi kriptografi yang paling sederhana. Sebuah algoritma hashing kriptografi menghasilkan string panjang tetap dari input plaintext yang bisa panjang apapun. Outputnya dapat disebut sebagai checksum, message digest, atau hash. Fungsi ini dirancang sedemikian rupa sehingga tidak mungkin untuk memulihkan data plaintext dari intisari (satu arah) dan agar input yang berbeda tidak mungkin menghasilkan output yang sama (tabrakan).
""")
st.markdown("""
    Algoritma hashing digunakan untuk membuktikan integritas. Misalnya, Bob dan Alice dapat membandingkan nilai yang digunakan untuk kata sandi dengan cara berikut:
""")
st.markdown("""
    1. Bob sudah memiliki intisari yang dihitung dari kata sandi plaintext Alice. Bob tidak dapat memulihkan nilai kata sandi plaintext dari hash.
    2. Ketika Alice perlu mengautentikasi ke Bob, dia mengetikkan kata sandinya, mengubahnya menjadi hash, dan mengirimkan intisari ke Bob.
    3. Bob membandingkan intisari Alice dengan nilai hash yang ada di filenya. Jika mereka cocok, dia dapat memastikan bahwa Alice mengetikkan kata sandi yang sama.
""")
st.markdown("""
Selain membandingkan nilai sandi, hash file dapat digunakan untuk memverifikasi integritas file tersebut setelah transfer.
""")
st.markdown("""
    1. Alice menjalankan fungsi hash pada file setup.exe untuk produknya. Dia menerbitkan intisari ke situs webnya dengan tautan unduhan untuk file tersebut.
    2. Bob mengunduh file setup.exe dan membuat salinan intisari.
    3. Bob menjalankan fungsi hash yang sama pada file setup.exe yang diunduh dan membandingkannya dengan nilai referensi yang diterbitkan oleh Alice. Jika cocok dengan nilai yang dipublikasikan di situs web, integritas file dapat diasumsikan.
    4. Pertimbangkan bahwa Mallory mungkin dapat mengganti file unduhan dengan file berbahaya. Mallory tidak dapat mengubah hash referensi.
    5. Kali ini, Bob menghitung hash tetapi tidak cocok, membuatnya curiga bahwa file tersebut telah dirusak.
""")

st.image("3.png")

st.markdown("""
    Mengonfirmasi unduhan file menggunakan hash kriptografis. (Gambar © 123RF.com.)
    Ada dua implementasi algoritma hash yang populer:
""")
st.markdown("""
    Secure Hash Algorithm (SHA)—dianggap sebagai algoritma terkuat. Ada varian yang menghasilkan keluaran dengan ukuran berbeda, dengan intisari yang lebih panjang dianggap lebih aman. Varian paling populer adalah SHA-256, yang menghasilkan intisari 256-bit.
    Message Digest Algorithm #5 (MD5)—menghasilkan intisari 128-bit. MD5 tidak dianggap cukup aman untuk digunakan seperti SHA-256, tetapi mungkin diperlukan untuk kompatibilitas antara produk keamanan.
""")
st.image("4.png")

# ASYMMETRIC ENCRYPTION
st.title("ASYMMETRIC ENCRYPTION")
st.markdown("""
    Dalam cipher enkripsi simetris, kunci rahasia yang sama digunakan untuk melakukan operasi enkripsi dan dekripsi. Dengan sandi asimetris, operasi dilakukan oleh dua kunci publik dan pribadi yang berbeda tetapi terkait dalam pasangan kunci.
""")
st.markdown("""
    Setiap kunci mampu membalikkan operasi pasangannya. Misalnya, jika kunci publik digunakan untuk mengenkripsi pesan, hanya kunci pribadi berpasangan yang dapat mendekripsi teks sandi yang dihasilkan. Kunci publik tidak dapat digunakan untuk mendekripsi ciphertext, meskipun digunakan untuk mengenkripsinya.
""")
st.markdown("""
    Kunci-kunci tersebut dihubungkan sedemikian rupa sehingga tidak mungkin untuk menurunkan satu dari yang lain. Ini berarti bahwa pemegang kunci dapat mendistribusikan kunci publik kepada siapa pun yang dia inginkan untuk menerima pesan aman. Tidak ada orang lain yang dapat menggunakan kunci publik untuk mendekripsi pesan; hanya kunci pribadi tertaut yang dapat melakukannya.
""")
st.markdown("""
    1. Bob menghasilkan pasangan kunci dan merahasiakan kunci pribadi.
    2. Bob menerbitkan kunci publik. Alice ingin mengirimi Bob pesan rahasia, jadi dia mengambil salinan kunci publik Bob.
    3. Alice menggunakan kunci publik Bob untuk mengenkripsi pesan.
    4. Alice mengirimkan ciphertext ke Bob.
    5. Bob menerima pesan dan dapat mendekripsinya menggunakan kunci pribadinya.
    6. Jika Mallory telah mengintip, dia dapat mencegat pesan dan kunci publik.
    7. Namun, Mallory tidak dapat menggunakan kunci publik untuk mendekripsi pesan, sehingga sistem tetap aman.
""")
st.image("5.png")
st.markdown("""
    Enkripsi asimetris dapat digunakan untuk membuktikan identitas. Pemegang kunci pribadi tidak dapat ditiru oleh orang lain. Kelemahan dari enkripsi asimetris adalah bahwa hal itu melibatkan overhead komputasi yang substansial dibandingkan dengan enkripsi simetris. Pesan tidak boleh lebih besar dari ukuran kunci. Di mana sejumlah besar data sedang dienkripsi pada disk atau diangkut melalui jaringan, enkripsi asimetris tidak efisien.
""")
st.markdown("""
    Akibatnya, enkripsi asimetris banyak digunakan untuk otentikasi dan non-penolakan dan untuk kesepakatan dan pertukaran kunci. Perjanjian/pertukaran kunci mengacu pada penetapan kunci simetris rahasia yang akan digunakan untuk enkripsi massal tanpa ada orang lain yang menemukannya.
""")