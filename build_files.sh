# build_files.sh

pip3 install -r requirements.txt
python3.11  manage.py collectstatic --no-input --clear

