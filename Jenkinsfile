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
                    bat 'docker build -t %DOCKER_IMAGE% .'
                }
            }
        }

        stage('Déploiement sur Docker') {
            steps {
                script {
                    echo "🚀 Déploiement de l’application sur Docker..."
                    bat 'docker stop %DOCKER_CONTAINER% || true'
                    bat 'docker rm %DOCKER_CONTAINER% || true'
                    bat 'docker run -d --name %DOCKER_CONTAINER% -p 8000:8000 %DOCKER_IMAGE%'
                }
            }
        }
    }

    /*post {
        always {
            emailext (
                subject: "Build ${currentBuild.fullDisplayName}",
                body: "Le build a ${currentBuild.result}. Voir les logs ici : ${env.BUILD_URL}",
                to: 'oussoumanesow0@gmail.com'  // Remplace ici par l'email des destinataires réels
            )
        }
    }*/


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
                to: 'oussoumanesow0@gmail.com'
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
                to: 'oussoumanesow0@gmail.com',
            )
        }
    }
}
