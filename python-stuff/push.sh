# pushes changes to github repo and asks the user for a commit msg
# use "sh push.sh" or whatever shell script name is to run script 

git add .
echo "What would you like the commit message to be?" 
read msg
git commit -m "$msg"
git push
echo "Successfully pushed to git repo"
