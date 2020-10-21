pipeline {
  agent {
    kubernetes {
      yamlFile 'agent.yaml'
    }
  }
  stages {
    stage('Build') {
                steps {
                        container('python') {
                                sh 'python3.6 setup.py bdist_egg'
                        }
                }
        }

    stage('Docker Build') {
      steps {
	container('docker') {
        	sh "docker build $WORKSPACE -t nexus:8086/testapp/testapp:${env.BUILD_NUMBER} "
	}
      }
    }
    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'nexus', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh "docker push nexus:8086/testapp/testapp:${env.BUILD_NUMBER}"
        }
      }
    }
}
}
