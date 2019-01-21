pipeline {
  agent any
  stages {
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