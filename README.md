# HNGi13 GetMe API

A simple RESTful API built with FastAPI that returns user profile information and a random cat fact from the Cat Facts API.

## Features

- Returns user profile information (email, name, stack)
- Fetches random cat facts from an external API
- Generates real-time UTC timestamps
- Handles errors gracefully
- Interactive API documentation

## Tech Stack

- Python 3.8+
- FastAPI
- Uvicorn
- Requests library

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/PreciousEzeigbo/HNGi13-getme.git
cd HNGi13-getme
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Testing the API

### Using Your Browser

Visit: `http://localhost:8000/me`

### Using curl

```bash
curl http://localhost:8000/me
```

### Using Interactive Docs

Visit: `http://localhost:8000/docs`

Click on the `/me` endpoint, then "Try it out" and "Execute"

## API Response Format

```json
{
  "status": "success",
  "user": {
    "email": "<your mail>",
    "name": "<your full name>",
    "stack": "<your backend stack>"
  },
  "timestamp": "<curent UTC time in ISO 8601 format>",
  "fact": "<random cat fact from Cat Facts API>"
}
```

## Deployment

### For Railway

1. Push to GitHub
2. Connect repository to Railway
3. Deploy


## Project Structure

```
HNGi13-getme/
├── main.py              # Main application
├── requirements.txt     # Dependencies
├── README.md           # Documentation
```

## Dependencies

```
fastapi==0.115.0
uvicorn[standard]==0.32.0
requests==2.32.3
```

## Error Handling

The API handles external API failures gracefully. If the Cat Facts API is unavailable, a fallback message is returned instead.

## Author

**Precious Ezeigbo**
- Email: preciousezeigbo81@gmail.com
- Stack: Python/FastAPI

## Acknowledgments

- [HNG Internship](https://hng.tech/) for the opportunity
- [Cat Facts API](https://catfact.ninja/) for providing cat facts
- [FastAPI](https://fastapi.tiangolo.com/) for the framework

---

Built for HNG Internship 13