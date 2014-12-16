import fb #To install this package run: sudo pip install fb
from facepy import GraphAPI #To install this package run: sudo pip install facepy

import time


token="##GENERATE ACCESS TOKEN USING FACEBOOK GRAPH EXPLORER"#Insert access token here.  
facebook=fb.graph.api(token)
graph1 = GraphAPI(token)


vid=220533111292436 #This is flipkart page's facebook id
query=str(vid)+"/posts?fields=id&limit=5000000000"
r=graph1.get(query)



idlist=[x['id'] for x in r['data']]
print("There are "+ str(len(idlist)) +" commentable posts.")

char1='y'
count=0
message = '##YOUR COMPLAINT GOES HERE##'
if char1=='y':
    nos=input("Enter number of posts to be commented on: ")
    if nos<=len(idlist):
       for indid in idlist[len(idlist)-(nos):len(idlist)-1]:
    	  count=count+1
          facebook.publish(cat="comments",id=indid,message=str(message)+str(count))
	  time.sleep(6)
	  
          
          print("Complaint number:"+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])	  
    else: 
          print("Not that many commentable posts available. ")
else :
  print("No complaints made.")
