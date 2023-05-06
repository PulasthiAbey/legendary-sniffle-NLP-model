from flask import Flask, request
import numpy as np
import random

app = Flask(__name__)

history = [
    {"title": "Historiography and Historical Methodologies",
        "link": "https://youtu.be/4UcFGh1Aj90"},
    {"title": "Colonialism and Post-Colonialism",
     "link": "https://youtu.be/SIxg9mGKFCg"},
    {"title":  "The Cold War and Its Impact",
               "link": "https://youtu.be/XDrykOhrb5s"},
    {"title":  "The Rise and Fall of Empires",
               "link": "https://youtu.be/OdX69Hbqmm4"},
    {"title": "Comparative Revolutions",
     "link": "https://youtu.be/U6AbSz1sj28"},
    {"title": "Gender and History", "link": "https://youtu.be/5e12ZojkYrU"},
    {"title": "Environmental History",
     "link": "https://youtu.be/KkFdDPBbn20"},
    {"title": "War and Society", "link": "https://youtu.be/fzd06DRvRKA"},
    {"title": "Intellectual History", "link": "https://youtu.be/-0rY78EQ2B4"}
]

science = [
    {"title": "Introduction to Biology", "link": "https://youtu.be/QnQe0xW_JY4"},
    {"title": "Physics and Its Applications", "link": "https://youtu.be/J6qtNLZIWd0"},
    {"title":  "Fundamentals of Chemistry", "link": "https://youtu.be/7YJvx6dlq6M"},
    {"title":  "Genetics and Genomics", "link": "https://youtu.be/C9aykwOpxns"},
    {"title": "Organic Chemistry", "link": "https://youtu.be/bVhcT2-QMEc"},
    {"title": "Ecology and Environmental Science", "link": "https://youtu.be/E6WAQpRulhA"},
    {"title": "Molecular Biology and Biotechnology", "link": "https://youtu.be/63XZFayqtHA"},
    {"title": "Earth and Space Science", "link": "https://youtu.be/s73tjJfyESM"},
    {"title": "Quantum Mechanics", "link": "https://youtu.be/ZbpRlKRaE8Q"}, 
    {"title": "Neuroscience", "link": "https://youtu.be/qPix_X-9t7E"}
]

drawing = [
    {"title": "Introduction to Drawing Techniques", "link": "https://youtu.be/cE6JBbTvTp4"},
    {"title": "Life Drawing: Anatomy and Gesture", "link": "https://youtu.be/NAY5N76VP8M"},
    {"title": "Perspective Drawing", "link": "https://youtu.be/Xn_0wEwZNEU"},
    {"title": "Portrait Drawing", "link": "https://youtu.be/W9pTY2AEUp4"},
    {"title": "Figure Drawing", "link": "https://youtu.be/9m4Hf_6U4Rc"},
    {"title": "Still Life Drawing", "link": "https://youtu.be/vTvSTspyp9U"},
    {"title": "Landscape Drawing", "link": "https://youtu.be/jQSfv55n0O0"},
    {"title": "Color Theory for Artists", "link": "https://youtu.be/NBg3GjrcMF4"},
    {"title": "Inking Techniques", "link": "https://youtu.be/7aMoBqmCbOE"}, 
    {"title": "Digital Drawing", "link": "https://youtu.be/iwRa5qTnr8o"}
]

technology = [
    {"title": "Introduction to Programming", "link": "https://youtu.be/zOjov-2OZ0E"},
    {"title": "Data Structures and Algorithms", "link": "https://youtu.be/bum_19loj9A"},
    {"title": "Database Design and Management", "link": "https://youtu.be/h0j0QN2b57M"},
    {"title": "Web Development", "link": "https://youtu.be/ysEN5RaKOlA"},
    {"title": "Computer Networks and Security", "link": "https://youtu.be/RkPs8Jl9TKk"},
    {"title": "Mobile App Development", "link": "https://youtu.be/Sfpcl4FX3TU"},
    {"title": "Artificial Intelligence and Machine Learning", "link": "https://youtu.be/9QErWiClGjM"},
    {"title": "Operating Systems and Computer Architecture", "link": "https://youtu.be/vBURTt97EkA"},
    {"title": "Computer Graphics and Visualization", "link": "https://youtu.be/NmMky9Pg8Yc"}, 
    {"title": "Software Engineering", "link": "https://youtu.be/O753uuutqH8"}
]

music = [
    {"title": "Introduction to Music Theory", "link": "https://youtu.be/rgaTLrZGlk0"},
    {"title": "Ear Training and Sight Singing", "link": "https://youtu.be/Ed2VUq9cu1I"},
    {"title": "Music History and Appreciation", "link": "https://youtu.be/PRO3eWavWrs"},
    {"title": "Choral and Ensemble Techniques", "link": "https://youtu.be/juQjapTu8oI"},
    {"title": "Music Composition and Arranging", "link": "https://youtu.be/iiL3K3ewfuc"},
    {"title": "Jazz Theory and Improvisation", "link": "https://youtu.be/lhNZEIFv3uk"},
    {"title": "Electronic Music Production", "link": "https://youtu.be/FgFXlGjIbyk"},
    {"title": "Music Education and Pedagogy", "link": "https://youtu.be/R-8XEdI-AXQ"},
    {"title": "Music Therapy", "link": "https://youtu.be/eqIijgUmvX8"}, 
    {"title": "World Music and Ethnomusicology", "link": "https://youtu.be/CCt-46BEJQU"}
]

education = [
    {"title": "Foundations of Education", "link": "https://youtu.be/3_oqeaj2gqE"},
    {"title": "Curriculum Design and Development", "link": "https://youtu.be/2kLQGU5KiBc"},
    {"title": "Assessment and Evaluation in Education", "link": "https://youtu.be/gGbQHnLNpVo"},
    {"title": "Classroom Management Strategies", "link": "https://youtu.be/u086rr7SRso"},
    {"title": "Educational Psychology and Learning Theories", "link": "https://youtu.be/sAxAegfVd00"},
    {"title": "Teaching Methods and Instructional Strategies", "link": "https://youtu.be/TbRThpeFKfs"},
    {"title": "Multicultural Education and Diversity in the Classroom", "link": "https://youtu.be/UFyCpEpviKY"},
    {"title": "Special Education and Inclusion Practices", "link": "https://youtu.be/nK2PDKPKd7k"},
    {"title": "Educational Technology Integration", "link": "https://youtu.be/lo9agDXhd3I"}, 
    {"title": "Research Methods in Education", "link": "https://youtu.be/nv7MOoHMM2k"}
]

@app.route("/", methods=["GET"])
def index():
    return "Prediction Model"

@app.route('/predict', methods=['POST'])
def predict():

    data = request.form['data']
    request_data = []
    response_data = []

    request_array = data.split(',')

    for item in request_array:
        if '"' not in item:
            request_data.append(item)

    for item_data in request_data:
        if "history" in item_data:
            random_data = random.sample(history, 3)
            response_data.append(random_data)
        else:
            if "science" in item_data:
                random_data = random.sample(science, 3)
                response_data.append(random_data)
            else:
                if "drawing" in item_data:
                    random_data = random.sample(drawing, 3)
                    response_data.append(random_data)
                else:
                    if "technology" in item_data:
                        random_data = random.sample(technology, 3)
                        response_data.append(random_data)
                    else:
                        if "music" in item_data:
                            random_data = random.sample(music, 3)
                            response_data.append(random_data)
                        else:
                            if "education" in item_data:
                                random_data = random.sample(education, 3)
                                response_data.append(random_data)
                            else:
                                print("Inputs are not in the parameter")

    print(response_data[1])
    return response_data


if __name__ == '__main__':
    app.run()
