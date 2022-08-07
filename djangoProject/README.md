# Django-mayBeMyGameChanger
 I am starting this repo with high hope
### Django Project and Application
প্রথমে আমরা একটি জ্যাঙ্গু প্রোজেক্ট তৈরি করে নিব <br>
**জ্যাঙ্গু প্রোজেক্ট তৈরি করতে নিচের কমান্ডটি টার্মিনালে রান করি:**

    django-admin startproject djangoProject

তাহলে আমরা djangoProject নামে একটি প্রোজেক্ট তৈরি করলাম <br><br>


জ্যাঙ্গু প্রোজেক্টে, আমরা নির্দিষ্ট কাজের জন্য আলাদা আলাদা আপ্লিকেশন তৈরি করব যাতে করে প্রোজেক্ট স্টাকচার সুন্দর ও ঠিক থাকে।<br>
**জ্যাঙ্গু আপ্লিকেশন তৈরি করতে নিচের কমান্ডটি টার্মিনালে রান করি:**

    python manage.py startapp first_app

তাহলে আমরা first_app নামে একটি আপ্লিকেশন তৈরি করলাম <br><br>

### Django View and URL
ওয়েব ব্রাউজারে আমরা যা দেখি তাই ভিউ। প্রতিটা পেইজ এক একটা ভিউ। 
ব্রাউজারে যে url টাইপ করি তা জ্যাঙ্গু urls.py এর মধ্য ম্যাচ করলে সেখান থেকে একটি view কল হয়। প্রতিটা view এ বলা থাকে ব্রাউজারে কি দেখানো হবে।
এর পর view থেকে ব্রাউজারে কি কি দেখান হবে তা রেসপন্স আকারে ব্রাউজারে পাঠানো হয়।<br>

প্রত্যেকটি অ্যাপ এর আন্ডারে views.py ফাইল থাকে। views.py ফাইলের মধ্যে প্রতিটা ফাংশনই এক একটা view। 

আসুন একটি view লিখে ফেলি।

    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello World")

একটি সহজ view লিখলাম যেখানে ব্রাউজারে "Hello World" রেসপন্স পাঠাবে। 
তো এই view টি কখন কল হবে? একটা নির্দিষ্ট url টাইপ করলেই, তাই না? এই view এর সাথে url ম্যাপ করতে urls.py ফাইলে url এড করে দিব।

    from django.contrib import admin
    from django.urls import path
    from first_app import views
    
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("index/", views.index, name='index'),
    ]

আমরা ব্রাউজারে ওয়েবসাইট/index লিখলেই "Hello World" দেখতে পারব। আমি যেহেতু লোকাল সার্ভারে কাজ করছি তাই আমি http://127.0.0.1:8000/index/ টাইপ করলে "Hello World" দেখব। 
![](/Users/forhad/Desktop/Screenshot 2022-08-07 at 10.29.48 AM.png 'ব্রাউজারে "Hello World" দেখা')