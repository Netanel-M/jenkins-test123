
pipeline {
    agent {
        label: 'linux'
    }
    parameters {
        string(name: 'COUNT', defaultValue: '0')
    }
    stages {
        stage("Begin") {
            steps {
                echo "Beginning build!"
            }
        }
        stage("Run script with argument") {
            steps {
                echo "$COUNT"
                sh 'python3 script.py $COUNT' > artifact.txt
            }
        }
        stage("Archive artifacts") {
            steps {
                archiveArtifacts artifacts: '*.txt', followSymlinks: false
            }
        }
    }
}
