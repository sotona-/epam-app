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
            def tag = ''
            def release = false
            if (env.gitlabBranch.contains('refs/tags')) {
              tag = env.gitlabBranch.replace('refs/tags/','')
              release = true
            } else {
              tag = env.BUILD_ID
            }
            sh "sed -i 's/__TAG__/${tag}/g' app/templates/index.html"
            docker.withRegistry('https://eu.gcr.io', 'gcr:registry') {
              def image = docker.build("engaged-yen-293214/testapp:${tag}")
              image.push("${tag}")
              image.push("latest")
            }
          }
	      }
      }
    }
    stage('Deploy') {
      steps{
	      container('kubectl') {
          if (release) {
            sh "sed -i 's/__NS__/testapp-test/g' k8s/manifest.yaml"
          } else {
            sh "sed -i 's/__NS__/testapp-release/g' k8s/manifest.yaml"
          }
          sh "sed -i 's/__TAG__/${tag}/g' k8s/manifest.yaml"
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
