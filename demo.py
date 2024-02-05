a = {
"content":[
{
"attachment":{
"href":"cid:63f5e4909ca9205450a40030",
"len":4,
"name":"Checklist_Ericsson_PKC_INM_CGNAT.txt",
"type":"text/plain",
"xmime:contentType":"text/plain"
}
},
{
"attachment":{
"href":"cid:642d4b2aceab0054508de410",
"len":10338,
"name":"Gaurav Saini",
"type":"application/octet-stream",
"xmime:contentType":"application/octet-stream"
}
}
]
}

print(a['content'][1]['attachment']['name'])



