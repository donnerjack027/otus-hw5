pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            additionalBuildArgs '--network=host'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'git --version'
                sh 'pytest --version'
            }
        }
    }
}
