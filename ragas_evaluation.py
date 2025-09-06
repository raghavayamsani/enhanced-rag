from langchain.chat_models import ChatOpenAI
from ragas.llms import LangchainLLMWrapper as ragas_llm
import os

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.metrics import faithfulness, context_precision, context_recall, answer_relevancy, answer_similarity, answer_correctness
from ragas import evaluate, EvaluationDataset
from evaluation_samples import samples






dataset = EvaluationDataset(samples=samples)


ragas_llm.chat_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

results = evaluate(
    dataset=dataset,
    metrics=[faithfulness, context_precision, context_recall, answer_relevancy, answer_similarity, answer_correctness]
)

#print(results)
faithfulness = float(results['faithfulness'][0])
context_precision = float(results['context_precision'][0])
context_recall = float(results['context_recall'][0])
answer_relevancy = float(results['answer_relevancy'][0])
answer_similarity = float(results['semantic_similarity'][0])
answer_correctness = float(results['answer_correctness'][0])


metric_names = [
    "Faithfulness",
    "Context Precision",
    "Context Recall",
    "Answer Relevancy",
    "Answer Similarity",
    "Answer Correctness"
]
values = [
    faithfulness,
    context_precision,
    context_recall,
    answer_relevancy,
    answer_similarity,
    answer_correctness
]

table_rows = [values]           # one row
headers    = metric_names


def tabulate(rows, headers=None, tablefmt="simple"):
    hdr = " | ".join(f"{h:^15}" for h in headers) if headers else ""
    sep = "-" * len(hdr.replace("|", "-"))
    body = "\n".join(
        " | ".join(f"{v:^15.4g}" for v in row) for row in rows
    )
    return f"{hdr}\n{sep}\n{body}"

print(tabulate(table_rows, headers=headers, tablefmt="grid"))