import configparser

'''
    使用配置文件更加方便
    配置文件的使用，读取配置文件的内容
'''

filePath = "configure.txt"

# 实例化对象，生成config对象
config = configparser.ConfigParser()

# 调用配置对象的方法进行读取
config.read(filePath)

name = config.get("A", "name")
print(name)
age = config.get("A", "age")
print(age)

print(config.get("B", "name"), "is", config.get("B", "age"), "years old")
