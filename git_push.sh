git add .
read -p 'Write commit:' com
git commit -m "$com"
git push orig_bas feature/reports