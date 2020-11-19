from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import enum

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(db.Text, nullable=False)

    #feedback = db.relationship("Feedback", backref="user", cascade="all,delete")

    # start of convenience class methods

    @classmethod
    def register(cls, username, password):
        """Register a user, hashing their password."""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            username=username,
            password=hashed_utf8
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False


class Board(db.Model):
    """Board."""

    __tablename__ = "boards"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.Text,
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade')
    )

    """
    position = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )
    """

class List(db.Model):
    """List."""

    __tablename__ = "lists"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.Text,
        nullable=False,
    )

    board_id = db.Column(
        db.Integer,
        db.ForeignKey('boards.id', ondelete='cascade')
    )



class CardStatusEnum(enum.Enum):
    done = 'done'
    WIP = 'WIP'
    cancelled = "cancelled"

class Card(db.Model):
    """Card."""

    __tablename__ = "cards"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.Text,
        nullable=False,
    )

    content = db.Column(
        db.Text,
    )


    card_status = db.Column(
        db.Enum(CardStatusEnum), 
        default= CardStatusEnum.WIP,
        nullable=False
    )

    list_id = db.Column(
        db.Integer,
        db.ForeignKey('lists.id', ondelete='cascade')
    )