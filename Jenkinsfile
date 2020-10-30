pipeline {
  agent {
    kubernetes {
      yamlFile 'agent.yaml'
    }
  }
  environment {
        PROJECT_ID = 'engaged-yen-293214'
        CLUSTER_NAME = 'cluster-1'
        LOCATION = 'europe-north1-a'
        CREDENTIALS_ID = 'engaged-yen-293214'
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
    stage('Deploy') {
      steps{
	      container('kubectl') {
          step([
            $class: 'KubernetesEngineBuilder',
            projectId: env.PROJECT_ID,
            clusterName: env.CLUSTER_NAME,
            location: env.LOCATION,
            manifestPattern: 'k8s/manifest.yaml',
            credentialsId: env.CREDENTIALS_ID,
            verifyDeployments: true
          ])
	      }
      }
    }
  }
}
