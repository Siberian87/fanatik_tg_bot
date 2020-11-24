from sqlighter import session, User

def get_db_info(user):
    user_db = []
    for row in session.query(User).order_by(User.user_id):
        user_db.append(row.user_id)
    if user in user_db:
        return True
    else:
        return False        
      

