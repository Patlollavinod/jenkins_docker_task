pipeline {
    agent any
    stages {
        stage('docker image  build') {
            steps {
                sh 'docker build .'
            }
        }
        stage('checkout '){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/feat-project2']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/prjpracticeteam/githubpractice.git']]])
            }
        }
        stage('git '){
            steps{
              git branch: 'main', url: 'https://github.com/Patlollavinod/jenkins_docker_task.git'
            }
        }
    }
}
