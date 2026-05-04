# 🌍 Village Explorer – Location Intelligence Platform

A full-stack web application that provides hierarchical geographical data of India using a secure and interactive REST API system.

---

## 🚀 Overview

Village Explorer is a location intelligence platform designed to deliver structured geographical data including:

* States
* Districts
* Mandals
* Villages

The system allows users to explore data dynamically through an interactive UI backed by a secure FastAPI backend.

---

## 🎯 Objectives

* Provide structured geographical data using REST APIs
* Implement secure authentication using API keys
* Develop an interactive frontend for hierarchical data selection
* Demonstrate full-stack integration (Frontend + Backend + Database)

---

## ✨ Features

* 🔐 User registration and login system
* 🔑 API key-based authentication
* 📍 Dynamic dropdown selection
* 🔄 Hierarchical filtering:

  * State → District → Mandal → Village
* ⚡ Real-time data fetching from backend
* 🚫 Restricted access for unauthorized users

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* FastAPI (Python)

### Database

* PostgreSQL (Supabase)

---

## 🏗️ System Architecture

The application follows a **client-server architecture**:

1. Frontend sends HTTP requests using Fetch API
2. Backend (FastAPI) processes requests
3. SQL queries retrieve data from PostgreSQL
4. Response is returned and displayed dynamically

---

## ⚙️ How It Works

1. User opens the application
2. Explorer remains locked initially
3. User signs up or logs in
4. API key is generated
5. User selects a state
6. Districts load dynamically
7. Mandals load based on district
8. Villages are fetched accordingly
9. Results are displayed in UI

---

## 🔧 Backend Implementation

* Built using FastAPI
* Database connectivity using SQLAlchemy
* Implemented REST endpoints:

```id="m8j3zq"
/signup
/login
/states
/districts
/mandals
/villages
```

* API key authentication handled via request headers

---

## 🎨 Frontend Implementation

* HTML for structure
* CSS for styling
* JavaScript for:

  * API calls
  * Dynamic dropdown updates
  * User interaction handling
  * Authentication control

---

## 🔐 Security

* API key-based authentication
* Protected endpoints
* Access restricted for unauthorized users

---

## 📊 Results

* Successfully implemented hierarchical data retrieval
* Smooth dynamic UI updates
* Secure API-based architecture

---

## 🚀 Future Enhancements

* 🔍 Search functionality
* 📱 Improved responsive design
* ☁️ Cloud deployment
* ⚡ Performance optimization (caching)

---

## 🎯 Conclusion

The Village Explorer project demonstrates the integration of frontend, backend, and database technologies to build a scalable, secure, and interactive location-based API system.

---

## 👨‍💻 Author

**Srujan Anirudh**
Computer Science Engineering Student

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
