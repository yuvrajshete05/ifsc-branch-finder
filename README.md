# IFSC Branch Finder API

A Django REST API service for retrieving bank and branch details based on IFSC codes, bank name, and city.

🔗 **Live URL**: [https://ifsc-branch-finder-3.onrender.com](https://ifsc-branch-finder-3.onrender.com)

---

## 📌 Problem Statement

Build an API server that serves bank and branch information. It should allow:
- Listing all banks
- Fetching branch details using IFSC
- Searching branches by bank name and city

---

## 🧠 Method Used to Solve the Problem

1. **Chose Python and Django**:  
   Used Django for quick API development and its powerful ORM to handle database models.

2. **Created Models**:  
   - `Bank`: Stores bank name and ID.
   - `Branch`: Stores branch name, IFSC, address, city, and a foreign key to `Bank`.

3. **Loaded Data**:  
   - Parsed and loaded the provided CSV into the SQLite database using a custom Django management command.

4. **Built API Views**:
   - Created REST API endpoints using Django views (no DRF used to keep it lightweight).
   - Used query parameters to filter data.

5. **URL Routing**:
   - `/api/banks/`: Returns all banks.
   - `/api/branches/?ifsc=...`: Returns branch by IFSC.
   - `/api/branches/?bank_name=...&city=...`: Returns matching branches.

6. **CORS & Deployment Settings**:
   - Set `ALLOWED_HOSTS` to allow Render domain.
   - Installed `gunicorn` for production.

7. **Deployed to Render**:
   - Uploaded code to GitHub.
   - Connected Render to GitHub for auto-deploy.
   - Set `Start Command`: `gunicorn bankproject.wsgi`.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite
- **Deployment**: Render.com

---

