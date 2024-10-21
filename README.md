# LLServer: FastAPI Server for Serving LLaVA Model

**LLServer** is a project designed to serve the LLaVA (Large Language and Vision Assistant) model via a FastAPI server. This server enables the processing of image and text prompts through the LLaVA model to generate detailed responses. The project supports multiple images in a single request and handles tasks asynchronously.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **FastAPI Server**: Lightweight, fast web server for handling requests to the LLaVA model.
- **LLaVA Model Integration**: Uses the LLaVA model for multimodal tasks with image and text prompts.
- **Asynchronous Task Handling**: Queue tasks and check their status or results asynchronously.
- **Support for Multiple Images**: Handle multiple images in a single API call for better image-based reasoning.

## Installation

### Prerequisites
- Python 3.8+
- CUDA-enabled GPU for faster inference (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/llserver.git
   cd llserver
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e ".[train]"
   ```

   This command will install the required dependencies including the LLaVA model and training extras.

4. Install additional dependencies for development:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables (optional, but useful for GPU or server configuration):
   ```bash
   export CUDA_VISIBLE_DEVICES=0  # If using GPU
   ```

## Usage

### Running the Server

To run the FastAPI server, execute the following command:

```bash
uvicorn server:app --reload
```

By default, the server will run at `http://127.0.0.1:8000`.

### Sending Requests

You can send requests to the server with image paths and text prompts using `curl` or a Python script. For example:

#### Python Example:
```python
import requests

image_paths = ["/path/to/image1.jpg", "/path/to/image2.jpg"]
prompt = "Describe these images."

response = requests.post(
    "http://127.0.0.1:8000/put_task/",
    data={"prompt": prompt, "image_paths": ",".join(image_paths)}
)

print(response.json())
```

#### Bash Example:
```bash
curl -X POST "http://127.0.0.1:8000/put_task/" -F "prompt=Describe these images." -F "image_paths=/path/to/image1.jpg,/path/to/image2.jpg"
```

## API Endpoints

### `POST /put_task/`
Submit a new task with a text prompt and a list of image paths.

- **Parameters**:
  - `image_paths` (str): Comma-separated paths to images.
  - `prompt` (str): The text prompt to generate a response based on the images.

- **Response**:
  - A JSON object with the `task_id`.

### `POST /get_task_result/`
Retrieve the result of a specific task by its `task_id`.

- **Parameters**:
  - `task_id` (str): The unique ID of the task.

- **Response**:
  - `status`: The current status of the task (`in queue`, `in progress`, `completed`, or `not found`).
  - `result`: The generated response if the task is completed.

## Configuration

You can configure the server's behavior via environment variables or by adjusting the `server.py` file.

- **CUDA_VISIBLE_DEVICES**: Use this to control which GPU(s) are available for the server to use. For example, setting `CUDA_VISIBLE_DEVICES=0` will make only the first GPU available.

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Open a pull request once your changes are ready.

We welcome improvements, feature suggestions, and bug reports.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Additional Notes

You can modify or extend the `README.md` based on more specific details of your project, such as additional dependencies or instructions for running tests.