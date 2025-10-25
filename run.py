from app import create_app, db
from app.models import User  # Class names should match the model (capitalized)

app = create_app()

# Create all tables within the application context
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
