# SpeedAlert 🚦
### Smart Road Hazard Reporting and Early Warning System

## About the Project

SpeedAlert is a project I am developing as a Computer Science student to work on a real-world road safety problem.

While travelling on village roads and highways, people may encounter unexpected speed breakers, damaged roads and other hazards. Sometimes these hazards are not properly marked, which can increase the risk of accidents.

I wanted to develop a software solution where people can report such road hazards, administrators can verify the reports, and drivers can receive warnings about verified hazards.

My goal is to explore how technology can help make everyday road travel safer.

## Why I Chose This Project

I wanted to develop something useful for real-life situations instead of working only on basic academic projects.

Road safety is an issue that affects everyone. Through SpeedAlert, I want to understand how web development, databases and location-based technologies can be combined to address a practical problem.

## Technologies Used

- **Python** – Backend programming
- **Flask** – Web application framework
- **MySQL** – Database management
- **HTML** – Web page structure
- **CSS** – User interface design
- **JavaScript** – Frontend functionality
- **Leaflet and OpenStreetMap** – Planned for interactive maps

## How the Project Works

1. Users report road hazards through the application.
2. Hazard details and GPS coordinates are stored in the MySQL database.
3. The administrator reviews the submitted reports.
4. Genuine hazards are verified, while false reports can be rejected.
5. Verified hazards will be displayed on an interactive map.
6. Drivers will be able to receive warnings when approaching verified hazards.

## Current Development Progress

- [x] Created the Flask application.
- [x] Installed and configured MySQL.
- [x] Connected Flask with MySQL.
- [x] Created the SpeedAlert database.
- [x] Created the hazards table.
- [ ] Complete the hazard reporting form.
- [ ] Implement automatic GPS detection.
- [ ] Develop administrator login.
- [ ] Build the admin dashboard.
- [ ] Implement hazard verification and rejection.
- [ ] Display hazards on an interactive map.
- [ ] Develop the driver warning system.

## Project Structure

```text
SpeedAlert/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── database.py
│   ├── templates/
│   └── static/
│
├── database/
├── docs/
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd SpeedAlert
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the environment

For Windows:

```powershell
venv\Scripts\activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure MySQL

Create a database named `speedalert_db` in MySQL.

Configure your database credentials in a `.env` file in the project root. Never upload this file to GitHub.

### Step 6: Run the application

```bash
python run.py
```

Open the following address in your browser:

`http://127.0.0.1:5000`

## What I Am Learning

Through this project, I am improving my knowledge of:

- Python and Flask backend development
- MySQL database connectivity
- Database design and SQL queries
- Frontend development using HTML, CSS and JavaScript
- GPS-based applications
- Building practical software solutions

## Future Enhancements

- Automatic GPS location detection
- Admin dashboard with secure login
- Duplicate hazard detection
- Interactive road hazard maps
- Location-based driver warnings
- Voice alerts and vibration support

## Project Status

**Currently under development.**

I am building SpeedAlert step by step and will continue updating this repository as I complete new features and learn new technologies.

---

*SpeedAlert – A small step towards safer roads.*