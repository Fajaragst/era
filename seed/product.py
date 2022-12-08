from app.api    import db
from app.api.product.models import Product



def seed_product():
    data = [
    {
        "name" : "TCL 40 inch Smart TV LED - Android 11.0 - FHD - WIFI/HDMI/USB Bluetooth/ Netflix -  (Model : 40A7)",
        "price" : 1899000,
        "description" : "TCL 32A7 SERIES, Best New Android TV. A+ Panel Quality, Feel the Comfortable",
        "quantity" : 300
    },
    {
        "name" : "AOKI Antena 2 tv digital luar dalam indoor outdoor AT3000",
        "price" : 135000,
        "description" : "ANTENA AOKI AT3000 adalah sebuah antena desain khusus untuk menerima sinyal digital terrestrial broadcasting. Dengan menggunakan teknologi dan sirkuit tingkat kebisingan rendah, akan memberikan daya terima sinyal yang baik. Dan desain yang menarik dan model yang bergaya,dimana akan bekerja sangat baik dengan STB (Set Top Box) Digital Anda.",
        "quantity" : 1847
    },
    {
        "name" : "Changhong 32 Inch Newest Android 11 Frameless Smart TV Digital Neflix LED TV-L32G7N-Garansi 5 Resmi FREE BRACKET",
        "price" : 1949000,
        "description" : "Seri Changhong G7N dilengkapi dengan OS Android 11 bersertifikat resmi, menyediakan 5000+ aplikasi yang tersedia untuk digunakan, dan menghadirkan pengalaman hidup yang lebih beragam dan kaya. Sistem suara telah ditingkatkan sepenuhnya, teknisi audio dbx-tv telah menyesuaikan dan mengoptimalkan speaker setiap TV untuk menghadirkan kualitas suara yang optimal. Seri G7N mendukung Wi-Fi dual-band 2.4G/5G, dengan sinyal nirkabel yang lebih stabil, kecepatan transmisi yang lebih cepat untuk memenuhi kebutuhan transmisi nirkabel definisi tinggi dan data besar. HDR10 membuat kualitas gambar lebih hidup, Teknologi Layar Penuh Mutakhir, tampilan ultra lebar yang inovatif membenamkan diri Anda dalam film dan video. Dilengkapi dengan Google Assistant, menggunakan suara untuk mengakses konten hiburan dengan mudah dan mengontrol rumah cerdas.",
        "quantity" : 641
    }
    ]

    for i in data:
        db.session.add(Product(**i))
    
    db.session.commit()