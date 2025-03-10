from flask import Blueprint,render_template, request,flash, jsonify
from flask_login import  login_required , current_user
from .models import Note
from . import db
import json

veiws = Blueprint('views',__name__)

@veiws.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note is too short","error")
        else:
            newNote = Note(data=note,user_id=current_user.id)
            db.session.add(newNote)
            db.session.commit()
            fla = flash("Note Added","success")
    return render_template('home.html',user=current_user)


@veiws.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted','warning')
    return jsonify({})