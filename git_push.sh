git add .
read -p 'Write commit:' com
git commit -m "$com"
read -p 'Write branch: ' br
git push origin $br