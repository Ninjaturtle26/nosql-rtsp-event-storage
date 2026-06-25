import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


NOSQL_ROOT = Path(__file__).resolve().parent
sys.path.insert(
    0,
    str(NOSQL_ROOT)
)

COLLECTIONS = (
    "events",
    "sessions",
    "cameras",
    "system_logs"
)


def now_iso():

    return datetime.now().replace(
        microsecond=0
    ).isoformat()


def new_demo_run():

    return "demo_" + datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


def print_document(
    title,
    document
):

    print(title)

    if document is None:

        print("null")

        return

    print(
        json.dumps(
            document,
            indent=2,
            ensure_ascii=False,
            default=json_default
        )
    )


def json_default(
    value
):

    if hasattr(
        value,
        "isoformat"
    ):

        return value.isoformat()

    return str(
        value
    )


def build_demo_documents(
    demo_run
):

    timestamp = now_iso()

    event_id = f"{demo_run}_event"
    camera_id = f"{demo_run}_camera"
    session_name = f"{demo_run}_session"
    log_id = f"{demo_run}_log"

    event_document = {
        "event_id": event_id,
        "project": "bed-monitoring-project",
        "camera": {
            "camera_id": camera_id,
            "location": "bedroom",
            "stream": "stream2"
        },
        "session": {
            "session_name": session_name,
            "started_at": timestamp
        },
        "event": {
            "type": "POSSIBLE_BED_EXIT",
            "start_frame": 100,
            "end_frame": 145
        },
        "files": {
            "attention_video": None,
            "session_video": (
                "outputs/camera1/live_sessions/"
                f"{session_name}_*.mp4"
            ),
            "possible_snapshot": (
                "outputs/camera1/possible_frames/"
                f"{event_id}_possible.jpg"
            )
        },
        "model": {
            "motion_model": "MOG2",
            "history": 336,
            "attention_window": 210
        },
        "created_at": timestamp,
        "notification": {
            "enabled": True,
            "status": "PENDING",
            "channel": "WHATSAPP",
            "sent_at": None,
            "retry_count": 0,
            "last_error": None
        },
        "demo": True,
        "demo_run": demo_run
    }

    session_document = {
        "session_name": session_name,
        "camera_id": camera_id,
        "project": "bed-monitoring-project",
        "status": "running",
        "started_at": timestamp,
        "created_at": timestamp,
        "demo": True,
        "demo_run": demo_run
    }

    camera_document = {
        "camera_id": camera_id,
        "project": "bed-monitoring-project",
        "location": "bedroom",
        "stream": "stream2",
        "status": "active",
        "current_session": session_name,
        "output_dir": "outputs/camera1",
        "last_seen_at": timestamp,
        "updated_at": timestamp,
        "demo": True,
        "demo_run": demo_run
    }

    log_document = {
        "log_id": log_id,
        "log_type": "CRUD_DEMO",
        "level": "INFO",
        "message": "Demo document inserted from nosql_model/crud_demo.py",
        "metadata": {
            "event_id": event_id,
            "camera_id": camera_id,
            "session_name": session_name
        },
        "created_at": timestamp,
        "demo": True,
        "demo_run": demo_run
    }

    return {
        "events": event_document,
        "sessions": session_document,
        "cameras": camera_document,
        "system_logs": log_document
    }


def latest_demo_document(
    db,
    collection_name,
    demo_run=None
):

    query = {
        "demo":
            True
    }

    if demo_run:

        query["demo_run"] = demo_run

    return db[
        collection_name
    ].find_one(
        query,
        sort=[
            (
                "_id",
                -1
            )
        ]
    )


def insert_demo(
    db,
    demo_run
):

    print("\n== INSERT ==")

    documents = build_demo_documents(
        demo_run
    )

    for collection_name, document in documents.items():

        result = db[
            collection_name
        ].insert_one(
            document
        )

        print(
            f"[INSERT] {collection_name} inserted_id={result.inserted_id}"
        )


def find_demo(
    db,
    demo_run=None
):

    print("\n== FIND ==")

    for collection_name in COLLECTIONS:

        query = {
            "demo":
                True
        }

        if demo_run:

            query["demo_run"] = demo_run

        count = db[
            collection_name
        ].count_documents(
            query
        )

        document = latest_demo_document(
            db,
            collection_name,
            demo_run=demo_run
        )

        print(
            f"[FIND] {collection_name} matched={count}"
        )

        print_document(
            f"[FIND] Latest {collection_name}:",
            document
        )


def update_one_demo_document(
    db,
    collection_name,
    update_data,
    demo_run=None
):

    document = latest_demo_document(
        db,
        collection_name,
        demo_run=demo_run
    )

    if document is None:

        print(
            f"[UPDATE] {collection_name} skipped: no demo document found"
        )

        return

    result = db[
        collection_name
    ].update_one(

        {
            "_id":
                document["_id"]
        },

        {
            "$set":
                update_data
        }
    )

    print(
        f"[UPDATE] {collection_name} matched={result.matched_count} "
        f"modified={result.modified_count}"
    )


def update_demo(
    db,
    demo_run=None
):

    print("\n== UPDATE ==")

    timestamp = now_iso()

    update_one_demo_document(
        db,
        "events",
        {
            "notification.status": "SENT",
            "notification.sent_at": timestamp,
            "notification.last_error": None
        },
        demo_run=demo_run
    )

    update_one_demo_document(
        db,
        "sessions",
        {
            "status": "finished",
            "ended_at": timestamp
        },
        demo_run=demo_run
    )

    update_one_demo_document(
        db,
        "cameras",
        {
            "status": "maintenance",
            "last_seen_at": timestamp,
            "updated_at": timestamp
        },
        demo_run=demo_run
    )

    update_one_demo_document(
        db,
        "system_logs",
        {
            "level": "SUCCESS",
            "message": "Demo document updated by UPDATE operation",
            "updated_at": timestamp
        },
        demo_run=demo_run
    )


def delete_demo(
    db,
    demo_run=None
):

    print("\n== DELETE ==")

    query = {
        "demo":
            True
    }

    if demo_run:

        query["demo_run"] = demo_run

    for collection_name in COLLECTIONS:

        result = db[
            collection_name
        ].delete_many(
            query
        )

        print(
            f"[DELETE] {collection_name} deleted={result.deleted_count}"
        )


def run_all(
    db,
    demo_run,
    keep_documents
):

    insert_demo(
        db,
        demo_run
    )

    find_demo(
        db,
        demo_run=demo_run
    )

    update_demo(
        db,
        demo_run=demo_run
    )

    find_demo(
        db,
        demo_run=demo_run
    )

    if keep_documents:

        print(
            "\n[KEEP] Demo documents were kept for MongoDB Compass prints."
        )

        return

    delete_demo(
        db,
        demo_run=demo_run
    )

    find_demo(
        db,
        demo_run=demo_run
    )


def run_menu(
    db
):

    demo_run = new_demo_run()

    while True:

        print("\nNoSQL CRUD demo")
        print(f"Current demo_run: {demo_run}")
        print("1 - INSERT demo documents")
        print("2 - FIND demo documents")
        print("3 - UPDATE demo documents")
        print("4 - DELETE demo documents")
        print("5 - RUN ALL and keep documents")
        print("6 - New demo_run")
        print("0 - Exit")

        option = input("Choose an option: ").strip()

        if option == "1":

            insert_demo(
                db,
                demo_run
            )

        elif option == "2":

            find_demo(
                db,
                demo_run=demo_run
            )

        elif option == "3":

            update_demo(
                db,
                demo_run=demo_run
            )

        elif option == "4":

            delete_demo(
                db,
                demo_run=demo_run
            )

        elif option == "5":

            run_all(
                db,
                demo_run,
                keep_documents=True
            )

        elif option == "6":

            demo_run = new_demo_run()

        elif option == "0":

            break

        else:

            print("Invalid option.")


def parse_args():

    parser = argparse.ArgumentParser(
        description=(
            "Demonstrates INSERT, FIND, UPDATE and DELETE "
            "in the bed_monitoring MongoDB database."
        )
    )

    parser.add_argument(
        "operation",
        nargs="?",
        choices=[
            "menu",
            "insert",
            "find",
            "update",
            "delete",
            "all"
        ],
        default="menu"
    )

    parser.add_argument(
        "--demo-run",
        default=None,
        help="Demo identifier used to find/update/delete the same documents."
    )

    parser.add_argument(
        "--keep",
        action="store_true",
        help="Keep demo documents after the all operation."
    )

    parser.add_argument(
        "--mongo-uri",
        default=os.getenv(
            "MONGO_URI",
            "mongodb://localhost:27017"
        )
    )

    parser.add_argument(
        "--database",
        default=os.getenv(
            "MONGO_DATABASE",
            "bed_monitoring"
        )
    )

    return parser.parse_args()


def main():

    args = parse_args()

    try:

        from src.storage.mongodb_client import MongoDBClient

    except ModuleNotFoundError as error:

        if error.name == "pymongo":

            print(
                "Missing dependency: pymongo. Run "
                "`python3 -m pip install -r nosql_model/requirements.txt`.",
                file=sys.stderr
            )

            return 1

        raise

    demo_run = (
        args.demo_run
        or new_demo_run()
    )

    mongo = MongoDBClient(
        uri=args.mongo_uri,
        database=args.database
    )

    try:

        db = mongo.connect()

        print(
            f"Connected to database={args.database}"
        )

        print(
            f"Demo run={demo_run}"
        )

        if args.operation == "menu":

            run_menu(
                db
            )

        elif args.operation == "insert":

            insert_demo(
                db,
                demo_run
            )

        elif args.operation == "find":

            find_demo(
                db,
                demo_run=args.demo_run
            )

        elif args.operation == "update":

            update_demo(
                db,
                demo_run=args.demo_run
            )

        elif args.operation == "delete":

            delete_demo(
                db,
                demo_run=args.demo_run
            )

        elif args.operation == "all":

            run_all(
                db,
                demo_run,
                keep_documents=args.keep
            )

    finally:

        mongo.close()

    return 0


if __name__ == "__main__":

    raise SystemExit(
        main()
    )
