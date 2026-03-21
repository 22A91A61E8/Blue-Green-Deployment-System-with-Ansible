\# Chatbot Evaluation Report



\## 1. Introduction

The goal of this project was to evaluate the feasibility of using a local LLM, \*\*Llama 3.2 3B\*\*, for customer support in an e-commerce scenario. We compared \*\*Zero-Shot\*\* prompting versus \*\*One-Shot\*\* prompting to see which method produces more relevant, coherent, and helpful responses.  



\## 2. Methodology

1\. \*\*Data Preparation\*\*:  

&#x20;  - We sourced 20 user queries from the Ubuntu Dialogue Corpus and adapted them to an e-commerce context.  

&#x20;  - Example: Technical query “My wifi driver is not working” was adapted to “My discount code isn't working.”  



2\. \*\*Prompt Engineering\*\*:  

&#x20;  - \*\*Zero-Shot Template\*\*: Provided the agent’s role and the customer query only.  

&#x20;  - \*\*One-Shot Template\*\*: Provided the agent’s role, a single example of an ideal query-response pair, and the customer query.  



3\. \*\*Evaluation\*\*:  

&#x20;  - Responses from both methods were recorded in `eval/results.md`.  

&#x20;  - Each response was scored on \*\*Relevance, Coherence, and Helpfulness\*\* (1–5).  



\## 3. Results \& Analysis

\- \*\*Overall Performance\*\*:

&#x20; - Zero-Shot responses were generally relevant and coherent, with occasional lower helpfulness scores (e.g., discount code query).  

&#x20; - One-Shot responses consistently scored higher, as the example guided the model toward more precise and actionable answers.  



\- \*\*Patterns Observed\*\*:

&#x20; - \*\*Zero-Shot\*\*: Slightly more generic answers; some queries needed interpretation.  

&#x20; - \*\*One-Shot\*\*: More structured, concise, and aligned with the e-commerce tone.  

&#x20; - Example:  

&#x20;   - Query: “My discount code isn’t working”  

&#x20;     - Zero-Shot: “Please check if your discount code is valid.” (Helpful, but generic)  

&#x20;     - One-Shot: “Ensure your discount code is valid and applied before checkout.” (More actionable)  



\- \*\*Average Scores\*\*:

&#x20; | Method       | Relevance | Coherence | Helpfulness |

&#x20; |-------------|-----------|-----------|-------------|

&#x20; | Zero-Shot   | 4.95      | 5.0       | 4.9         |

&#x20; | One-Shot    | 5.0       | 5.0       | 5.0         |



\## 4. Conclusion \& Limitations

\- \*\*Suitability\*\*: Llama 3.2 3B is suitable for local customer support simulations and small-scale e-commerce queries.  

\- \*\*Limitations\*\*:  

&#x20; 1. Responses are \*\*not connected to real-time order data\*\*.  

&#x20; 2. Potential for \*\*hallucinations or inaccurate advice\*\* on uncommon scenarios.  

&#x20; 3. Running locally on a CPU may result in \*\*slower response times\*\*.  

\- \*\*Next Steps\*\*:  

&#x20; 1. Integrate with real order data via APIs for dynamic responses.  

&#x20; 2. Explore \*\*few-shot prompting\*\* with 2–3 examples to further improve consistency.  

&#x20; 3. Compare Llama 3.2 with other models like Mistral 7B or Phi-3 Mini for performance evaluation.  



\## 5. FAQ (Common Issues)

1\. \*\*Ollama server connection errors\*\*: Ensure Ollama is running; verify endpoint `http://localhost:11434`.  

2\. \*\*Slow responses\*\*: Local CPU processing is slower than GPU servers.  

3\. \*\*Choosing good examples\*\*: Use simple, representative queries and concise responses for One-Shot prompts.  

4\. \*\*Alternative models\*\*: Other models can be pulled via `ollama pull <model\_name>` and used by updating `MODEL\_NAME` in `chatbot.py`.



