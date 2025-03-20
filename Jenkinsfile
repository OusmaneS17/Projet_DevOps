pipeline {
    agent any

    environment {
        PYTHON_EXE = "C:\\Users\\o.sow\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        VENV_DIR = 'venv'
    }

    stages {
        stage('Récupération du code') {
            steps {
                git branch: 'main', url: 'https://github.com/OusmaneS17/Projet_DevOps.git'
            }
        }

        stage('Installation des dépendances') {
            steps {
                bat '%PYTHON_EXE% -m venv %VENV_DIR%'
                bat 'call %VENV_DIR%\\Scripts\\activate && python -m pip install --upgrade pip || exit 0'
                bat 'call %VENV_DIR%\\Scripts\\activate && pip install -r requirements.txt'
                bat 'call %VENV_DIR%\\Scripts\\activate && pip list'
            }
        }

        stage('Migrations') {
            steps {
                bat 'call %VENV_DIR%\\Scripts\\activate && python manage.py makemigrations'
                bat 'call %VENV_DIR%\\Scripts\\activate && python manage.py migrate'
            }
        }

        /*stage('Tests unitaires') {
            steps {
                bat 'call %VENV_DIR%\\Scripts\\activate && python manage.py test'
            }
        }

        stage('Démarrage du serveur') {
            steps {
                bat 'call %VENV_DIR%\\Scripts\\activate && python manage.py runserver 0.0.0.0:8000'
            }
        }*/
    }

    post {
        success {
            emailext(
                subject: "Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Le build de ${env.JOB_NAME} a réussi.\nConsultez les logs ici: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'oussoumanesow0@gmail.com'
            )
        }

        failure {
            emailext(
                subject: "Build FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Le build de ${env.JOB_NAME} a échoué.\nConsultez les logs ici: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'oussoumanesow0@gmail.com'
            )
        }
    }
}
