from langgraph.graph import StateGraph
from typing import TypedDict
from retrieval import get_retriever

# ✅ OLLAMA MODEL
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

# STATE STRUCTURE
class State(TypedDict):
    query: str
    answer: str

# STEP 1: PROCESS QUERY
def process(state: State):
    query = state["query"]

    retriever = get_retriever()
    docs = retriever.invoke(query)

    if not docs:
        print("⚠️ Escalating to human...")
        return {"answer": "Human agent response: Refunds are allowed within 7 days"}

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question using the context below:

{context}

Question: {query}
"""

    response = llm.invoke(prompt)

    return {"answer": response}


# BUILD GRAPH
def build():
    builder = StateGraph(State)

    # only ONE node
    builder.add_node("process", process)

    # correct flow
    builder.set_entry_point("process")
    builder.set_finish_point("process")

    app = builder.compile()
    return app