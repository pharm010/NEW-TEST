import os
from datetime import datetime
import flask

# إنشاء تطبيق الويب
app = flask.Flask(__name__)


# تحديد المسار (الرابط) الخاص بتحميل الصورة
@app.route('/download')
def download_image():
    # 1. الحصول على عنوان IP الخاص بالمستخدم
    ip = flask.request.remote_addr
    
    # 2. الحصول على الوقت الحالي
    time = datetime.now()

    # 3. تسجيل عنوان IP والوقت في ملف نصي
    # استخدمنا "a" لإضافة سطر جديد دون مسح البيانات السابقة
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"IP: {ip} | Time: {time}\n")

    # 4. تحديد مسار الصورة التي سيتم تحميلها
    # التطبيق سيبحث عن مجلد اسمه 'images' وبداخله صورة اسمها 'product.jpg'
    image_path = os.path.join("images", "product.jpg")

    # 5. إرسال الصورة للمستخدم كملف قابل للتحميل
    return flask.send_file(image_path, as_attachment=True)

# أمر تشغيل التطبيق
if __name__ == "__main__":
    # نحدد المنفذ (Port) 5000 كافتراضي
    port = int(os.environ.get("PORT", 8080))
    app.run(host="127.0.0.1", port=port)
    
