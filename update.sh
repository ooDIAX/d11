sudo pkill gunicorn
docker compose down
docker compose up -d --build
pip install -r requirements.txt
echo "Sleeping for 10 seconds to allow the database to start up..."
sleep 10
python3 test-db.py
/home/ubuntu/.local/bin/gunicorn -b 0.0.0.0:8888 mini-server:app --daemon
# sleep 5
# tail -n 100 logs/webserver.log