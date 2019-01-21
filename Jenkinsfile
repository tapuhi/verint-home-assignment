pipeline {
  agent any
  stages {
    stage('installRequirements') {
      steps {
        sh '''ls -altrh
pip install -r requirements.txt'''
      }
    }
    stage('getWeatherJson') {
      steps {
        sh 'python weather2json.py'
      }
    }
  }
}