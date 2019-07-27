pipeline {
    agent none
    stage ('Checkout') {
        agent any
        steps {
            git(
                url: 'https://github.com/donnerjack027/otus-hw5.git',
                credentialsId: 'CREDENTIALS',
                branch: "master"
            )
        }
    }
    stage ('Build') {
        agent {
            dockerfile {
                filename 'Dockerfile'
                args '--network=host'
            }
        }
        steps {
            sh 'git --version'
            sh 'pytest --version'
        }
    }
}