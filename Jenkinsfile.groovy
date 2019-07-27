pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            args '--network=host'
        }
    stages {
            steps {
                sh 'git --version'
                sh 'pytest --version'
            }
        }
    }
}