pipeline {
  agent any
  stages {
    stage('getWeatherJson') {
      steps {
        sh 'python weather2json.py'
      }
    }
  }
}