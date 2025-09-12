# POS System (Django + Next.js + Tailwind CSS)

A full-stack Point of Sale (POS) system built with:

- **Frontend:** Next.js (React + TypeScript) with Tailwind CSS  
- **Backend:** Django REST Framework with JWT Authentication  
- **Database:** PostgreSQL  
- **Deployment:** Render (Backend) + Netlify (Frontend)  

This system supports authentication, user management, inventory, procurement, finance, sales, and reporting modules.

---

## 🚀 Features

- 🔐 **Authentication & Authorization** (JWT-based)  
- 👥 **User Roles** (Admin, Staff, etc.)  
- 📦 **Inventory Management**  
- 🛒 **Procurement Tracking** (request, approve, receive)  
- 💰 **Finance Module** (budget, expenses, payments)  
- 📊 **Sales & Reporting**  
- 🌙 **Dark/Light Mode UI**  
- 📱 Responsive design with **Tailwind CSS**

---

## 📂 Project Structure

pos-system/
├── backend/ # Django REST Framework (API)
│ ├── pos_backend/ # Django project root
│ ├── apps/ # Custom apps (auth, inventory, finance, etc.)
│ ├── requirements.txt
│ └── manage.py
│
├── frontend/ # Next.js (React + TypeScript)
│ ├── components/ # Reusable UI components
│ ├── pages/ # App pages (Dashboard, Inventory, Sales, etc.)
│ ├── hooks/ # Custom React hooks
│ ├── services/ # API service (fetch + auth helpers)
│ ├── public/ # Static assets
│ └── tailwind.config.js
│
└── README.md
