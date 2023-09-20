import chromadb
import argparse
import time

client = chromadb.PersistentClient(path="db")
collection = client.get_collection(name="fin1")


def search_documents(search_string, n_results):
    print("\nSearching...")
    time.sleep(0.5)

    results = collection.query(query_texts=[search_string], n_results=n_results)

    ids = results["ids"][0]
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    print("\n" + "-" * 50)
    # Loop through results
    for i in range(len(ids)):
        document = documents[i]
        metadata = metadatas[i]
        assignment_name = metadata["assignment_name"]
        task_number = metadata["task_number"]

        print(f"\n\033[1mResult {i+1}:\033[0m\n")
        print(f"\033[1mOpgave:\033[0m {assignment_name}")
        print(f"\033[1mDelopgave:\033[0m {task_number}\n")
        print(f"\033[1mTekst:\033[0m {document}")
        print("\n" + "-" * 50)

    print()


def main():
    parser = argparse.ArgumentParser(description="Search the database.")
    parser.add_argument("search_string", type=str, help="The search string.")
    parser.add_argument(
        "--n_results", default=5, type=int, help="Number of results to retrieve."
    )
    args = parser.parse_args()

    search_documents(args.search_string, args.n_results)


if __name__ == "__main__":
    main()
