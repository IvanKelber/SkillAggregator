import json
import csv
import re
from collections import Counter


def main():
    skills = ["java","python","go","golang","c","c++","c#","c/c++",
    "ruby","javascript","jquery","html","css","sql","nosql","php",
    "perl","rails","mvc","django","apache","aws","heroku","spark",
    "kafka","redis","cassandra","mongodb","rabbitmq","meteor.js",
    "meteor","node.js","react.js","d3.js","mysql","sympfony","numpy",
    "hadoop","rest","restful","json","xml","ios","gradle","maven","android",
    "pyramid","bash","tensorflow","r","matlab"]

    with open('../data/muse_jobs.json',"rb") as mj:
        data = json.load(mj)

    total_count = {}
    for job in data:
        counter = Counter(job["contents"].lower().split(' '))
        for skill in skills:
            if(counter[skill] > 0):
                total_count[skill] = total_count.get(skill,0) + 1

    print sorted(total_count.items(),key=lambda x: -x[1])
def findSkills(skills,content):
    for skill in skills:
        results = re.search("\s" + skill + "\s",content.lower())

if __name__ == '__main__':
    main()
