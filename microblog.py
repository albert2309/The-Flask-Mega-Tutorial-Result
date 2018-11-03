from app import create_app, db, cli
from app.models import User, Post, Message, Notification

app = create_app()
cli.register(app)

# When I start a shell with the flask shell command, the model class is automatically imported for me:
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification}

