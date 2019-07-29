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
                try {
                    sh 'pytest -s -v test_suites/test_suite_hw_26.py  --alluredir ${WORKSPACE}/allure-results'
                }
                catch (e) {
                    currentBuild.result = 'FAILURE'
                    throw e
                }
                finally {
                    stage('Report') {
                        steps {
                            script {
                                    allure([
                                            includeProperties: false,
                                            jdk: '',
                                            properties: [],
                                            reportBuildPolicy: 'ALWAYS',
                                            results: [[path: 'target/allure-results']]
                                    ])
                            }
                        }
                    }
                }
            }
        }

    }
}