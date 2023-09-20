# Django REST APIs - Project Title

## Introduction

Hello, I'm Muhammad Shahbaz, a passionate Data Scientist and Full Stack Developer. Welcome to my Django REST API project! This project was created for both fun and demonstration of my skills.

In this project, I have developed a set of RESTful APIs, which include user authentication (signup and login), and a test endpoint (`test_token`). These APIs can be used as a foundation for various web applications, mobile apps, or any other software that requires secure user authentication.

## Features

- **User Authentication**:

  - `POST /api/signup`: Register new users.
  - `POST /api/login`: Authenticate and obtain an access token.

- **Test API Endpoint**:
  - `GET /api/test_token`: A sample protected endpoint to test user authentication.

## Getting Started

To run this project locally, follow these steps:

1. Create a virtual environment (venv or conda env):

   ```bash
   # Create a virtual environment (venv)
   python -m venv venv

   # Activate the virtual environment
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate  # Windows
   ```

2. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

After setting up the project locally, you can use the following endpoints:

- **Signup**: `POST /api/signup`

  Create a new user account by providing necessary user details.

- **Login**: `POST /api/login`

  Authenticate and obtain an access token by providing valid credentials.

- **Test Token**: `GET /api/test_token`

  Access a sample protected endpoint to verify user authentication.

## Contributions

Contributions and feedback are welcome! If you have suggestions, found issues, or want to improve this project, please feel free to open an issue or submit a pull request.

## Contact

**Muhammad Shahbaz**

- Email: [YourEmail@example.com](mailto:shahbiqureshi33@gmail.com)
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/mshahbazq)
- GitHub: [Your GitHub Profile](https://github.com/mshahbazq)

## License

This project is licensed under the MIT License.

---

Thank you for checking out my Django REST API project. I hope you find it helpful and inspiring for your own projects. If you have any questions or need assistance, please don't hesitate to reach out.
