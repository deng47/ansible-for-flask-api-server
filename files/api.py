#!/usr/bin/python3

from flask import Flask, jsonify
import re

app = Flask(__name__)

@app.route('/api/MemFree')
def getfreemem():
    with open('/proc/meminfo', 'r') as f:
         freemem = f.readlines()[1]
         return jsonify(MemFree=re.findall(r'\d+ kB', freemem)[0])


@app.route('/api/SReclaimable')
def getrecmem():
    with open('/proc/meminfo', 'r') as f:
         meminfo = f.readlines()[22]
         return jsonify(SReclaimable=re.findall(r'\d+ kB', meminfo)[0])


@app.route('/api/loadavg')
def getload():
    with open('/proc/loadavg', 'r') as f:
         loadavg = f.read().split()
         return jsonify(loadavg=loadavg[0:3])


@app.route('/api/partitions')
def getpart():
    with open('/proc/partitions', 'r') as f:
         partitions = [ each.split()[-1] for each in f.readlines()[2:] ]
         return jsonify(Partitions=partitions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
