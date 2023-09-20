import chromadb
import json

client = chromadb.PersistentClient(path="db")
collection = client.get_or_create_collection(name="fin1")


def create_id(assignment_name: str, task_number: str) -> str:
    return f"{assignment_name}-{task_number}"


def load_documents():
    with open("questions.json", "r") as file:
        data = json.load(file)

    all_tasks = []
    for assignment_name, value in data.items():
        for task_number, task_description in value.items():
            all_tasks.append(
                {
                    "assignment_name": assignment_name,
                    "task_number": task_number,
                    "task_description": task_description,
                }
            )

    ids = [
        create_id(task["assignment_name"], task["task_number"]) for task in all_tasks
    ]
    documents = [task["task_description"] for task in all_tasks]
    metadatas = [
        {"assignment_name": task["assignment_name"], "task_number": task["task_number"]}
        for task in all_tasks
    ]

    collection.add(ids=ids, documents=documents, metadatas=metadatas)


def main():
    load_documents()


if __name__ == "__main__":
    main()
