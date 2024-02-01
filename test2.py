a = {"python":1,"java":2 ,"js":4}


res = {key:value for key, value in a.items() if key != "js"}


print(res)