import streamlit as st
import streamlit.components.v1 as components
import time
import streamlit.components.v1 as components

# with st.spinner('Wait for it...'):
#     time.sleep(5)


st.title("CYBER SECURITY ⏳")
components.html("""
<!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    
    <p>
        <button class="btn btn-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapseWidthExample" aria-expanded="false" aria-controls="collapseWidthExample">
            Hashing Algorithms
        </button>
    </p>
    <div style="min-height: 100%;">
        <div class="collapse collapse-horizontal" id="collapseWidthExample">
            <div class="card card-body" style="width: 100%">
                adalah jenis operasi kriptografi yang paling sederhana. Sebuah algoritma hashing kriptografi menghasilkan string panjang tetap dari input plaintext yang bisa panjang apapun. Outputnya dapat disebut sebagai checksum, message digest, atau hash.
            </div>
        </div>
    </div>
""")
components.html("""
<!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    
    <p class="d-flex justify-content-end">
        </button>
        <button class="btn btn-success" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample2" aria-expanded="false" aria-controls="multiCollapseExample2">
            Algoritma Hashing
        </button>
    </p>
    <div style="min-height: 100%;">
        <div class="collapse multi-collapse" id="multiCollapseExample2">
            <div class="card card-body">
                Algoritma hashing digunakan untuk membuktikan integritas. Fungsi ini dirancang sedemikian rupa sehingga tidak mungkin untuk memulihkan data plaintext dari intisari (satu arah) dan agar input yang berbeda tidak mungkin menghasilkan output yang sama (tabrakan).
            </div>
        </div>
    </div>
""")

components.html("""
    <div></div>
""")
st.markdown("""
    Misalnya, Bob dan Alice dapat membandingkan nilai yang digunakan untuk kata sandi dengan cara berikut:
""")

st.warning("""
    1. Bob sudah memiliki intisari yang dihitung dari kata sandi plaintext Alice. Bob tidak dapat memulihkan nilai kata sandi plaintext dari hash.
    2. Ketika Alice perlu mengautentikasi ke Bob, dia mengetikkan kata sandinya, mengubahnya menjadi hash, dan mengirimkan intisari ke Bob.
    3. Bob membandingkan intisari Alice dengan nilai hash yang ada di filenya. Jika mereka cocok, dia dapat memastikan bahwa Alice mengetikkan kata sandi yang sama.
""")
components.html("""
    <div></div>
""")
st.markdown("""
Selain membandingkan nilai sandi, hash file dapat digunakan untuk memverifikasi integritas file tersebut setelah transfer.
""")
st.success("""
    1. Alice menjalankan fungsi hash pada file setup.exe untuk produknya. Dia menerbitkan intisari ke situs webnya dengan tautan unduhan untuk file tersebut.
    2. Bob mengunduh file setup.exe dan membuat salinan intisari.
    3. Bob menjalankan fungsi hash yang sama pada file setup.exe yang diunduh dan membandingkannya dengan nilai referensi yang diterbitkan oleh Alice. Jika cocok dengan nilai yang dipublikasikan di situs web, integritas file dapat diasumsikan.
    4. Pertimbangkan bahwa Mallory mungkin dapat mengganti file unduhan dengan file berbahaya. Mallory tidak dapat mengubah hash referensi.
    5. Kali ini, Bob menghitung hash tetapi tidak cocok, membuatnya curiga bahwa file tersebut telah dirusak.
""")

st.image("3.png")

st.markdown("""
    Ada dua implementasi algoritma hash yang populer:
""")
st.success("""
    1. Secure Hash Algorithm (SHA)—dianggap sebagai algoritma terkuat. Ada varian yang menghasilkan keluaran dengan ukuran berbeda, dengan intisari yang lebih panjang dianggap lebih aman. Varian paling populer adalah SHA-256, yang menghasilkan intisari 256-bit.
    2. Message Digest Algorithm #5 (MD5)—menghasilkan intisari 128-bit. MD5 tidak dianggap cukup aman untuk digunakan seperti SHA-256, tetapi mungkin diperlukan untuk kompatibilitas antara produk keamanan.
""")
st.image("4.png")