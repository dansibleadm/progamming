git add .
read -p 'Write commit:' com
git commit -m "$com"
read -p 'Write local branch: ' l_br
read -p 'Write branch: ' br
git push $l_br $br