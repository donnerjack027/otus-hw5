pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            args '--network=host'
        }
        steps {
            sh 'git --version'
            sh 'pytest --version'
        }
    }
}