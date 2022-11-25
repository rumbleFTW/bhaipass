import os

# for item in os.listdir():
#     if '.' not in item:
#         for pth in os.listdir(item):
#             if "." not in pth:
#                 with open(item+"/"+pth+"/index.html", "r") as file:
#                     data = file.read()
#                     print(data)
#                 with open(item+"/"+pth+"/index.html", "w") as file:
#                     file.write(data.replace('window.close();', r'window.location.replace("https://csemoodle.tint.edu.in/")'))

######################################################################################

payload = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <script>navigator.clipboard.writeText(`
target123
`);setTimeout(() => {window.location.replace("https://csemoodle.tint.edu.in/")}, 2000)</script>
</head>
<body>
    
</body>
</html>
"""
for item in os.listdir('codes'):
    if '.' not in item:
        os.mkdir(item)
        for topic in os.listdir('codes\\'+item):
            pth = (item+'\\'+topic).replace('txt', '')
            os.mkdir(pth)
            with open('codes\\'+item+'\\'+topic, "r") as file:
                data = file.read()
            file.close()
            with open(pth+'\\'+'index.html', "w") as file:
                file.write(payload.replace('target123', data))
            

