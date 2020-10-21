pipeline {
  agent any
  stages {
    stage('Docker Build') {
      steps {
        sh "docker build $WORKSPACE -t frezzzer/test-py-app:${env.BUILD_NUMBER} "
      }
    }
    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'frezzzer_docker_hub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh "docker push frezzzer/test-py-app:${env.BUILD_NUMBER}"
        }
      }
    }
    stage('Docker Remove Image') {
      steps {
        sh "docker rmi frezzzer/test-py-app:${env.BUILD_NUMBER}"
      }
    }
}
}
