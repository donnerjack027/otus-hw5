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
                sh 'pytest -s -v test_suites/test_suite_hw_26.py  --alluredir ${WORKSPACE}/allure-results'
                archiveArtifacts '*.ini'
            }
        }
    }
}