import requests
import time

url = "https://facebookbot.promotion2022.com/api/promotion/post/like"
interval_seconds = 1  # تحديد عدد الثواني بين كل ركوست

while True:
    try:
        response = requests.post(url)
        # هنا يمكنك التعامل مع الاستجابة response
        print(f"تم إرسال الركوست بنجاح. الاستجابة: {response.text}")
    except Exception as e:
        print(f"حدث خطأ: {e}")

    time.sleep(interval_seconds)
