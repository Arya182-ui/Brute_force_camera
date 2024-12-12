import cv2
import time
import firebase_admin
from firebase_admin import credentials, storage

firebase_config = {
"your data base key"
}

cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    'storageBucket': "your database url"
})

def camera():
    def open_camera():
        max_attempts = 10
        cap = None
        for index in range(max_attempts):
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                return cap
            cap.release()
        return None

    def upload_image(image_data, photo_counter):
        bucket = storage.bucket()
        blob = bucket.blob(f'captured_photo_{photo_counter}.jpg')
        blob.upload_from_string(image_data, content_type='image/jpeg')

    def run_camera(cap):
        while True:
            for photo_counter in range(1, 11):  
                ret, frame = cap.read()
                if not ret:
                    break

                is_success, buffer = cv2.imencode('.jpg', frame)
                if is_success:
                    upload_image(buffer.tobytes(), photo_counter)
                    time.sleep(1) 

            time.sleep(120) 

    cap = open_camera()
    if cap is not None:
        run_camera(cap)

    if cap:
        cap.release()
    cv2.destroyAllWindows()
    pass

if __name__ == "__main__":
    camera()
