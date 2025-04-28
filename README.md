# Simple Flask App for Form Handling and Basic API

This project is a beginner-friendly **Flask application** built for learning purposes.  
It demonstrates key concepts such as routing, form handling, redirects, basic API creation, and testing using **Postman**.

---

## Features

- Simple web pages using Flask routes (`/`, `/index`)
- Form submission to calculate average marks and redirect based on result (pass/fail)
- Basic API endpoint (`/api`) that accepts JSON data and returns the sum
- Testing the API with **Postman**
- Use of `render_template`, `redirect`, and `url_for`
- Lightweight and easy-to-understand structure

---

## Project Structure

```
/project-folder
│
├── app.py              # Main Flask application
├── templates/          
│   ├── form.html       # HTML form for submitting marks
│   └── test.json       # Sample JSON file for API testing
```

---

## How to Run

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Start the Flask server:
   ```bash
   python app.py
   ```

3. Open your browser and visit:
   - `http://127.0.0.1:5000/` → Welcome page
   - `http://127.0.0.1:5000/index` → Index page
   - `http://127.0.0.1:5000/form` → Form page to submit marks

4. Test the API (`/api`) using **Postman**:
   - Set method to `POST`
   - URL: `http://127.0.0.1:5000/api`
   - In **Body → raw → JSON** format, send:
     ```json
     {
       "a": 10,
       "b": 20
     }
     ```

---

## Example API Response

**Request (Body):**
```json
{
  "a": 10,
  "b": 20
}
```
**Response:**
```json
30.0
```

---

## Purpose

This project was built as part of my learning journey to practice and understand Flask fundamentals, including routing, form handling, API creation, and API testing with Postman.

---

## Notes

- `form.html` → Displays a simple form for entering subject marks.
- `test.json` → Sample JSON file you can use to quickly test the API in Postman.
- API endpoints return JSON responses, ideal for real-world integrations.

---

# Final Tip

This mini-project can be expanded later by:
- Adding **form validations**
- Storing results in a **database** (like MongoDB or SQLite)
- Creating a proper **frontend template** (Bootstrap/HTML5)