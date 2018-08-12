#!/usr/local/bin/python3.7

import requests
import time
import json
import os

cookies = {
    '_ga': '',
    'user': '',
    '_gid': '',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://intra.epitech.eu/user/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

params = (
    ('format', 'json'),
)
url = "https://intra.epitech.eu/user/{}/binome/"

def send_request(todo, done):
    email_address = todo.pop()
    print("[INFO] Done: {}  Todo: {}  Current: {}".format(len(done), len(todo), email_address))
    users = requests.get(url.format(email_address), headers=headers, params=params, cookies=cookies).json()
    for user in users["binomes"]:
        if user["login"] not in todo and user["login"] not in done:
            todo.append(user["login"])
    done.append(email_address)
    return todo, done

def write_file(filename, data):
    filename = 'data/{}.json'.format(filename) 
    with open(filename, 'w') as outfile:
        json.dump({"email_address": data}, outfile)
    print("[INFO] Saved file {}".format(filename))

todo = ["initial_email@epitech.eu"]
done = []

if __name__ == '__main__':
    os.system("mkdir -p data")
    while 0 != len(todo):
        if len(done) % 100 == 0 and 0 != len(done):
            write_file("done_{}".format(len(done)), done)
            write_file("todo_{}".format(len(done)), todo)
        todo, done = send_request(todo, done)

    write_file("final_{}".format(len(done)), done)
    print("[INFO] Finished. Todo: {}".format(len(todo)))
