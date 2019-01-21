pipeline {
  agent any
  stages {
    stage('md5check') {
        steps {
          sh 'md5sum -c weather2json.py.md5'
        }
    }
    stage('installRequirements') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('getWeatherJson') {
      steps {
        sh 'python weather2json.py'
      }
    }
  }
}