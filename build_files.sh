# build_files.sh

pip install -r requirements.txt
python3.11.9 manage.py collectstatic --no-input --clear

