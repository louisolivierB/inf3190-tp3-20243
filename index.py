# Copyright 2024 <Votre nom et code permanent>
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import random
from flask import Flask, render_template, request, redirect, g
from .database import Database

app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()
        
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/')
def accueil():
    db = get_db()
    data = db.get_animaux()
    animaux = []
    for i in range(5):
       animal = random.choice(data)
       data.remove(animal)
       animaux.append(animal)
    return render_template('accueil.html', animaux=animaux)
    
    
@app.route('/form')
def form():
    return render_template('form.html', erreur_nom=False, erreur_espece=False, 
        erreur_race=False, erreur_age=False, erreur_description=False, erreur_courriel=False, 
        erreur_adresse=False, erreur_ville=False, erreur_cp=False)


@app.route("/submit", methods=['POST'])
def submit():
    erreur_nom = not validation_nom(request.form['nom'])
    erreur_espece = not validation_generique(request.form['espece'])
    erreur_race = not validation_generique(request.form['race'])
    erreur_age = not validation_age(request.form['age'])
    erreur_description = not validation_generique(request.form['description'])
    erreur_courriel = not validation_courriel(request.form['courriel'])
    erreur_adresse = not validation_generique(request.form['adresse'])
    erreur_ville = not validation_generique(request.form['ville'])
    erreur_cp = not validation_cp(request.form['cp'])
    if erreur_nom or erreur_espece or erreur_race or erreur_age or erreur_description \
      or erreur_courriel or erreur_adresse or erreur_ville or erreur_cp:
        return render_template('form.html', erreur_nom=erreur_nom, erreur_espece=erreur_espece,
            erreur_race=erreur_race, erreur_age=erreur_age, erreur_description=erreur_description,
            erreur_courriel=erreur_courriel, erreur_adresse=erreur_adresse, erreur_ville=erreur_ville,
            erreur_cp=erreur_cp), 400
    else:
        db = get_db()
        db.add_animal(request.form['nom'], request.form['espece'], request.form['race'],
            request.form['age'], request.form['description'], request.form['courriel'],
            request.form['adresse'], request.form['ville'], request.form['cp'])
        return redirect('/merci')
      
@app.route('/merci')
def merci():
    return render_template('merci.html')
    

@app.route('/animaux', methods=['POST'])
def animaux():
    db = get_db()
    data = db.get_animaux()
    animaux = []
    for animal in data:
      if animal['nom'].lower() == request.form['query'].lower():
         animaux.append(animal)
      elif animal['espece'].lower() == request.form['query'].lower():
         animaux.append(animal)
      elif animal['race'].lower() == request.form['query'].lower():
         animaux.append(animal)
      elif animal['description'].lower() == request.form['query'].lower():
         animaux.append(animal)
      elif animal['courriel'].lower() == request.form['query'].lower():
         animaux.append(animal)
      elif animal['adresse'].lower() == request.form['query'].lower():
         animaux.append(animal)
      elif animal['ville'].lower() == request.form['query'].lower():
         animaux.append(animal)
      elif animal['cp'].lower() == request.form['query'].lower():
         animaux.append(animal)
    return render_template('animaux.html', animaux=animaux, query=request.form['query']) 
   
   
@app.route('/animal/<id>')
def animal(id):
    animal = get_db().get_animal(id)
    if animal is None:
        return render_template('404.html'), 404
    else:
        return render_template('animal.html', animal=animal)
   
   
def validation_nom(nom):
    return len(nom.strip()) >= 3 and len(nom.strip()) <= 20 and not contient_virgule(nom)
   
   
#todo : verif si char entre 0 et 30 passe le test
def validation_age(age):
    age_pattern = r"^[0-9]+$"
    return re.match(age_pattern, age) and int(age) >= 0 and int(age) <= 30   


def validation_courriel(courriel):
    courriel_pattern = r"^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|.(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"   
    return re.match(courriel_pattern, courriel.lower()) is not None and not contient_virgule(courriel)


def validation_cp(cp):
    cp_pattern = r"^[A-Za-z]\d[A-Za-z]\s\d[A-Za-z]\d$"   
    return re.match(cp_pattern, cp.lower()) is not None and not contient_virgule(cp)
   

def validation_generique(chaine):
    return len(chaine.strip()) != 0 and not contient_virgule(chaine)
   
   
def contient_virgule(chaine):
    return ',' in chaine
