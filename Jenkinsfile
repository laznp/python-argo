pipeline {
    agent none
    stages {
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
        stage('Build Web') {
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
