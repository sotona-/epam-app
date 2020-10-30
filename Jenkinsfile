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
    stage('Docker Push') {
      steps {
      	container('docker') {
          script {
            docker.withRegistry('https://eu.gcr.io', 'gcr:jenkins-docker') {
              def image = docker.build("engaged-yen-293214/testapp:${env.BUILD_ID}")
              image.push("${env.BUILD_ID}")
              myContainer.push("latest")
            }
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
