import requests
import time

# Адрес вашего FastAPI сервера
BASE_URL = "http://127.0.0.1:8000"

def put_task(image_paths, prompt):
    """
    Функция для добавления задачи с несколькими изображениями в очередь.
    """
    url = f"{BASE_URL}/put_task/"
    
    # Превращаем список путей в строку с разделителем, чтобы передать через форму
    data = {
        'image_paths': image_paths,  # Передаём как строку с разделителем
        'prompt': prompt
    }
    
    # Выполняем POST запрос
    response = requests.post(url, data=data)
    
    return response.json()

def get_task_result(task_id):
    """
    Функция для получения результата задачи по её ID.
    """
    url = f"{BASE_URL}/get_task_result/"
    json_data = {"task_id": task_id}
    response = requests.post(url, json=json_data)
    return response.json()