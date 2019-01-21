pipeline {
  agent any
  stages {
    stage('md5check') {
      steps {
        sh 'md5sum -c hash.md5'
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
    stage('validateJson') {
      steps {
        sh 'cat forcast_data.json | python -m json.tool  >> /dev/null && exit 0 || echo "NOT valid JSON"; exit 1'
      }
    }
  }
}