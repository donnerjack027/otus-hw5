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
            steps {
                sh 'pylint --disable=W1202 --output-format=parseable --reports=no module > pylint.log || echo "pylint exited with $?")'
                sh 'cat render/pylint.log'
            }
            step([
                    $class                     : 'WarningsPublisher',
                    parserConfigurations       : [[
                                                          parserName: 'PYLint',
                                                          pattern   : 'pylint.log'
                                                  ]],
                    unstableTotalAll           : '0',
                    usePreviousBuildAsReference: true
            ])
        }

    }
}