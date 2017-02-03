import json
import csv
import re
from collections import Counter


def main():
    skills = ["java","python","go","golang","c","c\+\+","c#","c/c\+\+",
    "ruby","javascript","jquery","html","css","sql","nosql","php",
    "perl","rails","mvc","django","apache","aws","heroku","spark",
    "kafka","redis","cassandra","mongodb","rabbitmq","meteor.js",
    "meteor","node.js","react.js","d3.js","mysql","sympfony","numpy",
    "hadoop","rest","restful","json","xml","ios","gradle","maven","android",
    "pyramid","bash","tensorflow","r","matlab",'rust','.net',"tornado","unix",
    "linux","git","vcs","statistics","machine learning","distributed systems","networking",
    "operating systems","algorithms","data structures","scala","coffeescript",
    "framer.js","swift","objective-c","mongo"]

    with open('../data/muse_jobs.json',"rb") as mj:
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
                total_count[skill] = total_count.get(skill,0) + 1
        if(not hit):
            not_hit_urls.append(job["refs"]["landing_page"])

    print sorted(total_count.items(),key=lambda x: -x[1])
    print "====================="
    # for url in not_hit_urls:
    #     print url
    #     print "========================"
def findSkills(skills,content):
    for skill in skills:
        results = re.search("\s" + skill + "\s",content.lower())

if __name__ == '__main__':
    main()
