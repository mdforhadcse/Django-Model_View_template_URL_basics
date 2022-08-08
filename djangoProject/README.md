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

![](https://github.com/mdforhadcse/Django-mayBeMyGameChanger/blob/main/readme_images/Screenshot%202022-08-07%20at%2010.29.48%20AM.png "'ব্রাউজারে &quot;Hello World&quot; দেখ'")

<br><br>

এখন আমরা দেখছি শুধু মাত্র মেইন প্রোজেক্ট ফোল্ডারে urls.py ফাইল আছে। অনেক বড় প্রোজেক্ট এ একটা মাত্র urls.py অনেক বড় ম্যাসাকার হয়ে যাবে।
তার জন্য আমরা প্রতিটা অ্যাপ এর আন্ডারে urls.py লিখব।

### Django Models
জ্যাঙ্গু প্রোজেক্টে ডাটাবেইজ সম্পর্কিত সকল কাজ models.py এর মধ্যে করতে হয়। এটি প্রত্যেকটা অ্যাপের মধ্যেই থাকে।
নিচের কোডের মাধ্যমে ডাটাবেইজে Musician ও Album নামে ২ টা টেবিল তৈরি করি। টেবিল তৈরি করার জন্য শুধু ক্লাস তৈরি করব এবং models.Model কে ইনহেরিট করব।

    class Musician(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        instrument = models.CharField(max_length=100)
        
        
    class Album(models.Model):
        artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        release_date = models.DateField()
        numbers_stars = models.IntegerField()


এখানে বলে রাখা ভাল যে কোন টেবিলেই প্রাইমারি কি ডিক্লার করা হয় নি। জ্যাঙ্গুর একটা বিল্ট সুবিধা হল অটো প্রাইমারি কি ডিক্লার হয়ে যায়।

    id = models.AutoField(primary_key=True)

এই কোডটুকু জ্যাঙ্গু নিজেই করে ফেলে।
<br>
ডাটাবেইজ গুলো একচুয়ালি কাজ করানোর জন্য জন্য টার্মিনাল ওপেন করে কমান্ড রান করতে হবে

    python manage.py migrate
অ্যাপকে কানেক্ট করলাম

    python manage.py makemigrations first_app
তারপর আবার 

    python manage.py migrate


model/database এ কোন চেঞ্জ হলে এই তিনটি কোড আবার চালাতে হবে। 

<br>
টেবিল তৈরি হল। এবার ডাটাবেইজে ডাটা এন্ট্রি করার পালা। 
আমরা এডমিন প্যানেল থেকে ডাটা এন্ট্রি করার জন্য first_app এর মধ্যে admin.py এর এর মধ্যে নিচের কোড লেখি

    admin.site.register(Musician)
    admin.site.register(Album)

এবার আমরা অ্যাডমিন প্যানেল তৈরি করার জন্য সুপার ইউজার তৈরি করব টার্মিনাল থেকেঃ

    python manage.py createsuperuser