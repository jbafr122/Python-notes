git add .
echo "What would you like the commit message to be?" 
read msg
git commit -m "$msg"
git push
echo "Successfully pushed to git repo"
