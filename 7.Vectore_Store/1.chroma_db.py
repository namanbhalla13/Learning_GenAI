from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
PERSIST_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "sample"
EMBEDDING_MODEL = "text-embedding-3-small"


PLAYERS = [
    {
        "id": "virat_kohli",
        "content": (
            "Virat Kohli is one of the most successful and consistent batsmen "
            "in IPL history."
        ),
        "team": "Royal Challengers Bangalore",
    },
    {
        "id": "rohit_sharma",
        "content": "Rohit Sharma is the most successful captain in IPL history.",
        "team": "Mumbai Indians",
    },
    {
        "id": "ms_dhoni",
        "content": "MS Dhoni is a legendary captain known for finishing matches.",
        "team": "Chennai Super Kings",
    },
    {
        "id": "kl_rahul",
        "content": "KL Rahul is a stylish top-order batsman.",
        "team": "Lucknow Super Giants",
    },
    {
        "id": "andre_russell",
        "content": "Andre Russell is a powerful all-rounder.",
        "team": "Kolkata Knight Riders",
    },
    {
        "id": "hardik_pandya",
        "content": "Hardik Pandya is a dynamic all-rounder.",
        "team": "Gujarat Titans",
    },
]


def build_documents(players):
    ids = [player["id"] for player in players]
    docs = [
        Document(
            page_content=player["content"],
            metadata={"team": player["team"], "player_id": player["id"]},
        )
        for player in players
    ]
    return ids, docs


def sync_documents(vector_store, ids, docs):
    """Add only missing docs and re-embed only changed docs."""
    existing = vector_store.get(ids=ids, include=["documents", "metadatas"])
    existing_by_id = {
        doc_id: {
            "page_content": existing["documents"][index],
            "metadata": existing["metadatas"][index],
        }
        for index, doc_id in enumerate(existing["ids"])
    }

    docs_to_add = []
    ids_to_add = []
    docs_to_update = []
    ids_to_update = []

    for doc_id, doc in zip(ids, docs):
        stored_doc = existing_by_id.get(doc_id)

        if stored_doc is None:
            ids_to_add.append(doc_id)
            docs_to_add.append(doc)
            continue

        if (
            stored_doc["page_content"] != doc.page_content
            or stored_doc["metadata"] != doc.metadata
        ):
            ids_to_update.append(doc_id)
            docs_to_update.append(doc)

    if docs_to_add:
        vector_store.add_documents(documents=docs_to_add, ids=ids_to_add)

    for doc_id, doc in zip(ids_to_update, docs_to_update):
        vector_store.update_document(document_id=doc_id, document=doc)

    return len(docs_to_add), len(docs_to_update)


def print_documents(vector_store):
    stored = vector_store.get(include=["documents", "metadatas"])

    print(f"\nStored documents: {len(stored['ids'])}")
    for doc_id, content, metadata in zip(
        stored["ids"], stored["documents"], stored["metadatas"]
    ):
        print(f"- {doc_id}: {content} | {metadata}")


def print_search_results(title, results):
    print(f"\n{title}")
    for index, result in enumerate(results, start=1):
        if isinstance(result, tuple):
            doc, score = result
            print(f"{index}. score={score:.4f} | {doc.page_content} | {doc.metadata}")
        else:
            print(f"{index}. {result.page_content} | {result.metadata}")


def update_player(vector_store, player_id, content, team):
    updated_doc = Document(
        page_content=content,
        metadata={"team": team, "player_id": player_id},
    )
    vector_store.update_document(document_id=player_id, document=updated_doc)


def main():
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    vector_store = Chroma(
        embedding_function=embedding_model,
        persist_directory=str(PERSIST_DIR),
        collection_name=COLLECTION_NAME,
    )

    doc_ids, documents = build_documents(PLAYERS)
    added_count, updated_count = sync_documents(vector_store, doc_ids, documents)

    print(f"Sync complete: added={added_count}, updated={updated_count}")
    print_documents(vector_store)

    query = "Who among these players are all-rounders?"

    print_search_results(
        "Similarity search",
        vector_store.similarity_search(query=query, k=2),
    )

    print_search_results(
        "Similarity search with score",
        vector_store.similarity_search_with_score(query=query, k=2),
    )

    print_search_results(
        "Metadata filter",
        vector_store.similarity_search_with_score(
            query="captain",
            k=2,
            filter={"team": "Chennai Super Kings"},
        ),
    )

    # Update example:
    # update_player(
    #     vector_store,
    #     player_id="virat_kohli",
    #     content=(
    #         "Virat Kohli is one of the most successful and consistent batsmen in IPL "
    #         "history. He is known for his aggressive style of play."
    #     ),
    #     team="Royal Challengers Bangalore",
    # )

    # Delete example:
    # vector_store.delete(ids=["virat_kohli"])


if __name__ == "__main__":
    main()
