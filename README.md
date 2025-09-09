# Enhanced RAG: Hybrid Graph-Based Retrieval with LLM Reranking

A novel Retrieval-Augmented Generation system that combines graph-based text indexing with Large Language Model (LLM) reranking for superior contextual awareness and retrieval accuracy.

## 🚀 Overview

Current RAG systems suffer from fragmented responses and inadequate contextual awareness due to flat data representations. Our hybrid approach addresses these limitations by:

- **Combining structural insights** from graph-based retrieval with **semantic understanding** from LLM reranking
- **Capturing complex inter-entity relationships** through graph representations
- **Enhancing contextual refinement** beyond traditional embedding-based approaches

## 📊 Performance Highlights

Our system demonstrates significant improvements across multiple domains:

| Domain | Faithfulness | Answer Correctness | Answer Relevancy |
|--------|-------------|-------------------|------------------|
| Agriculture | **1.0000** (+31.7%) | **0.8328** (+26.5%) | **0.9519** (maintained) |
| Computer Science | **1.0000** (maintained) | **0.8563** (+39.0%) | **0.9737** (+1.2%) |
| Legal | **1.0000** (+31.7%) | **0.9910** (+19.2%) | **1.0000** (+20.2%) |
| Mixed | **0.4000** (+20.0%) | **0.6528** (+6.7%) | **0.9445** (+9.9%) |

## 🏗️ Architecture

The system employs a modular hybrid architecture:

1. **Document Processing Pipeline**
   - Metadata storage in PostgreSQL
   - Vector embeddings in Weaviate
   - Graph relationships in Neo4j

2. **Dual Retrieval System**
   - Graph-based retrieval for structural relationships
   - Vector-based retrieval for semantic similarity

3. **LLM Reranking Module**
   - Semantic relevance assessment
   - Context-aware result optimization

## 🛠️ Technical Stack

- **Metadata Store**: PostgreSQL
- **Vector Store**: Weaviate
- **Graph Store**: Neo4j
- **LLM**: OpenAI GPT-4o-mini
- **Embeddings**: OpenAI text-embedding models
- **Reranking**: Cohere Reranking with OnDevice fallback
- **Framework**: Python with modular architecture

## Evaluation Metrics

- **Faithfulness**: Factual accuracy with respect to context
- **Context Precision**: Relevance of retrieved context
- **Context Recall**: Completeness of relevant context retrieval
- **Answer Relevancy**: Alignment with user query
- **Semantic Similarity**: Semantic closeness to expected answer
- **Answer Correctness**: Overall correctness and completeness

## 🔬 Research Applications

### Primary Use Cases

1. **Scientific Literature Search**
   - Cross-domain knowledge synthesis
   - Complex inter-entity relationship understanding
   - Comprehensive research discovery

2. **Recommendation Systems**
   - Enhanced user behavior understanding
   - Multi-dimensional preference modeling
   - Context-aware suggestions

3. **Knowledge Management**
   - Enterprise knowledge bases
   - Legal document analysis
   - Technical documentation systems

## 🐛 Known Limitations

- **Scalability**: Computational overhead from dual retrieval may impact large-scale deployments
- **Domain Coverage**: Current evaluation limited to four domains
- **Graph Construction**: Relies on predefined entity extraction methods

## 🔮 Future Improvements

- [ ] Adaptive graph construction algorithms
- [ ] Multi-modal graph representations
- [ ] Dynamic parameter optimization
- [ ] Federated learning approaches
- [ ] Enhanced caching mechanisms

## 👥 Team

- **Giridharan Perumanam Bhaskar** - Graph retrieval and system integration
- **Raghava Krishna Yamsani** - Reranking module and API development  
- **Srikanth Chigurupati** - Evaluation and documentation

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/raghavayamsani/enhanced-rag/issues)
- **Discussions**: [GitHub Discussions](https://github.com/raghavayamsani/enhanced-rag/discussions)
- **Documentation**: [Full Documentation](https://enhanced-rag.readthedocs.io)

## 🙏 Acknowledgments

- UltraDomain dataset contributors
- LightRAG and RankLLM research teams
- OpenAI for GPT-4o-mini and embedding models
- The broader RAG research community

---

**Built with ❤️ by Team 11**
