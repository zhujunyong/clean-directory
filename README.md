# clean-directory
clean unless files(directories) in specify directory

# 在mac, linux等类unix系统上运行

# 删除特定文件名的文件或者目录，比如.svn目录，.settings目录，.project文件和Thumbs.db文件等
clean_fullfile.py

usage: python3 clean_fullfile.py /Users/zhujunyong/Downloads/workspace .project .classpath .svn .settings .git desktop.ini target .gitignore .metadata bin Thumbs.db

# 删除特定后缀名的文件，比如.class文件和.jar文件等
clean_ext.py

usage: python3 clean_ext.py /Users/zhujunyong/Downloads/workspace .class .jar .war



