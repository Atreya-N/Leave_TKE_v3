
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
    
    # def __repr__(self):
    #     return f"<LeaveRequest {self.id}>"
    
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "employee_id": self.employee_id,
    #         "leave_type": self.leave_type,
    #         "start_date": self.start_date,
    #         "end_date": self.end_date,
    #         "reason": self.reason,
    #         "status": self.status,
    #         "manager_remarks": self.manager_remarks
    #     }