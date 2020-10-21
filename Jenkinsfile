pipeline {
  agent {
    kubernetes {
      yamlFile 'agent.yaml'
    }
  }
  stages {
    stage('Docker Build') {
      steps {
	container('docker') {
        	sh "docker build $WORKSPACE -t nexus:8086/testapp/testapp:${env.BUILD_NUMBER} "
	}
      }
    }
    stage('Docker Push') {
      steps {
	container('docker') {
          withCredentials([usernamePassword(credentialsId: 'nexus', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
            sh "docker login http://nexus:8086 -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
            sh "docker push nexus:8086/testapp/testapp:${env.BUILD_NUMBER}"
          }
	}
      }
    }
}
}
