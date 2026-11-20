
from flask import Blueprint, render_template, request
from app.database import get_db_connection

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/about")
def about():
    return "Welcome to SpeedAlert - Smart Road Hazard Intelligence System"


@main.route("/report", methods=["POST"])
def report_hazard():

    hazard_type = request.form.get("hazard_type")
    description = request.form.get("description")
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    road_type = request.form.get("road_type")
    severity = request.form.get("severity")
    visibility = request.form.get("visibility")

    if not all([hazard_type, latitude, longitude,
                road_type, severity, visibility]):
        return render_template(
            "index.html",
            message="Please complete all required fields."
        )

    try:
        latitude = float(latitude)
        longitude = float(longitude)

        if not (-90 <= latitude <= 90 and
                -180 <= longitude <= 180):
            raise ValueError("Invalid GPS coordinates")

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO hazards
            (hazard_type, description, latitude, longitude,
             road_type, severity, visibility)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            hazard_type, description, latitude, longitude,
            road_type, severity, visibility
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return render_template(
            "index.html",
            message="Hazard reported successfully!"
        )

    except (ValueError, TypeError):
        return render_template(
            "index.html",
            message="Please enter valid GPS coordinates."
        )

    except Exception as error:
        print("Database error:", error)
        return render_template(
            "index.html",
            message="Unable to save the report. Please try again."
        )
