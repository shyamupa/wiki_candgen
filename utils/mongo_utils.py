import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import argparse
from pymongo import MongoClient


def list_mongo(host, port, args):
    client = MongoClient(host, port)
    print(client.max_pool_size)
    db = client['mymongo']
    if args["list"]:
        for name in sorted(db.list_collection_names()):
            print(name, db[name].count())
    elif args["drop"] and args["name"] is not None:
        name = args["name"]
        logging.info("dropping %s", name)
        db[name].drop()
    else:
        print("no action performed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('--port', default=27017, dest="port")
    parser.add_argument('--host', default="localhost", dest="host")
    parser.add_argument('--name')
    parser.add_argument('--drop', action="store_true", dest="drop")
    parser.add_argument('--list', action="store_true", dest="list")
    args = parser.parse_args()
    args = vars(args)
    list_mongo(host=args["host"], port=args["port"], args=args)
