# tflite-androidapp-atiksiniflandirma1
WASTE CLASSIFICATION ANDROID APP by using TENSORFLOW LITE MODEL MAKER&amp;ANDROID STUDIO
TENSORFLOW LITE MODEL MAKER&ANDROID STUDIO ile ATIK SINIFLANDIRMA1 UYGULAMASI

Bu AtikSiniflandirma1 Android Uygulaması yapılırken izlenen yol şu şekildedir :
# 1.  Tensorflow Lite Model Maker ile Model oluşturma ve. tflite formatında aktarma
      atiksiniflandirma1_tflite.py dosyası
      num_label: 6, labels: cardboard_mavi, glass_yesil, metal_gri, paper_mavi, plastic_sari, trash_cop
# 2.	Android Studio ile “Create a New Project” 
      Configure Your Project alanında Uygulama adi AtikSiniflandirma1 olarak ele alındı
# 3.	build.gradle dosyasını güncelleme (.app uzantılı olan)
      dosya içinde en alta aşağıdaki kütüphane referansı eklenir : 
      implementation 'com.google.mlkit:image-labeling-custom:16.3.1'
      Ayrıca aynı dosyada Android sekmesinde aşağıdaki ayar eklenir ki .tflite formatlı model bloke olmasın:
      aaptOptions{
      noCompress "tflite"
      }
# 4.	res/layout/activity_main.xml dosyasını güncelleme (kullanıcı arayüzü oluşturma)
# 5.	src/main/assets dosyası güncelleme
      model.tflite dosyası (deneme.tflite dosyası olarak güncellendi) ve test yapılmak istenen görüntü eklenir (glass9.jpg)
# 6.	src/main/java/com.google.devrel.AtikSiniflandirma1/MainActivity.kt güncelleme
      bu örnekte kotlin kullanılmaktadır.
# 7.	Emulator veya Andorid cihaz ile test etme
