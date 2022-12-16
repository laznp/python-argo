pipeline {
    agent none
    stages {
        stage("Checkout") {
            agent any
            steps {
                git branch: 'main', credentialsId: 'github-credential', url: 'git@github.com:laznp/python-argo.git'
            }
        }
        stage('Build Frontend') {
            agent any
            when {
                changeset "**/frontend/*.*"
                beforeAgent true
            }
            steps {
                dir('frontend') {
                  sh """
                    echo "building frontend"
                  """
                }
            }
        }
        stage('Build Backend') {
            agent any
            when {
                changeset "**/backend/*.*"
                beforeAgent true
            }
            steps {
               dir ('backend') {
                  sh """
                    echo "building backend"
                  """
               }
            }
        }
    }
}
