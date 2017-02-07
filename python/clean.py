import json
import csv
import re
from collections import Counter

# skills = ["java","python","go","golang","c","c\+\+","c#","c/c\+\+",
# "ruby","javascript","jquery","html","css","sql","nosql","php",
# "perl","rails","mvc","django","apache","aws","heroku","spark",
# "kafka","redis","cassandra","mongodb","rabbitmq","meteor.js",
# "meteor","node.js","react.js","d3.js","mysql","symfony","numpy",
# "hadoop","rest","restful","json","xml","ios","gradle","maven","android",
# "pyramid","bash","tensorflow","r","matlab",'rust','.net',"tornado","unix",
# "linux","git","vcs","statistics","machine learning","distributed systems","networking",
# "operating systems","algorithms","data structures","scala","coffeescript",
# "framer.js","swift","objective-c","mongo","jira","angularjs","nodejs","oop",
# "object oriented","object-oriented"]
skills = {'jira': 'JIRA', 'gradle': 'Gradle', 'pyramid': 'Pyramid',
'php': 'PHP', 'mongo': 'MongoDB', 'nosql': 'NoSQL', 'nodejs': 'Node.js',
'c#': 'C#', 'meteor.js': 'MeteorJS', 'mysql': 'SQL', 'rest': 'REST', 'kafka': 'Kafka',
'node.js': 'Node.js', 'object oriented': 'OOP', 'objective-c': 'Objective-C', 'c\\+\\+': 'C/C++',
'angularjs': 'AngularJS', 'linux': 'Linux', 'go': 'Go', 'framer.js': 'Framer.js',
'django': 'Django', 'distributed systems': 'Distributed Systems', 'cassandra': 'Cassandra',
'xml': 'XML', 'git': 'Git', 'java': 'Java', 'json': 'JSON', 'scala': 'Scala',
'swift': 'Swift', 'unix': 'Unix', 'redis': 'Redis', 'hadoop': 'Hadoop', 'rails': 'Rails',
'perl': 'Perl', 'coffeescript': 'CoffeeScript', 'heroku': 'Heroku', 'vcs': 'VCS',
'matlab': 'Matlab', 'meteor': 'MeteorJS', 'mongodb': 'MongoDB', 'tensorflow': 'TensorFlow',
'android': 'Android', 'numpy': 'NumPy', 'css': 'CSS', 'symfony': 'Symfony',
'python': 'Python', 'ios': 'iOS', 'javascript': 'Javascript', 'aws': 'AWS',
'maven': 'Maven', 'data structures': 'Data Structures', 'statistics': 'Statistics',
'tornado': 'Tornado', 'oop': 'OOP', 'c/c\\+\\+': 'C/C++', 'sql': 'SQL', 'apache': 'Apache',
'networking': 'Networking', 'spark': 'Spark', 'r': 'R', 'ruby': 'Ruby', 'bash': 'Bash',
'jquery': 'jQuery', 'golang': 'Go', 'c': 'C/C++', '.net': '.NET', 'html': 'HTML',
'rabbitmq': 'RabbitMQ', 'machine learning': 'Machine Learning', 'react.js': 'React',
'object-oriented': 'OOP', 'mvc': 'MVC', 'algorithms': 'Algorithms',
'operating systems': 'Operating Systems', 'd3.js': 'D3', 'restful': 'REST', 'rust': 'Rust'}

def main():


    with open('../static/data/muse_jobs.json',"rb") as mj:
        data = json.load(mj)

    total_count = {}
    not_hit_urls = []
    total_posts = float(len(data))
    for job in data:
        hit = False
        for skill in skills:
            regex = re.compile("\W"+skill+"[ .,]")
            if(re.search(regex,job["contents"].lower())):
                hit = True
                total_count[skills[skill]] = total_count.get(skills[skill],0) + 1
        if(not hit):
            not_hit_urls.append(job["refs"]["landing_page"])

    print "====================="
    with open('../static/data/counts.csv',"wb")as counts, open("../static/data/topten.csv","wb") as topten:
        writer = csv.writer(counts)
        ttwriter = csv.writer(topten)
        header = ["Skill","Count","Percentage"]
        writer.writerow(header)
        ttwriter.writerow(header)
        k = 0
        for skill,count in sorted(total_count.items(),key=lambda x: -x[1]):
            if(k < 10):
                ttwriter.writerow([skill,count,'%.2f'%((count/total_posts)*100)])
            k += 1
            writer.writerow([skill,count,'%.2f'%((count/total_posts)*100)])

    # for url in not_hit_urls:
    #     print url
    #     print "========================"
def findSkills(skills,content):
    for skill in skills:
        results = re.search("\s" + skill + "\s",content.lower())

if __name__ == '__main__':
    main()
