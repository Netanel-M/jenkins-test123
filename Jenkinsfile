
pipeline {
    agent any
    parameters {
        string(name: count, defaultValue: "0")
    }
    
    options {
        timeout(time: 12, unit: 'HOURS')

    }
    stages {
        stage("Begin") {
            steps {
                echo "Beginning build!"
            }
        }
        stage("Run script with argument") {
            steps {
                sh "python3 script.py $count"
            }
        }
    }
}
