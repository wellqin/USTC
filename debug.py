# Test File
a = {"lishuntao": {"company": "hut"},
     "lishuntao1": {"company": "hut1"}
     }
new_dict = a.setdefault("litao", "hugongda")
print(new_dict)  # hugongda
print(a)  # hugongda
