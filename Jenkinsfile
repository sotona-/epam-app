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
        tag = ''
        release = false
  }
  stages {
    stage('Docker Push') {
      steps {
      	container('docker') {
          script {
            println('1')
            println(env.tag)
            if (env.gitlabBranch.contains('refs/tags')) {
              env.tag = env.gitlabBranch.replace('refs/tags/','')
              env.release = true
              println('2')
              println(env.tag)
            } else {
              env.tag = env.BUILD_ID
            }
            println('3')
            println(env.tag)
            sh "sed -i 's/__TAG__/${env.tag}/g' app/templates/index.html"
            docker.withRegistry('https://eu.gcr.io', 'gcr:registry') {
              def image = docker.build("engaged-yen-293214/testapp:${env.tag}")
              image.push("${env.tag}")
              if (env.release) {
                image.push("latest")
              }
            }
          }
	      }
      }
    }
    stage('Deploy') {
      steps{
	      container('kubectl') {
          script {
            if (env.release) {
              sh "sed -i 's/__NS__/testapp-test/g' k8s/manifest.yaml"
            } else {
              sh "sed -i 's/__NS__/testapp-release/g' k8s/manifest.yaml"
            }
          }
          sh "sed -i 's/__TAG__/${env.tag}/g' k8s/manifest.yaml"
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
