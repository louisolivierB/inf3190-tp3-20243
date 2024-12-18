document.getElementById("form-adoption").onkeypress = function(e) {
  let key = e.charCode || e.keyCode || 0;     
  if (key == 13) {
    e.preventDefault();
  }
};

function validationNom() {
   let nom = document.getElementById("nom").value;
   if(nom.trim().length >= 3 && nom.trim().length <= 20 && !contientVirgule(nom)) {
      cacherErreur("erreur-nom"); 
      return true;
   } else {
      afficherErreur("erreur-nom");  
      return false;
   }
}

function validationEspece() {
   let espece = document.getElementById("espece").value;
   if(espece.trim().length != 0 && !contientVirgule(espece)) {
      cacherErreur("erreur-espece"); 
      return true;
   } else {
      afficherErreur("erreur-espece");  
      return false;
   }
}

function validationRace() {
   let race = document.getElementById("race").value;
   if(race.trim().length != 0 && !contientVirgule(race)) {
      cacherErreur("erreur-race"); 
      return true;
   } else {
      afficherErreur("erreur-race");  
      return false;
   }
}

function validationAge() {
   let age = document.getElementById("age").value;
   if(/^[0-9]+$/.test(age) && age >= 0 && age <= 30) {
      cacherErreur("erreur-age"); 
      return true;
   } else {
      afficherErreur("erreur-age");  
      return false;
   }
}

function validationDescription() {
   let description = document.getElementById("description").value;
   if(description.trim().length != 0 && !contientVirgule(description)) {
      cacherErreur("erreur-description");
      return true;
   } else {
      afficherErreur("erreur-description");
      return false;
   }
}

function validationCourriel() {
   let courriel = document.getElementById("courriel").value;
   let courrielValide =  courriel.toLowerCase().match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
   if(courrielValide && !contientVirgule(courriel)) {
      cacherErreur("erreur-courriel");
      return true;
   } else {
      afficherErreur("erreur-courriel");
      return false;
   }
}

function validationAdresse() {
   let adresse = document.getElementById("adresse").value;
   if(adresse.trim().length != 0 && !contientVirgule(adresse)) {
      cacherErreur("erreur-adresse");
      return true;
   } else {
      afficherErreur("erreur-adresse");
      return false;
   }
}

function validationVille() {
   let ville = document.getElementById("ville").value;
   if(ville.trim().length != 0 && !contientVirgule(ville)) {
      cacherErreur("erreur-ville");
      return true;
   } else {
      afficherErreur("erreur-ville");
      return false;
   }
}

function validationCP() {
   let cp = document.getElementById("cp").value;
   let patternCP = /^[A-Za-z]\d[A-Za-z]\s\d[A-Za-z]\d$/;
   if(patternCP.test(cp) && !contientVirgule(cp)) {
      cacherErreur("erreur-cp");
      return true;
   } else {
      afficherErreur("erreur-cp");
      return false;
   }
}

function validationFormAdoption() {
   erreurNom = validationNom();
   erreurEspece = validationEspece();
   erreurRace = validationRace();
   erreurAge = validationAge();
   erreurDescription = validationDescription();
   erreurCourriel = validationCourriel();
   erreurAdresse = validationAdresse();
   erreurVille = validationVille();
   erreurCP = validationCP();
   return erreurNom && erreurEspece && erreurRace && erreurDescription && 
      erreurCourriel && erreurAdresse && erreurVille && erreurCP
}

function afficherErreur(erreurId) {
   erreur = document.getElementById(erreurId);
   erreur.style.display = "inline";
}

function cacherErreur(erreurId) {
   erreur = document.getElementById(erreurId);
   erreur.style.display = "none";
}

function contientVirgule(chaine) {
   return chaine.includes(",");
}

document.getElementById("nom").addEventListener("change", validationNom); 
document.getElementById("espece").addEventListener("change", validationEspece); 
document.getElementById("race").addEventListener("change", validationRace); 
document.getElementById("age").addEventListener("change", validationAge); 
document.getElementById("description").addEventListener("change", validationDescription); 
document.getElementById("courriel").addEventListener("change", validationCourriel);
document.getElementById("adresse").addEventListener("change", validationAdresse); 
document.getElementById("ville").addEventListener("change", validationVille); 
document.getElementById("cp").addEventListener("change", validationCP);
document.getElementById("form-adoption").addEventListener("submit", e=> {
   e.preventDefault();
   if(validationFormAdoption())
      document.getElementById("form-adoption").submit();
   else
      return false;
});
