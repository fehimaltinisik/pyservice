from sqlmodel import Session
from sqlmodel import select

from src.clients.sqliteclient import in_session
from src.entities import Order
from src.exceptions import order_exceptions


@in_session
def save_and_refresh(session: Session, order: Order) -> None:
    """Saves and refreshes the order object with the new ID."""
    session.add(order)
    session.commit()

    session.refresh(order)


@in_session
def find_by_id(session: Session, order_id: int) -> Order:
    query = select(Order).where(Order.id == order_id)
    result = session.exec(query).one_or_none()
    if not result:
        raise order_exceptions.OrderNotFound(f"User with ID {order_id} not found!")

    return result


"""
# @with_session
def update_user(user: User):
    cursor.execute('UPDATE users SET email=?, birth_time=? WHERE id=?',
                   (*user.row(), user.id))
    connection.commit()
    logger.debug(f"User {user.id} updated")
+
    

# @with_session
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    connection.commit()
    logger.debug(f"User with ID {user_id} deleted")
"""
