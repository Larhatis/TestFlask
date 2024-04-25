from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'mon_utilisateur' and password == 'mon_mot_de_passe':
            return redirect(url_for('notes'))
        else:
            return 'Nom d\'utilisateur ou mot de passe incorrect.'
    return render_template('connexion.html')
@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    with open('notes.txt', 'r') as f:
        notes = f.readlines()
    notes.pop(note_id)
    with open('notes.txt', 'w') as f:
        f.writelines(notes)
    return redirect(url_for('notes'))

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        note = request.form['note']
        with open('notes.txt', 'a') as f:
            f.write(note + '\n')
        return redirect(url_for('notes'))
    notes = []
    with open('notes.txt', 'r') as f:
        notes = f.readlines()
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
