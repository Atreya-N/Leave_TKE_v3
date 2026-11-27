
from app.database import db


class LeaveRequest(db.Model):
    __tablename__ = "Leave_Requests"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("Users.id"),
        nullable=False
    )

    leave_type = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.Text, nullable=False)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Pending"
    )

    manager_remarks = db.Column(db.Text, nullable=True)
