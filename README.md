# ansible-for-flask-api-server

Use ansible playbook to deploy a flask api server
  - the playbook will install python3, pip and flask
  - then it will config the api.py to run as a systemd daemon and send logs to rsyslog
  - the api.py accepts https requests for localhost status, like realtime cpu, mem usage and partitiones
  - it's tested on a CentOS7 Google Compute Engine. Firewall rules and file paths may need to be modified if it runs on other platform

Security Risk:
  - It uses the same self-signed certificate keypair on different servers

Todo: Documentation
