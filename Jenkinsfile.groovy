pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            additionalBuildArgs '--network=host'
        }
    stages {
            steps {
                sh 'git --version'
                sh 'pytest --version'
            }
        }
    }
}