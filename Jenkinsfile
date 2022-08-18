
pipeline {
    agent any
    parameters {
        text(name: COUNT, defaultValue: "0")
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
                echo "test"
            }
        }
    }
}
