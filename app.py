from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Employee({self.id}, {self.name}, {self.department})"


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        try:
            employee_id = int(request.form['employee_id'])
            name = request.form['name']
            department = request.form['department']

            if not (employee_id and name and department):
                return render_template('add_employee.html', error="All fields are required!")

            
            existing_employee = Employee.query.get(employee_id)
            if existing_employee:
                return render_template('add_employee.html', error="Employee ID must be unique!")

            
            new_employee = Employee(id=employee_id, name=name, department=department)
            db.session.add(new_employee)
            db.session.commit()
            return render_template('add_employee.html', success=f"Employee {name} added successfully!")
        except ValueError:
            return render_template('add_employee.html', error="Employee ID must be a number!")

    return render_template('add_employee.html')

@app.route('/view_employees')
def view_employees():
    employees = Employee.query.all()  
    return render_template('view_employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
