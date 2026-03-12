pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                echo 'Preparing environment...'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }
        stage('Results') {
            steps {
                echo 'Gathering and saving results...'
            }
        }
    }
}