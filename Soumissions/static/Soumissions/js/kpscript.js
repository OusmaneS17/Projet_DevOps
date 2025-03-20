document.addEventListener('DOMContentLoaded', function() {
    // Récupération des éléments du formulaire
    var form = document.getElementById('enqueteForm');// Assurez-vous que l'ID est correct

    var classe= document.getElementById('classe');// Assurez-vous que l'ID est correct

    function toggleSubmitButton() {
        var classes = parseInt(classe.value);
        
         // Vérifications
        if (!isNaN(classes) ) {
            // Activation du bouton 
            
            form.querySelector('button[type="submit"]').removeAttribute('disabled');
        } else {
            // Désactivation du bouton 
            
            form.querySelector('button[type="submit"]').setAttribute('disabled', 'disabled');
        }
    }

    
       classe.addEventListener('input', function() {
           toggleSubmitButton();
                
       });

    // Ajout d'un écouteur d'événements pour la soumission du formulaire
    form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
            }
        
    });
});
