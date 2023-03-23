ppipeline {
    agent any
    stages{
        stage('docker image build') {
            steps {
               sh 'docker build  main.py .'
        stage('Checkout') {
            steps {
               checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Patlollavinod/jenkins_docker_task.git']]])
            }
        }
        stage('Run python program') {
            steps {
                 git branch: 'main', url: 'https://github.com/Patlollavinod/jenkins_docker_task.git'
                sh 'python main.py '
            }
        }                 
           }
        }
    }
}
