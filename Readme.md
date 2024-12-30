# 📋 Form Builder API

![Django](https://img.shields.io/badge/Django-3.2-brightgreen)
![Django REST Framework](https://img.shields.io/badge/DRF-3.12-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 📝 Table of Contents

- [🖥️ Description](#️-description)
- [🚀 Features](#-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [📚 Installation](#-installation)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [🔐 Authentication](#-authentication)
- [📦 Usage](#-usage)
- [🎓 Key Learnings](#-key-learnings)
- [🔮 Future Enhancements](#-future-enhancements)


## 🖥️ Description

The **Form Builder API** is a robust backend application built with **Django** and **Django REST Framework (DRF)**. It allows administrators to create customizable forms with various question types (e.g., dropdowns, text fields, checkboxes), collect user responses, and analyze the data through insightful analytics endpoints.

This project serves as the foundation for a comprehensive form management system, enabling seamless form creation, distribution, and data analysis.

## 🚀 Features

- **Form Management:**
  - Create, retrieve, update, and delete forms.
  - Add multiple questions to each form with different types.
  - Define options for questions like dropdowns and checkboxes.

- **Response Handling:**
  - Allow users to submit responses to forms.
  - Support various answer types based on question types.

- **Analytics:**
  - Generate insightful analytics for each form.
  - Analyze response data, including option selection counts and text response insights.

- **Authentication & Permissions:**
  - Implement Token Authentication for secure access.
  - Restrict administrative actions to authorized users.

- **API Documentation:**
  - Interactive documentation using Swagger/OpenAPI.
  - Organized Postman Collections for easy API testing and collaboration.

## 🛠️ Technologies Used

- **Backend:**
  - [Django](https://www.djangoproject.com/) - High-level Python Web framework.
  - [Django REST Framework (DRF)](https://www.django-rest-framework.org/) - Toolkit for building Web APIs.
  - [drf-yasg](https://github.com/axnsan12/drf-yasg) - Automatic Swagger/OpenAPI 2.0 schema generation.
  - [django-cors-headers](https://github.com/adamchainz/django-cors-headers) - Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).
  - [djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt) - JSON Web Token authentication for DRF.

- **Testing:**
  - [pytest](https://pytest.org/) & [pytest-django](https://pytest-django.readthedocs.io/) - Testing frameworks.
  - DRF's built-in `APIClient` for API testing.

- **Version Control:**
  - [Git](https://git-scm.com/) - Version control system.
  - [GitHub](https://github.com/) - Hosting service for Git repositories.

## 📚 Installation

Follow these steps to set up the **Form Builder API** on your local machine.

### Prerequisites

Ensure you have the following installed:

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for version control)
- **Virtual Environment Tool** (`venv` or `virtualenv`)

### Setup Instructions

1. **Clone the Repository**

   git clone https://github.com/Nani2139/morpheus.git
   cd morpheus

2. **Create a Virtual Environment**

   python -m venv venv

3. **Activate the Virtual Environment**

   Windows: venv\Scripts\activate
   macOS/Linux:source venv/bin/activate

4. **Install Dependencies**

   pip install django djangorestframework drf-yasg django-cors-headers djangorestframework-simplejwt


5. **Apply Migrations**
   python manage.py migrate

6. **Create a Superuser**
   python manage.py createsuperuser

7. **Run the Development Server**
   python manage.py runserver

8. **Access the Application**
   *Admin Panel*: http://127.0.0.1:8000/admin/
   *API Endpoints*: http://127.0.0.1:8000/api/
   *Swagger Documentation*: http://127.0.0.1:8000/swagger/
   *ReDoc Documentation*: http://127.0.0.1:8000/redoc/

## 🔐 Authentication

This project utilizes **Token Authentication** to secure its API endpoints. Here's a brief overview:

### Token Authentication

- **Purpose:** Ensure that only authenticated users can access protected endpoints.
- **Implementation:**
  - Users obtain a token by providing their credentials.
  - This token must be included in the `Authorization` header of subsequent API requests.
- **Endpoints:**
  - **Obtain Token:** `/api/token/` (POST)
    - **Payload:**
      ```json
      {
          "username": "yourusername",
          "password": "yourpassword"
      }
      ```
    - **Response:**
      ```json
      {
          "refresh": "your_refresh_token",
          "access": "your_access_token"
      }
      ```
  - **Refresh Token:** `/api/token/refresh/` (POST)
    - **Payload:**
      ```json
      {
          "refresh": "your_refresh_token"
      }
      ```
    - **Response:**
      ```json
      {
          "access": "new_access_token"
      }
      ```

### Protecting Endpoints

- **Admin Endpoints:** Restricted to admin users only.
- **Response Submission:** Open to any authenticated user.

*Note: Ensure that you include the obtained access token in the `Authorization` header as follows:*


## 📦 Usage

Here's how to interact with the **Form Builder API**:

### 1. **Admin Actions**

- **Access Admin Panel:**

Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

- **Manage Forms, Questions, and Options:**

- **Forms:** Create, edit, or delete forms.
- **Questions:** Add various types of questions to each form.
- **Options:** Define selectable options for questions like dropdowns and checkboxes.

### 2. **Submitting Responses**

- **Endpoint:** `POST /api/responses/`

- **Payload Example:**

```json
{
   "form": 3,
   "answers": [
       {
           "question": 1,
           "selected_option": 2
       }
   ]
}
```
## 🎓 Key Learnings
1. **Token-Based Authentication with Django REST Framework:**
   - Implemented secure token authentication to protect API endpoints, ensuring that only authorized users can access sensitive functionalities.
   - Managed token generation, refreshing, and validation using `djangorestframework-simplejwt`, enhancing the security and scalability of the authentication system.

2. **Comprehensive API Documentation:**
   - Utilized `drf-yasg` to generate interactive Swagger/OpenAPI documentation, providing clear and accessible information for developers to understand and test API endpoints.
   - Created organized Postman Collections to facilitate efficient API testing.
   
3. **Backend Development and Data Analytics:**
   - Designed and developed a robust backend system with Django models, serializers, and viewsets to handle dynamic form creation, user responses, and data storage.
   - Developed custom analytics endpoints to process and visualize response data, offering valuable insights and enhancing the decision-making capabilities for administrators.

## 🔮 Future Enhancements

While the current scope covers the backend functionalities, there are several avenues for future development:

- **Frontend Interface:**
  - **User Interface for End-Users:** Enable users to interact with forms seamlessly through a web or mobile application.
  - **Admin Dashboard:** Provide administrators with a user-friendly dashboard to manage forms and view analytics.

- **Advanced Authentication:**
  - **Implement OAuth2:** For more secure and scalable authentication mechanisms.
  - **Role-Based Access Control:** Define user roles with specific permissions.

- **Extended Analytics:**
  - **Sentiment Analysis:** Analyze text responses for sentiment insights.
  - **Data Visualization:** Integrate charts and graphs to represent analytics data visually.

- **Email Notifications:**
  - **Response Alerts:** Notify administrators when new responses are submitted.

- **Deployment:**
  - **Production Setup:** Deploy the application to cloud platforms like Heroku, AWS, or DigitalOcean.
  - **CI/CD Integration:** Automate testing and deployment processes.








   

