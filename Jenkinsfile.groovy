pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            additionalBuildArgs '--network=host'
        }
    }
    stages {
        stage('Pylint') {
                steps {
                    sh 'pylint --disable=E1206 test_suites/test_suite_hw_26.py'
                    archiveArtifacts 'render/pylint.log'
                }
            }
        stage('Test') {
            steps {
                sh 'pytest -s -v test_suites/test_suite_hw_26.py  --alluredir ${WORKSPACE}/allure-results'
                archiveArtifacts '*.ini'
            }
        }
    }
    post {
        always {
            allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
            ])
        }
        success {
            echo 'Successfully!'
        }
        failure {
            echo 'Failed!'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
    }
}