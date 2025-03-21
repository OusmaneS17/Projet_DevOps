pipeline {
    agent any

    environment {
        PYTHON_EXE = "C:\\Users\\o.sow\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        VENV_DIR = 'venv'
        DOCKER_IMAGE = "django_image"
        DOCKER_CONTAINER = "container_app_django"
        EMAIL_RECIPIENTS = "oussoumanesow0@gmail.com"
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

        stage('Construction de l\'image Docker') {
            steps {
                script {
                    echo "🐳 Construction de l’image Docker..."
                    bat 'docker build -t ${env.DOCKER_IMAGE} .'
                }
            }
        }

        stage('Déploiement sur Docker') {
            steps {
                script {
                    echo "🚀 Déploiement de l’application sur Docker..."
                    bat 'docker stop ${env.DOCKER_CONTAINER} || true'
                    bat 'docker rm ${env.DOCKER_CONTAINER} || true'
                    bat 'docker run -d --name ${env.DOCKER_CONTAINER} -p 8080:8000 ${env.DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build et déploiement réussis !"
            emailext(
                subject: "✅ Déploiement réussi : ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    🎉 L’application a été déployée avec succès !  
                    🔗 Consultez les logs ici: ${env.BUILD_URL}  
                    🌍 Accédez à l’application sur : http://<IP_SERVEUR>:8000/
                """,
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: env.EMAIL_RECIPIENTS
            )
        }

        failure {
            echo "❌ Échec du pipeline !"
            emailext(
                subject: "❌ Échec du déploiement : ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    ❗ Une erreur est survenue pendant le pipeline.  
                    📜 Consultez les logs ici: ${env.BUILD_URL}
                """,
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: env.EMAIL_RECIPIENTS
            )
        }
    }
}
