Created a file to count vovels in a wordsimple-pipeline
================
https://github.com/MarcoFasa17/simple-pipeline-.git

Step-by-step recap

1. Created app.py  
def count_vowels(word):  
    return sum(1 for ch in word.lower() if ch in 'aeiou')

2. Created test_app.py  
import unittest  
from app import count_vowels  
class TestApp(unittest.TestCase):  
    def test_count_vowels(self):  
        self.assertEqual(count_vowels("hello"), 2)

3. Created empty requirements.txt

4. Created Jenkinsfile  
pipeline {  
    agent { docker { image 'python:3.11-slim' } }  
    stages {  
        stage('Checkout') { steps { checkout scm } }  
        stage('Build')  { steps { sh 'python --version' } }  
        stage('Test')   { steps { sh 'python -m unittest test_app.py -v' } }  
        stage('Deploy') { steps { echo 'Deployment successful' } }  
    }  
}

5. Pushed all files to GitHub repo above

6. Jenkins > New Pipeline job > pointed to this repo > Build Now → all stages green