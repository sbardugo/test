import glob, os


os.chdir('C:/Users/sbardugo/Desktop/ChangePassword Platform')

for filename in glob.glob("*.xml"):

    print(filename)