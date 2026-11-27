
from app.database import db
from app.models import LeaveRequest


def add_leave(employee_id, leave_type, start_date, end_date, reason):
    new_leave = LeaveRequest(
        employee_id=employee_id,
        leave_type=leave_type,
        start_date=start_date,
        end_date=end_date,
        reason=reason
    )

    db.session.add(new_leave)
    db.session.commit()

    return new_leave
#-----
# GET REQUESTS
#-----
def get_leave_by_id(leave_id):
    return db.session.get(LeaveRequest, leave_id)


def get_leaves_by_employee(employee_id):
    return (
        LeaveRequest.query
        .filter_by(employee_id=employee_id)
        .order_by(LeaveRequest.id.desc())
        .all()
    )
    
# def get_leaves_by_employee(employee_id):
#     obj = LeaveRequest.query.filter_by(employee_id=employee_id).order_by(LeaveRequest.id.desc()).all()
#     print("Obj: ", obj)
#     return (
#         obj
#     )


def get_leaves_by_employees(employee_ids):
    if not employee_ids:
        return []

    return (
        LeaveRequest.query
        .filter(LeaveRequest.employee_id.in_(employee_ids))
        .order_by(LeaveRequest.id.desc())
        .all()
    )


def get_all_leaves():
    return LeaveRequest.query.order_by(
        LeaveRequest.id.desc()
    ).all()


def update_leave(leave, leave_type, start_date, end_date, reason):
    leave.leave_type = leave_type
    leave.start_date = start_date
    leave.end_date = end_date
    leave.reason = reason

    db.session.commit()

    return leave


def process_leave(leave, status, manager_remarks):
    leave.status = status
    leave.manager_remarks = manager_remarks

    db.session.commit()

    return leave


def delete_leave(leave):
    db.session.delete(leave)
    db.session.commit()
