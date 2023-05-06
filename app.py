from flask import Flask, request
import numpy as np
import random

app = Flask(__name__)

history = ["Historiography and Historical Methodologies",
           "World History and Globalization",
           "Colonialism and Post-Colonialism",
           "The Cold War and Its Impact",
           "The Rise and Fall of Empires",
           "Comparative Revolutions",
           "Gender and History",
           "Environmental History",
           "War and Society",
           "Intellectual History"]

science = ["Introduction to Biology",
           "Fundamentals of Chemistry",
           "Physics and Its Applications",
           "Genetics and Genomics",
           "Organic Chemistry",
           "Ecology and Environmental Science",
           "Molecular Biology and Biotechnology",
           "Earth and Space Science",
           "Quantum Mechanics",
           "Neuroscience"]

drawing = ["Introduction to Drawing Techniques",
           "Life Drawing: Anatomy and Gesture",
           "Perspective Drawing",
           "Portrait Drawing",
           "Figure Drawing",
           "Still Life Drawing",
           "Landscape Drawing",
           "Color Theory for Artists",
           "Inking Techniques",
           "Digital Drawing"]

technology = ["Introduction to Programming",
              "Data Structures and Algorithms",
              "Database Design and Management",
              "Web Development",
              "Computer Networks and Security",
              "Mobile App Development",
              "Artificial Intelligence and Machine Learning",
              "Operating Systems and Computer Architecture",
              "Computer Graphics and Visualization",
              "Software Engineering"]

music = ["Introduction to Music Theory",
         "Ear Training and Sight Singing",
         "Music History and Appreciation",
         "Choral and Ensemble Techniques",
         "Music Composition and Arranging",
         "Jazz Theory and Improvisation",
         "Electronic Music Production",
         "Music Education and Pedagogy",
         "Music Therapy",
         "World Music and Ethnomusicology"]

education = ["Foundations of Education",
             "Curriculum Design and Development",
             "Assessment and Evaluation in Education",
             "Classroom Management Strategies",
             "Educational Psychology and Learning Theories",
             "Teaching Methods and Instructional Strategies",
             "Multicultural Education and Diversity in the Classroom",
             "Special Education and Inclusion Practices",
             "Educational Technology Integration",
             "Research Methods in Education"]


@app.route('/predict', methods=['POST'])
def predict():
    random_history = random.sample(history, 3)
    data = request.form['data']

    request_array = data.split(',')

    print(request_array[0])
    return data


if __name__ == '__main__':
    app.run()
