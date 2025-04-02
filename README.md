# LLServer

Данный проект предоставляет фреймворк для управления и взаимодействия с различными AI моделями с использованием унифицированного сервера (`uniserver`) и обработчика для упрощенной коммуникации. Модели контейнеризированы и могут быть запущены, остановлены и опрошены для выполнения задач и получения результатов.

## Основные возможности

- **Унифицированный сервер (`uniserver`)**: Сервер на основе FastAPI, управляющий жизненным циклом контейнеров AI моделей.
- **Обработчик (Handler)**: Python-класс для взаимодействия с `uniserver` для управления моделями и задачами.
- **Управление моделями**: Запуск, остановка и мониторинг моделей.
- **Управление задачами**: Отправка задач моделям и получение результатов.

## Требования

- Docker
- Python 3.10+
- FastAPI
- Uvicorn

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/AmpiroMax/llserver.git -b v0.1.0
   cd llserver
   ```

2. Установите необходимые Python-пакеты:
   ```bash
   pip install -r dev_requirements.txt
   ```

3. Убедитесь, что Docker установлен и запущен на вашем компьютере.

## Использование

### Сборка модели

Перед запуском модели необходимо собрать Docker-образ:

```bash
./build.sh --model <имя_модели>
```

Доступные модели: `api_model`, `ecot`, `cogact`.

Пример:
```bash
./build.sh --model api_model
```

### Запуск Uniserver

Для запуска `uniserver`, выполните следующую команду:

```bash
./run_uniserver.sh
```

### Использование обработчика (Handler)

Класс `UniserverHandler` предоставляет интерфейс для взаимодействия с `uniserver`. Ниже приведены примеры его использования:

#### Инициализация обработчика

```python
from llserver.utils.handler import UniserverHandler

# Инициализация обработчика с портом, на котором запущен uniserver
handler = UniserverHandler(port=8000)
```

#### Получение списка запущенных моделей

```python
running_models = handler.get_running_models()
print(running_models)
```

#### Запуск модели

```python
response = handler.start_model("api_model")
print(response)
```

#### Остановка модели

```python
response = handler.stop_model("a2a59714-f407-4e40-a460-688793a3562f")
print(response)
```

#### Отправка задачи

```python
task_id = handler.put_task(
    model_id="a2a59714-f407-4e40-a460-688793a3562f",
    image_paths=["/путь/к/изображению1.jpg", "/путь/к/изображению2.jpg"],
    prompt="Опишите сцену на изображениях."
)
print(task_id)
```

#### Получение результата задачи

```python
result = handler.get_task_result(
    model_id="a2a59714-f407-4e40-a460-688793a3562f",
    task_id="id-вашей-задачи"
)
print(result)
```

## Конфигурация

- **Dockerfile**: Каждая модель имеет свой Dockerfile для контейнеризации.
- **Requirements**: Каждая модель имеет файл `requirements.txt`, указывающий её зависимости.

